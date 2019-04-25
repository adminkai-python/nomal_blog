from flask import Blueprint,render_template,request,redirect,url_for,session
from biger_blog.models import *
from biger_blog.forms import CommentForm

blog_app = Blueprint("blog",__name__)

@blog_app.route("/")
def index():
    page = request.args.get("page",default=1,type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page,per_page=7)
    posts = pagination.items
    return render_template("blog/index.html",posts=posts,pagination=pagination)

@blog_app.route("/post/<post_id>", methods=["GET","POST"])
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        print("csrf验证已经关闭")
        username = comment_form.username.data
        comment = comment_form.comment.data
        comment_sql = Comment(username=username,comment=comment,post_id=post_id)
        db.session.add(comment_sql)
        db.session.commit()
        return redirect(url_for("blog.post",post_id=post_id))
    if request.method == "POST" and comment_form.validate_on_submit() == False:
        print("错误原因为:{}".format(comment_form.errors))
        print("前端生成的csrf字段为：{}".format(comment_form.csrf_token))
        print("session的csrf令牌值为：{}".format(session["csrf_token"]))
    return render_template("blog/post.html",post=post,comment_form=comment_form)


@blog_app.route("/category")
def category():
    return render_template("blog/category.html")