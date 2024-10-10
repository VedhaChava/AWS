import sys
import os

# Path to the application and virtual environment
app_path = '/var/www/html/myapp'
venv_path = '/var/www/html/myapp/myvenv'

# Activate the virtual environment
activate_this = os.path.join(venv_path, 'bin/activate_this.py')
# Check if activate_this.py exists and run it
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), dict(__file__=activate_this))
else:
    print("activate_this.py not found, skipping activation.")

# Add the application to the system path
sys.path.insert(0, app_path)

from app import app as application  # Import your Flask app
