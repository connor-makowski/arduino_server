# API Server
A simple flask server instance for restful web access to blink

## Installation
Make sure you have Python 3.6+ installed on your system. You can download it [here](https://www.python.org/downloads/).

### Set up a Virtual Environment
Set up a virtual environment:
  If you are using `virtualenv`, you can create a new environment based on Python 3.6.x:
  ```sh
  virtualenv -p python3 venv
  ```
  Where `venv` is the directory name to place the new virtual environment.

  Then, you must activate it:
  ```sh
  source venv/bin/activate
  ```

  In Windows this can be sourced by typing:
  ```sh
  venv\Scripts\activate
  ```

### Install requirements
While in (venv), install all requirements:
```
pip install -r requirements.txt
```

## Running the Server
Run the server
```
python run.py
```

## Using the Server
Post to the server (localhost:6001):
  ```
  curl -i 192.168.1.102:6001/red
  ```
  ```
  curl -i 192.168.1.102:6001/green
  ```
