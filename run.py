#!/usr/bin/env python3

from routes import app
from System import System

if __name__ == '__main__':
    app.config['SYSTEM'] = System()
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True, port=4000)