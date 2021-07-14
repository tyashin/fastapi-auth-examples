* cd backend-MySQL
* pipenv shell
* pipenv install
* create MySQL database
* rename file "app/core/sample.env" to "app/core/.env"
* modify MySQL connection string in .env file.
* uvicorn app.main:app --reload
* go to http://127.0.0.1:8000/docs

![Screenshot](https://raw.githubusercontent.com/tyashin/fastapi-quasar-auth-examples/master/img/backend-sqlite-api.png)
