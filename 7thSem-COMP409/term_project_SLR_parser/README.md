# SLR Parser Implementation

Implementing a SLR parser of compiler to parse and validate a grammar

## Dependency

* fastapi 0.88.0 FastAPI framework, high performance, easy to learn, fast to code, ready for production
* graphviz 0.20.1 Simple Python interface for Graphviz
* jinja2 3.1.2 A very fast and expressive template engine.
* python-multipart 0.0.5 A streaming multipart parser for Python
* uvicorn 0.20.0 The lightning-fast ASGI server.

## Running

1. Create virtual environment  
`virtualenv .venv`

2. Activate virtualenv and install requirements  
`source .venv/scripts/activate; pip install -r requirements.txt`

3. Run server (*Note: required to be in base folder*)  
`uvicorn main:app --reload`

4. Running in browser  
By default server should run in port 8000 of local host. So, go to browser and open **localhost:8000**

## Reference

SLR parser was created with reference to <https://github.com/Vipul97/slr-parser>
