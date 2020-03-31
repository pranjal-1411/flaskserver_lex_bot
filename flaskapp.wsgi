import sys
sys.path.insert(0, '/var/www/html/flaskapp')
activate_this = '/home/ubuntu/flaskapp/env/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))
from flaskapp import app as application
