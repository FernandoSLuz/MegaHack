#!/usr/bin/python
from app import Flask
from app import create_app

app = create_app(True)

if __name__ == '__main__':
    Flask.run(app, debug=True)