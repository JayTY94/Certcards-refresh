Django Project
A container for the entire web application, including settings, URLs, and WSGI/ASGI entry point. One project can hold multiple Django apps.

Django App
A self-contained feature module (e.g., blog, accounts, billing). Apps are reusable and plugged into a project.

MTV Pattern
Django’s architecture similar to MVC: Model (database/ORM), Template (HTML output), View (Python function/class connecting input to response).

Model
Python class that defines a database table via Django’s ORM. Fields map to columns; instances map to rows.

ORM (Object-Relational Mapper)
Layer that lets you query/update the database using Python methods instead of SQL. (Todo.objects.filter(done=False)).

Migration
Django’s system for version-controlling database schema changes. Generated with makemigrations, applied with migrate.

Admin Site
Built-in, auto-generated UI for CRUD operations on models. Accessed at /admin/.

Static Files
CSS, JavaScript, and images that are part of the application code. Collected via collectstatic for serving in production.

Media Files
User-uploaded content (e.g., profile pics, documents). Should be stored in durable storage like Azure Blob Storage.

Template
HTML file using Django’s template language ({% for %}, {{ variable }}) to render dynamic data.

View
Python function or class that handles an HTTP request and returns a response. Often pulls from models and renders templates.

URLconf
Mapping of URL patterns to views (urls.py).

Middleware
Functions that process requests/responses globally (e.g., auth, CSRF protection).

Form / ModelForm
Classes for validating, rendering, and handling user input, tied to Django’s security (CSRF, validation).

CSRF Protection
Security mechanism preventing cross-site request forgery. Django includes it by default via middleware and template tags.

WSGI / ASGI
Python web server interfaces. WSGI = synchronous (classic web apps). ASGI = async (for websockets, long polling).

Gunicorn
A common Python WSGI HTTP server used to serve Django apps in production. Azure App Service uses it for Django deployments.

Environment Variables
Configuration values set outside code (e.g., DJANGO_SECRET_KEY, DEBUG, ALLOWED_HOSTS). Essential for Azure App Service deployments.

ALLOWED_HOSTS
A Django setting defining which hostnames are valid for requests. Must include your *.azurewebsites.net and custom domains.

CSRF_TRUSTED_ORIGINS
Django setting for trusted domains when validating CSRF tokens, often needed for HTTPS custom domains.

collectstatic
Command that gathers all static files into one folder (STATIC_ROOT) for production serving.

App Service (Azure)
PaaS hosting option where Django runs inside a managed Linux container. You deploy code, set environment variables, and Azure handles the OS.

Application Insights
Azure service for monitoring logs, exceptions, and performance of your Django app.

Scaling
App Service can scale Django apps horizontally (more instances) or vertically (bigger instance sizes).

Startup Command
Command App Service runs to start the app (e.g., gunicorn mysite.wsgi:application).

dj-database-url
Helper library that parses a DATABASE_URL environment variable into Django’s DATABASES setting. Handy for Azure PostgreSQL/MySQL.

django-storages + azure-storage-blob
Library combo for storing Django’s media/static files in Azure Blob Storage instead of local ephemeral disk.




Deployment Slot
An Azure App Service feature that lets you run multiple versions (e.g., staging and production) side by side. You can test updates in a staging slot, then swap into production with minimal downtime.

Zip Deploy
Deployment method where you upload a zipped copy of your Django project to App Service. Azure unpacks and runs it. Simple, but limited compared to CI/CD.

Run Command / Startup Command
Custom command specified in Azure App Service to start your app (e.g., gunicorn mysite.wsgi:application). Overrides defaults if needed.

Container (App Service for Linux)
Your Django app runs inside a managed Linux container. You don’t control the OS directly; you just provide your app, dependencies, and startup instructions.

Oryx Build System
Azure’s automatic build system for Python/Node/etc. Detects your app type, installs dependencies (pip install -r requirements.txt), and prepares it for App Service.

Kudu (Deployment Engine)
The deployment backend for App Service. Handles zip deployments, build processes, and gives you a debug console (https://<appname>.scm.azurewebsites.net/).

Requirements File (requirements.txt)
Lists Python package dependencies for deployment. Azure’s build process installs everything listed here.

Collectstatic Step
Part of Django deployment where python manage.py collectstatic --noinput gathers all static files into STATIC_ROOT so they can be served in production.

Ephemeral Storage
The disk space in App Service containers is temporary. Files written there (like uploads) don’t persist across restarts. That’s why static and media files should go to durable storage like Azure Blob Storage.

Azure Blob Storage (Static/Media)
Cloud storage for persistent files. Integrated into Django via django-storages so static and uploaded media files survive restarts and scale across multiple instances.

Environment Variables (App Settings)
Stored in Azure App Service → Configuration. Used to hold sensitive values like DJANGO_SECRET_KEY, DB connection strings, and production flags.

App Service Logs
Application logs (stdout/stderr) streamed directly from Django. Viewable via Azure Portal, az webapp log tail, or Application Insights.

Application Insights
Azure monitoring service that can automatically capture Django logs, request traces, exceptions, and performance metrics.

Managed Identity
App Service can have a system-assigned identity that authenticates to other Azure resources (e.g., Blob Storage, Key Vault) without storing secrets in code.

Key Vault Integration
Azure Key Vault can store secrets (like DJANGO_SECRET_KEY, DB passwords) securely. App Service integrates directly to inject these into environment variables.

Continuous Deployment (CI/CD)
Automated deployments from GitHub Actions, Azure DevOps, or other pipelines. Handles build, test, collectstatic, migrations, and push to App Service.

Migrations in Deployment
Running python manage.py migrate --noinput during deployment to apply DB schema changes. Best done in a controlled pipeline step, not at app startup.

Scaling (Horizontal/Vertical)
App Service can scale out (multiple containers running your Django app) or scale up (larger instance size). Important for load and availability.

App Service Plan
The compute resource that hosts your App Service apps. Determines pricing, scaling, and features.

Custom Domain Binding
Mapping your Django app to a custom domain (www.example.com) in App Service. Requires setting DNS records and possibly TLS certificates.

Let’s Encrypt / App Service Managed Certificate
TLS/SSL options for securing your custom domain. App Service can generate free managed certificates for HTTPS.

Deployment Center
Azure Portal feature to configure CI/CD sources like GitHub or Azure DevOps for automatic deployments.

az webapp up
Azure CLI shortcut command to quickly deploy a Python/Django app to a new App Service, often used for testing or prototyping.