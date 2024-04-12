PROJECT CREATE WITH DJANGO REST FRAMEWORK AND MYSQL DATABASE

create directory .venv in root of our project

install interpreter poetry:
    for install curl -sSL https://install.python-poetry.org | python3 -

    install djangorestframework and mysqlclient:
        use command poetry add djangorestframework mysqlclient

for docker use command:
    docker compose build (Dockerfile)
    docker compose up
                                or
            docker compose up --build

    poetr[pyproject.toml](pyproject.toml)y export --output requirements.txt --without-hashes
    

for docker shell:
    docker compose run --rm app sh

        make migrations for all you apps:
             ./manage.py migrate
             ./manage.py makemigrations
            exit
     ./manage.py collectstatic -- to collect static file


after install any library use command:
    poetry export --output requirements.txt --without-hashes

create react ts in directory frontend
    npx create-react-app . 

build project in directory frontend
    npm run build

npm run watch -- command that monitors changes in files with extension js and css

Use the API endpoints for Postman (including example requests and responses):

    HTTP method 'get' localhost/api/books  -- get all books (200)
    HTTP method 'getById' localhost/api/books/:id  -- get book by id(200)
    HTTP method 'post' localhost/api/books  -- post book(201)
    HTTP method 'put' localhost/api/books/:id  -- full update by id(200)
    HTTP method 'patch' localhost/api/books/:id  -- partial update by id(200)
    HTTP method 'delete' localhost/api/books/:id  -- destroy book by id(204)

for open swagger documentation follow link http://localhost/api/doc

for test your endpoints:
    restart docker,
    from docker shell:
        docker compose run --rm app sh 
            command:
                ./manage.py test .

    we have to create new connection to new db with port number that we put in file docker-compose.yml db->ports , for this we are using USER:root and PASSWORD: from .env MYSQL_ROOT_PASSWORD
        in console from db we have to run command:
            grant all privileges on test_mydb.* to 'user'@'%';
            flush privileges;


    
    



  