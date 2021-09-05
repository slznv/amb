# (Work In Progress) Graphs

This repo contains a web service that provides an API for clients to run algorithms and
perform updates on the graphs. The graphs it will deal with are normal, directed graphs with a
set of nodes and edges. 

The web service supports basic CRUD operations on nodes and edges(not implemented).


## Run service locally
### as python app
```bash
make install
make run
```

### as Docker container
```bash
docker build -t graphs .
docker run -p 8000:8000 graphs
```

After the app is up and running, web-service will be available on 
`localhost:8000`

## Development
### Install dependencies from Pipfile
```bash
make install
```
### Run tests:
#### Linting
```bash
make linting
```
#### Unit Tests
```bash
make unit
```
