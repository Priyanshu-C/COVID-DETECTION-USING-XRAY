import os
from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

###########################
#### BLUEPRINT CONFIGS #######
#########################

# Import these at the top if you want
# We've imported them here for easy reference
from CovidTestXray.MainPage.views import core

# Register the apps
app.register_blueprint(core)

