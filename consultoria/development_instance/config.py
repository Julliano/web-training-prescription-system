RUN_DEBUG = True
RUN_USE_RELOADER = True
RUN_HOST = '0.0.0.0'
RUN_PORT = 5000
CSRF_ENABLED = False
SQLALCHEMY_ECHO = True
DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = '123'
DB_NAME = 'consultoria'
SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s?client_encoding=utf8' % (DB_USER,DB_PASS,DB_HOST,DB_NAME)
SECRET_KEY = '@Consultor14'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_TRACKABLE = True
SESSION_PROTECTION = "strong"
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = "jullianoVolpato@gmail.com"
MAIL_PASSWORD = "eusoroxConsultoria"
MAIL_DEFAULT_SENDER = "Julliano Volpato - Consultoria"
SEND_FILE_MAX_AGE_DEFAULT = 0