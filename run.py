#!/usr/bin/env python3

from routes import app
from System import System
from helper.get_skills import get_skills
from helper.get_currencies import get_currencies

if __name__ == '__main__':
    app.config['SYSTEM'] = System()
    app.config['SKILLS'] = get_skills()
    app.config['CURRENCIES'] = get_currencies()
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True, port=5000)

