from flask import Flask
from flask_cors import CORS
from endpoints import bugCRUD   # Import endpoints
from gateway import gateway     # Import gateway startup

# Create the flask application and make it CORS compliant
app = Flask(__name__)
CORS(app)

# Create database and table if they don't exist
gateway.check_database()
gateway.check_tables()

# Change the configuration settings of the app
app.config.from_object("resources.config.Config")   # Import app config file

# Add endpoints
app.add_url_rule('/bugs', view_func=bugCRUD.createBug, methods=['POST'])

# Run it
if __name__ == '__main__':
    app.run()