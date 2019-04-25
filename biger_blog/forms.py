from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length
from flask_ckeditor import CKEditorField

class CommentForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired(message="必填数据"),Length(1,100,message="用户名太长")])
    comment = TextAreaField("内容",validators=[DataRequired(message="必填数据"),Length(1,2000,message="内容需要在2000字以内")])
    submit = SubmitField(render_kw={"value":"提交"})

class AdminForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired(message="必填数据"),Length(1,100,message="用户名太长")])
    password = PasswordField("密码",validators=[DataRequired(message="必填数据"),Length(6,20,message="密码长度在6到20位")])
    submit = SubmitField("登录")