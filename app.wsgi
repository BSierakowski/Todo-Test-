import sys, os, bottle

sys.path = ['/var/www/app/'] + sys.path
os.chdir(os.path.dirname(__file__))

import app # loads app

application = bottle.default_app()
