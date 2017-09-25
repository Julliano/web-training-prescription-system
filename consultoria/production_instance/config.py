from os import urandom

RUN_DEBUG = True
RUN_USE_RELOADER = False
RUN_HOST = '0.0.0.0'
RUN_PORT = 80
CSRF_ENABLED = False
SQLALCHEMY_ECHO = False
DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = '123'
DB_NAME = 'consultoriaProd'
SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s?client_encoding=utf8' % (DB_USER,DB_PASS,DB_HOST,DB_NAME)
SECRET_KEY = '@Consultor14'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_TRACKABLE = True
SESSION_PROTECTION = "strong"
SEND_FILE_MAX_AGE_DEFAULT = 0
