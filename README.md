# CFTask

A simple ETL pipeline that takes csvs, transforms, pushes to db, and exposes with rest API.

## Description
A network of 3 docker containers - one running postgres, one that runs the ETL code, and one that runs the Flask API.

### ETL
The ETL container simply takes the csv files, does some simple joins/aggregation, and loads to the postgres db. 

### API
The API container spins up a minimal flask-restful API with one endpoint to expose the data as outlined.

### DB
Just runs the postgres docker container and sets some psql parameters

## Getting Started

### Dependencies

* Docker installation

### Executing program

* docker-compose up
* `curl -v http://127.0.0.1:5000/read/first-chunk` to use hit the API

### Testing
Execute the following to run api or etl tests in their respective containers:
```
docker exec -it <cftask-etl/cftask-api> bash
cd test
pytest
```

## Improvements
For the sake of time prioritization, there are certainly areas in this codebase that could still be improved
### Testing
Test coverage in the API code is not 100% - in general I would prioritize testing ETL code as I regard data quality as more fundamental than API function in this case. However, given more time, I would improve this.
### Container Orchestration
I am currently using `sleep` to ensure the API is ready after the ETL has run, which is not optimal. Ideally, I would use a bash script to wait for the 0 exit code then spin up the api.

