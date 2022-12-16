# CFTask

A simple ETL pipeline that takes csvs, transforms, pushes to db, and exposes with rest API.

## Description
* A network of 3 docker containers - one running postgres, one that runs the ETL code, and one that runs the Flask API. 
* The ETL container waits until the psql server is ready to accept connections, and the API containter waits until the ETL container has finished running. * The ETL and API containers have mounted volumes for development

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
Test coverage in the API code is not 100% - I prioritized testing ETL code as I regard data quality as more fundamental than API function in this case.  (i.e., no data is better than wrong data). However, given more time, I would improve this.
### Logging
At the moment logs are persistent as they are present in the container-specific directory which is mounted as a volume. However this may not be best practice, and I have not had time to think about improving this.

