# Edén Loteamiento - Base Django

Base técnica del proyecto **Edén Loteamiento**, preparada para evolucionar hacia una landing page inmobiliaria con:

- panel administrativo
- gestión de loteamiento y lotes
- captación de leads
- SEO básico
- analítica
- mapa y disponibilidad

La ubicación base del proyecto es:

- **Nombre del proyecto:** Edén Loteamiento
- **Ubicación:** Tomás Romero Pereira, Itapúa, Paraguay
- **Coordenadas:** `-26.494759, -55.273071`

---

## 1. Objetivo de este repositorio

Este repositorio contiene la **base inicial profesional en Django** sobre la cual se construirá el sistema web del proyecto.

Actualmente la base está pensada para dejar listo:

- el entorno de desarrollo
- la estructura del proyecto Django
- la separación en apps
- la preparación para PostgreSQL
- la organización de `templates`, `static`, `media` y `requirements`
- la configuración pensada para desarrollo local y futura producción
- el versionado correcto con Git y GitHub

Este README está escrito para que **cualquier persona que clone el repositorio en Windows o Linux** pueda instalar todo correctamente y dejar el entorno operativo.

---

## 2. Stack base recomendado

Este proyecto fue planteado con esta base:

- **Python 3.13.x**
- **Django 5.2.x**
- **PostgreSQL 17**
- **Git**

> Si usas otra versión cercana y compatible, puede funcionar, pero esta es la base recomendada para mantener consistencia con el proyecto.

---

## 3. Estructura actual del proyecto

La estructura actual esperada del repositorio es esta:

```text
EdenLoteamiento/
├─ .venv/
├─ apps/
│  ├─ core/
│  ├─ pages/
│  ├─ projects/
│  ├─ lots/
│  ├─ leads/
│  ├─ seo/
│  └─ analytics/
├─ config/
│  ├─ settings/
│  │  ├─ __init__.py
│  │  ├─ base.py
│  │  ├─ local.py
│  │  └─ production.py
│  ├─ asgi.py
│  ├─ urls.py
│  └─ wsgi.py
├─ docs/
├─ media/
│  ├─ projects/
│  ├─ lots/
│  ├─ gallery/
│  └─ plans/
├─ requirements/
│  ├─ base.txt
│  ├─ local.txt
│  └─ production.txt
├─ static/
│  ├─ css/
│  ├─ js/
│  ├─ img/
│  ├─ icons/
│  └─ vendors/
├─ templates/
│  ├─ base/
│  ├─ includes/
│  ├─ pages/
│  ├─ projects/
│  ├─ lots/
│  └─ leads/
├─ .env
├─ .gitignore
└─ manage.py
```

> `.venv/` es local y no debe subirse al repositorio.

---

## 4. Requisitos previos

Antes de ejecutar el proyecto necesitas instalar:

- Python
- Git
- PostgreSQL

En Windows también conviene tener:

- PowerShell
- Visual Studio Code o editor equivalente
- pgAdmin, si prefieres administrar PostgreSQL visualmente

En Linux:

- terminal bash
- gestor de paquetes (`apt`, `dnf`, etc.)

---

## 5. Instalación en Windows

### 5.1 Instalar Python

1. Descarga Python desde la web oficial.
2. Ejecuta el instalador.
3. Marca **Add Python to PATH**.
4. Deja habilitado:
   - `pip`
   - `venv`
   - `py launcher`
5. Finaliza instalación.

Verifica en PowerShell:

```powershell
python --version
pip --version
```

Si `python` no responde, prueba:

```powershell
py --version
```

---

### 5.2 Instalar Git

1. Descarga Git desde la web oficial.
2. Instálalo con las opciones por defecto.
3. Verifica:

```powershell
git --version
```

---

### 5.3 Instalar PostgreSQL

1. Descarga PostgreSQL para Windows desde la web oficial.
2. Ejecuta el instalador.
3. Durante la instalación deja marcadas estas opciones:
   - PostgreSQL Server
   - pgAdmin
   - Command Line Tools
4. Define una contraseña para el usuario `postgres`.
5. Deja el puerto por defecto: `5432`.

---

### 5.4 Verificar si `psql` funciona en Windows

Prueba en PowerShell:

```powershell
psql --version
```

Si aparece este error:

```text
psql : El término 'psql' no se reconoce...
```

normalmente significa que **PostgreSQL sí está instalado, pero la carpeta `bin` no está agregada al PATH**.

La ruta típica es:

```text
C:\Program Files\PostgreSQL\17\bin
```

#### Cómo agregar PostgreSQL al PATH en Windows

1. Busca: **Editar las variables de entorno del sistema**
2. Abre **Variables de entorno**
3. Edita la variable `Path`
4. Agrega esta ruta:

```text
C:\Program Files\PostgreSQL\17\bin
```

5. Acepta todo
6. Cierra PowerShell y vuelve a abrirlo
7. Ejecuta otra vez:

```powershell
psql --version
```

#### Verificación rápida sin tocar PATH

También puedes probar así:

```powershell
& "C:\Program Files\PostgreSQL\17\bin\psql.exe" --version
```

Si eso funciona, PostgreSQL está bien instalado y el problema era solo el `PATH`.

---

## 6. Instalación en Linux

### 6.1 Instalar Python, venv y Git

En Debian/Ubuntu:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
```

Verifica:

```bash
python3 --version
pip3 --version
git --version
```

---

### 6.2 Instalar PostgreSQL

En Debian/Ubuntu:

```bash
sudo apt install -y postgresql postgresql-contrib
```

Verifica:

```bash
psql --version
```

Si el servicio no arranca automáticamente:

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo systemctl status postgresql
```

---

## 7. Clonar el repositorio

### Por HTTPS

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

> Reemplaza `TU_USUARIO` y `TU_REPOSITORIO` por los valores reales del repositorio.

---

## 8. Crear y activar el entorno virtual

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego vuelve a activar:

```powershell
.venv\Scripts\Activate.ps1
```

Cuando se activa correctamente, verás algo así:

```text
(.venv) PS C:\ruta\del\proyecto>
```

---

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 9. Instalar dependencias Python

Con el entorno virtual activo, actualiza `pip`.

### Windows

```powershell
python -m pip install --upgrade pip
```

### Linux

```bash
python3 -m pip install --upgrade pip
```

Luego instala dependencias.

### Si usarás instalación directa base

```bash
pip install "Django>=5.2,<5.3" "psycopg[binary]" python-decouple Pillow whitenoise django-extensions
```

### Si el proyecto ya trae requirements

```bash
pip install -r requirements/base.txt
```

> Si `requirements/local.txt` o `requirements/production.txt` ya estuvieran definidos y encadenados, usa los que correspondan. En esta base inicial, el archivo mínimo esperado es `requirements/base.txt`.

---

## 10. Configurar PostgreSQL

### Opción A - usando pgAdmin en Windows

1. Abre **pgAdmin**
2. Conéctate al servidor PostgreSQL usando el usuario `postgres`
3. Crea una base llamada:

```text
eden_loteamiento_db
```

---

### Opción B - usando `psql` en Windows o Linux

Entrar al cliente:

```bash
psql -U postgres
```

Si en Linux necesitas entrar como usuario del sistema PostgreSQL:

```bash
sudo -u postgres psql
```

Crear base:

```sql
CREATE DATABASE eden_loteamiento_db;
```

Crear usuario:

```sql
CREATE USER eden_user WITH PASSWORD 'cambiar_esta_password';
```

Dar privilegios:

```sql
GRANT ALL PRIVILEGES ON DATABASE eden_loteamiento_db TO eden_user;
```

Salir:

```sql
\q
```

---

## 11. Configurar archivo `.env`

En la raíz del proyecto debe existir un archivo `.env`.

Ejemplo base:

```env
SECRET_KEY=django-insecure-cambiar-esto
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=eden_loteamiento_db
DB_USER=eden_user
DB_PASSWORD=cambiar_esta_password
DB_HOST=127.0.0.1
DB_PORT=5432

CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

SITE_URL=http://127.0.0.1:8000
WHATSAPP_NUMBER=595000000000
```

### Importante

No subir `.env` al repositorio.

---

## 12. Configuración esperada de Django

La estructura actual del proyecto está pensada para trabajar con settings separados:

```text
config/settings/base.py
config/settings/local.py
config/settings/production.py
```

El criterio es:

- `base.py`: configuración compartida
- `local.py`: entorno de desarrollo
- `production.py`: entorno productivo

---

## 13. Aplicar migraciones

Con PostgreSQL creado, `.env` configurado y entorno virtual activo, ejecuta:

```bash
python manage.py migrate
```

Esto crea las tablas base de Django.

---

## 14. Crear superusuario

Para acceder al panel admin:

```bash
python manage.py createsuperuser
```

Completa:

- nombre de usuario
- correo
- contraseña

---

## 15. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrir en navegador:

```text
http://127.0.0.1:8000/
```

Panel admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 16. Flujo de puesta en marcha rápida

### Windows o Linux

1. instalar Python
2. instalar Git
3. instalar PostgreSQL
4. verificar que `psql` funcione
5. clonar el repositorio
6. crear y activar `.venv`
7. instalar dependencias
8. crear archivo `.env`
9. crear la base de datos PostgreSQL
10. correr migraciones
11. crear superusuario
12. ejecutar `runserver`

---

## 17. Flujo de trabajo diario

Cada vez que vuelvas a trabajar en el proyecto:

### Windows

```powershell
cd ruta\del\proyecto
.venv\Scripts\Activate.ps1
python manage.py runserver
```

### Linux

```bash
cd ruta/del/proyecto
source .venv/bin/activate
python manage.py runserver
```

---

## 18. Problemas comunes

### 18.1 `python` no se reconoce

En Windows:

```powershell
py --version
```

Si `py` funciona, puedes usar `py` en lugar de `python`.

---

### 18.2 `psql` no se reconoce

En Windows, revisa que PostgreSQL esté instalado y que esta ruta esté en el `PATH`:

```text
C:\Program Files\PostgreSQL\17\bin
```

Luego reinicia la terminal.

---

### 18.3 Error al activar `.venv` en PowerShell

Ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego activa otra vez:

```powershell
.venv\Scripts\Activate.ps1
```

---

### 18.4 Error de conexión a PostgreSQL

Revisa:

- que PostgreSQL esté iniciado
- que la base exista
- que el usuario y contraseña coincidan con `.env`
- que `DB_HOST=127.0.0.1`
- que `DB_PORT=5432`

---

### 18.5 `ModuleNotFoundError`

Normalmente significa que faltan dependencias dentro del entorno virtual activo.

Ejecuta:

```bash
pip install -r requirements/base.txt
```

---

## 19. Comandos útiles

### Activar entorno virtual

#### Windows

```powershell
.venv\Scripts\Activate.ps1
```

#### Linux

```bash
source .venv/bin/activate
```

### Desactivar entorno virtual

```bash
deactivate
```

### Levantar servidor

```bash
python manage.py runserver
```

### Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario

```bash
python manage.py createsuperuser
```

### Ver versión de Django

```bash
python -m django --version
```

### Ver versión de PostgreSQL client

```bash
psql --version
```

---

## 20. Qué no debe subirse al repositorio

El `.gitignore` debe contemplar al menos esto:

```gitignore
.venv/
__pycache__/
*.pyc
.env
db.sqlite3
media/
staticfiles/
.vscode/
.idea/
.DS_Store
Thumbs.db
```

---

## 21. Estado actual del proyecto

Esta base deja preparado el proyecto para avanzar con:

- configuración completa de settings
- registro de apps en Django
- conexión definitiva a PostgreSQL
- panel admin
- modelos de loteamiento, lotes y leads
- templates reales
- landing page
- SEO y analítica

---

## 22. Fuentes oficiales

- Python Downloads: https://www.python.org/downloads/
- Python `venv`: https://docs.python.org/3/library/venv.html
- Django installation: https://docs.djangoproject.com/en/6.0/topics/install/
- Django 5.2 release notes: https://docs.djangoproject.com/en/6.0/releases/5.2/
- PostgreSQL Windows installer: https://www.postgresql.org/download/windows/
- PostgreSQL `psql`: https://www.postgresql.org/docs/current/app-psql.html
- GitHub - adding locally hosted code: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
- GitHub - uploading a project: https://docs.github.com/en/get-started/start-your-journey/uploading-a-project-to-github

---

## 23. Nota final

Si al clonar el repositorio algo no corre correctamente, primero valida en este orden:

1. Python instalado y accesible
2. `.venv` creado y activado
3. dependencias instaladas
4. PostgreSQL instalado
5. `psql` funcionando
6. base de datos creada
7. `.env` configurado
8. migraciones aplicadas

Con esa secuencia normalmente el entorno queda operativo sin problemas.
