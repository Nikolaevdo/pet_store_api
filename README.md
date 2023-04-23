# Pet Store API

This is a RESTful API for managing animals in a pet store. The API provides CRD (Create, Read, and Delete) operations for animals on the database.


The API provides the following endpoints:
GET /pets

Returns a list of all animals in the database.

POST /pets

Creates a new animal in the database based on the given data and returns its current state in the database.


DELETE /pets

Removes animals with the given IDs from the database.

## Minimum requirement 

 _Python 3.10_

## Installing
_To package install use: ```make install_dep```_

 _To build use: ```make build```_

## App start 
 _To app run use: ```make run```_ 



### Dependencies: 
 anyio              3.6.2  High level compatibility layer for multiple asynchronous event loop implementations

click              8.1.3  Composable command line interface toolkit

fastapi            0.95.1 FastAPI framework, high performance, easy to learn, fast to code, ready for production

fastapi-cli        0.0.1  

flake8             6.0.0  the modular source code checker: pep8 pyflakes and co


h11                0.14.0 A pure-Python, bring-your-own-I/O implementation of HTTP/1.1

idna               3.4    Internationalized Domain Names in Applications (IDNA)

importlib-metadata 1.7.0  Read metadata from Python packages

mccabe             0.7.0  McCabe checker, plugin for flake8

pycodestyle        2.10.0 Python style guide checker

pydantic           1.10.7 Data validation and settings management using python type hints

pyflakes           3.0.1  passive checker of Python programs

sniffio            1.3.0  Sniff out which async library your code is running under

starlette          0.26.1 The little ASGI library that shines.

typing-extensions  4.5.0  Backported and Experimental Type Hints for Python 3.7+

uvicorn            0.21.1 The lightning-fast ASGI server.

zipp               3.15.0 Backport of pathlib-compatible object wrapper for zip files