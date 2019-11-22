#!/usr/bin/env python3

from routes import app
from System import System
from helper.get_skills import get_skills
from helper.get_currencies import get_currencies
from helper.init_packages import init_packages

if __name__ == '__main__':
    app.config['SYSTEM'] = System()
    app.config['SKILLS'] = get_skills()
    app.config['CURRENCIES'] = get_currencies()
    app.config['SYSTEM'].set_packages(init_packages())
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True, port=5000)

