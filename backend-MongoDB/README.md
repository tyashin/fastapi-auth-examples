- cd backend-Postgres
- pipenv shell
- pipenv install
- create MongoDB database
- rename file "app/core/sample.env" to "app/core/.env"
- modify MongoDB connection string and database name in .env file.
- uvicorn app.main:app --reload
- go to http://127.0.0.1:8000/docs

![Screenshot](https://raw.githubusercontent.com/tyashin/fastapi-quasar-auth-examples/master/img/backend-sqlite-api.png)
