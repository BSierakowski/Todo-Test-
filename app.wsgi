# Change working directory so relative paths (and template lookup) work again
import os 
os.chdir(os.path.dirname(__file__))

import bottle

#include pwd
import sys
wsgi_dir=os.path.dirname(__file__)
sys.path = [wsgi_dir] + sys.path

# ... build or import your bottle application here ...
import app

# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
