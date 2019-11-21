# fwd-be
REST de TODO's

Comandos para deploy en Heroku

Instalar heroku CLI y añadir al PATH
Asociar repositorio en github con proyecto de heroku

$ heroku login
$ heroku run python manage.py migrate -a APP-NAME

Deshabilita staticfiles en caso de no ser necesarias
$ heroku config:set DISABLE_COLLECTSTATIC=1 -a APP-NAME

Consultar el log en caso de errores
$ heroku logs --tail -a APP-NAME