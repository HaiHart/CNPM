# Restuarant project
## Install dependencies for backend
```
cd backend
pip install pipenv
pipenv shell
pipenv sync
```

Go to src/settings.py and change the database, user and password

## Run backend
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Project setup
```
cd ..
npm install
```
npm install --save mdbvue 
### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
