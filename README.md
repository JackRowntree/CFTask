# CFTask

A simple ETL pipeline that takes csvs, transforms, pushes to db, and exposes with rest API.

## Description
A network of 3 docker containers - one running postgres, one that runs the ETL code, and one that runs the Flask API.

### ETL
The ETL container simply takes the csv files, does some simple joins/aggregation, and loads to the postgres db.

### API
The API container spins up a minimal flask-restful API with one endpoint to expose the data as outlined.

## Getting Started

### Dependencies

* Docker installation

### Executing program

* docker-compose up
* `curl -v http://127.0.0.1:5000/read/first-chunk` to use hit the API

### Testing
Execute the following:
```
docker exec -it <cftask-etl/cftask-api> bash
cd test
pytest
```
