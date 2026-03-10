from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from apps.leads.forms import LeadForm
from apps.lots.models import Lot
from apps.projects.models import Project


class HomeView(FormView):
    template_name = "pages/home.html"
    form_class = LeadForm

    def get_active_project(self):
        return (
            Project.objects.filter(active=True, featured=True)
            .order_by("-updated_at", "-created_at")
            .first()
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["project"] = self.get_active_project()
        return kwargs

    def get_map_lots(self, project):
        if not project:
            return []

        lots = project.lots.order_by("order", "block", "number")
        map_lots = []

        for lot in lots:
            if lot.map_feature:
                map_lots.append(lot.map_feature)

        return map_lots

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_active_project()

        featured_lots = []
        available_lots = []

        if project:
            featured_lots = list(
                project.lots.filter(featured=True).order_by("order", "block", "number")[:6]
            )
            available_lots = list(
                project.lots.filter(status=Lot.STATUS_AVAILABLE).order_by("order", "block", "number")[:12]
            )

        context["project"] = project
        context["featured_lots"] = featured_lots
        context["available_lots"] = available_lots
        context["map_lots"] = self.get_map_lots(project)
        return context

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.project = self.get_active_project()
        lead.source = lead.SOURCE_WEBSITE
        lead.save()

        messages.success(
            self.request,
            "Tu consulta fue enviada correctamente. Te contactaremos pronto.",
        )
        return redirect(f"{reverse('pages:home')}#contacto")

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Revisa los datos del formulario. Hay campos obligatorios incompletos.",
        )
        return super().form_invalid(form)