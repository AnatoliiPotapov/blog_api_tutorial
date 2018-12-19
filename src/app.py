#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint

# flask-swagger-ui for api documentation
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
  API_URL,
  config={  # Swagger UI config overrides
    'app_name': "Test application"
  }
)

def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(swaggerui_blueprint, url_prefix='/api/docs')
  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')


  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'LMS by Potapov Anatoly'

  return app

