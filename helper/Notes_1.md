# Inventory Management App

### Technologies used
- React: Dynamic, Fast and Coustomizable frontend
- Django: Robust Backend

### Project Setup
- Setting python backend
- Creating react TS frontend
- User authentications
- Page navigation 
- Backend communication

### Backend SetUp
- creating virtual environment
    - installing virtual env
    ```shell
    python -m pip install virtualenv
    ```
    - creating a virtual env 
    ```shell
    python -n venv env
    ```

- installing packages 
    - installing django 
    ```shell
    python -m pip install django
    ``` 

    - install django rest framework for web apis 
    ```shell
    pip install djangorestframework django-cors-headers django-environ djangorestframework-simplejwt
    pip intall python-dotenv
    pip freeze > requirements.txt   # save dependencies
    ```

- creating django project and app using django-admin command
    ```shell
    django-admin startproject config . # start a project name config folder (.) else it will create another folder config under config folder 

    
    django-admin startapp users     # create app as resuable components
    python manage.py startapp users # django-admin and python manage.py both are same commands
    python manage.py startapp inventory
    python manage.py startapp dashboard
    python manage.py startapp settings
    ```
   
    
- changing settings
- including urls 
- migrating our databases

### Frontend setup
- installing nodejs using nvm with pnpm 
```shell
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.13.1".
nvm current # Should print "v22.13.1".

# Download and install pnpm:
corepack enable pnpm

# Verify pnpm version:
pnpm -v
```


## **📌 Frontend (React + TypeScript)**
```
frontend/
│── package.json
│── tsconfig.json
│── .env                # API keys, backend URL
│── src/
│   ├── api/            # API requests (Axios)
│   │   ├── auth.ts     # Login, OTP verification
│   │   ├── inventory.ts
│   │   ├── dashboard.ts
│   ├── components/     # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   ├── pages/          # Page components
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Inventory.tsx
│   │   ├── Settings.tsx
│   ├── contexts/       # React Context for state management
│   │   ├── AuthContext.tsx
│   │   ├── RoleContext.tsx
│   ├── hooks/          # Custom hooks (useAuth, useInventory, etc.)
│   ├── utils/          # Helper functions
│   ├── styles/         # Tailwind or CSS Modules
│   ├── App.tsx
│   ├── main.tsx
│── public/
│── dist/ (for production build)
```

--- 
 
### **Project Folder Structure for Inventory Management App**  
---

## **📌 Backend (Django + Django REST Framework)**
```
backend/
│── __init__.py
│── manage.py
│── .env                # Environment variables (e.g., secret keys, DB credentials)
│── requirements.txt    # Python dependencies
│── config/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│── apps/               # All Django apps
│   ├── users/          # Authentication & role management
│   │   ├── models.py   # User model with roles
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   ├── otp.py      # OTP logic (email & mobile)
│   ├── inventory/      # Scrap management
│   │   ├── models.py   # Scrap, Purchase, Sales, Recycle models
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py  # Filtering logic
│   ├── dashboard/      # Role-based dashboards
│   │   ├── views.py
│   │   ├── urls.py
│   ├── settings/       # Settings for all roles
│   │   ├── views.py
│   │   ├── urls.py
│── static/             # Static files (if needed)
│── media/              # Uploaded files
│── tests/              # Unit tests
│── db.sqlite3 (or PostgreSQL)
```
---

## **📌 API Design (Django REST Framework)**
### **Authentication & OTP**
| Endpoint             | Method | Description |
|----------------------|--------|-------------|
| `/api/auth/register/` | POST   | Register user (email/phone) |
| `/api/auth/login/`    | POST   | Login via email/phone OTP |
| `/api/auth/verify-otp/` | POST | Verify OTP & issue JWT |
| `/api/auth/logout/`   | POST   | Logout user |

### **Inventory Management**
| Endpoint            | Method | Description |
|----------------------|--------|-------------|
| `/api/inventory/`    | GET    | Get all scrap items |
| `/api/inventory/`    | POST   | Add new scrap entry |
| `/api/inventory/{id}/` | PUT  | Update scrap details |
| `/api/inventory/{id}/` | DELETE | Delete scrap item |

### **Dashboard**
| Endpoint            | Method | Description |
|----------------------|--------|-------------|
| `/api/dashboard/`    | GET    | Get dashboard data (filtered by role) |

---

### **Next Steps 🚀**
1️⃣ Set up Django models and serializers for **Users & Inventory**  
2️⃣ Implement **JWT + OTP authentication**  
3️⃣ Create **React role-based dashboard**  
4️⃣ Connect React frontend with Django APIs using Axios  
5️⃣ Deploy backend (e.g., **Heroku, AWS**) and frontend (**Vercel, Netlify**)  


## **📌 Django Setup Commands (with Django REST Framework)**

--- 

### **1️⃣ Create a Virtual Environment & Install Dependencies**
```sh
# Create project folder and navigate into it
mkdir backend && cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install Django, DRF & Other Dependencies
pip install django djangorestframework django-cors-headers django-environ djangorestframework-simplejwt

# Save dependencies
pip freeze > requirements.txt
```

---

### **2️⃣ Create Django Project & Apps**
```sh
# Start Django project
django-admin startproject config .

# Create core apps
python manage.py startapp users
python manage.py startapp inventory
python manage.py startapp dashboard
python manage.py startapp settings
```

---

### **3️⃣ Configure Django Settings (`config/settings.py`)**
Update installed apps:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Third-party apps
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",

    # Your apps
    "apps.users",   # apps/users
    "apps.inventory",   # apps/inventory
    "apps.dashboard",   # apps/dashboard
    "apps.roles_settings",  # apps/roles_settings
]
```

Add middleware:
```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Enable CORS
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

Enable CORS:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # React frontend
    "http://127.0.0.1:5173",
]
```

Set up REST Framework:
```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

---

Since `settings.py` is inside the `config` folder, Django needs to know where to find it. 

---
#### Solutions list: 

### **1️⃣ Set `DJANGO_SETTINGS_MODULE` Environment Variable**
Run this in your terminal before running Django commands:
```sh
export DJANGO_SETTINGS_MODULE=config.settings  # For Linux/macOS
set DJANGO_SETTINGS_MODULE=config.settings    # For Windows (Command Prompt)
$env:DJANGO_SETTINGS_MODULE="config.settings" # For Windows (PowerShell)
```

Or add it permanently to your virtual environment's `activate` script.

---

### **2️⃣ Run Commands with Explicit Settings**
If you are running a Django command, specify the settings module explicitly:
```sh
python manage.py runserver --settings=config.settings
```

---

### **3️⃣ Update `wsgi.py` & `asgi.py`**
Inside `config/wsgi.py` and `config/asgi.py`, update:
```python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
```

---

### **4️⃣ Check `__init__.py` in `config/`**
Ensure there is an empty `__init__.py` file inside `config/` to make it a package.

---

After this, try running:
```sh
python manage.py runserver
```


### **4️⃣ Apply Migrations & Create Superuser**
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Enter email/password
```

---

### **5️⃣ Run Development Server**
```sh
python manage.py runserver
```

---

### **6️⃣ Setup API URLs (`config/urls.py`)**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),  
    path("api/inventory/", include("inventory.urls")),
    path("api/dashboard/", include("dashboard.urls")),
]
```

---

### **7️⃣ Setup Authentication API (`users/views.py`)**
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
def login(request):
    phone = request.data.get("phone")
    if not phone:
        return Response({"error": "Phone number required"}, status=400)

    # Dummy OTP logic (implement actual OTP system)
    otp = "123456"  
    return Response({"message": "OTP sent", "otp": otp})

@api_view(["POST"])
def verify_otp(request):
    phone = request.data.get("phone")
    otp = request.data.get("otp")

    if otp == "123456":
        user = {"id": 1, "role": "admin"}  # Dummy user
        token = RefreshToken.for_user(user)
        return Response({"token": str(token.access_token)})
    
    return Response({"error": "Invalid OTP"}, status=400)
```

---

### **8️⃣ Test APIs with Django's Built-in Server**
```sh
curl -X POST http://127.0.0.1:8000/api/users/login/ -H "Content-Type: application/json" -d '{"phone": "9876543210"}'
```

---
