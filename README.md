# CFTask

A simple ETL pipeline that takes csvs, transforms, pushes to db, and exposes with rest API.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

* Docker installation

### Executing program

* docker-compose up
* `curl -v http://127.0.0.1:5000/read/first-chunk` to use hit the API
```

### Testing
Execute the following:
* `docker exec -it <cftask-etl/cftask-api> bash`
* `cd test`
* `pytest`
