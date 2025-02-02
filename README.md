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