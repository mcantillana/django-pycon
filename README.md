## Como ejecutar el proyecto

### Crear fichero de entorno

crear un fichero .env en la raiz del proyecto con la siguiente info
~~~
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=pycon-static
AWS_S3_ENDPOINT_URL=s3.us-west-000.backblazeb2.com

ALLOWED_HOSTS=127.0.0.1,localhost
DEBUG=True
~~~

Para utilizar los estaticos en s3 o blazer debes colocar la información del bucket y luego ejecutar:

~~~
docker-compose run web python manage.py collectstatic
~~~

finalmente para dejar corriendo el proyecto puedes utilizar 
~~~
docker-compose up -d
~~~

