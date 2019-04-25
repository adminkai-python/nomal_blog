from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

db = SQLAlchemy()
moment = Moment()

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

bootstrap = Bootstrap()
ckeditor = CKEditor()



