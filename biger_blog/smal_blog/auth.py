from flask import Blueprint,render_template,redirect,url_for
from biger_blog.forms import AdminForm

auth_app = Blueprint("auth",__name__)

@auth_app.route("/login",methods=["GET","POST"])
def login():
    admin_form = AdminForm()
    if admin_form.validate_on_submit():
        username = admin_form.username.data
        password = admin_form.password.data
        print(username)
        print(password)
        return redirect(url_for("blog.index"))
    return render_template("auth/login.html",admin_form=admin_form)
