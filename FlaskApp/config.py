# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# image directory
# UPLOAD_FOLDER = BASE_DIR+'UPLOAD_FOLDER'

# # Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# DATABASE_CONNECT_OPTIONS = {}

#MongoDb Setting Alchemy
# MONGOALCHEMY_DATABASE = 'flaskapp'
#localhost
#MONGOALCHEMY_CONNECTION_STRING = 'mongodb://localhost:27017/app'
#production
# MONGOALCHEMY_CONNECTION_STRING = 'mongodb://swarup260:14919755#WAS@ds133961.mlab.com:33961/flaskapp'

# PyMongo
# MONGO_URI = 'mongodb://localhost:27017/app'



# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "b200aa754271c7d3db81baf6e69d9f7823b64669"

# Secret key for signing cookies
SECRET_KEY = "b200aa754271c7d3db81baf6e69d9f7823b64669"
