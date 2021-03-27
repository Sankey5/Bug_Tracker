from flask import Flask

app = Flask(__name__)

app.config.from_object("resources.config.Config")   # Import app config file

# Import endpoints
from endpoints import bugCRUD

# Add endpoints
app.add_url_rule('/bugs', view_func=bugCRUD.createBug, methods=['POST'])

if __name__ == '__main__':
    app.run()