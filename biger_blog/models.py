from biger_blog.extends import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password_hash = db.Column(db.String(100),nullable=False)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)




class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    body = db.Column(db.Text,nullable=False)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))

    category = db.relationship("Category",back_populates="posts")
    comments = db.relationship("Comment",back_populates="post")




class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    category_name = db.Column(db.String(100),nullable=False)

    posts = db.relationship("Post",back_populates="category")



class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    comment = db.Column(db.Text,nullable=False)
    username = db.Column(db.String(100),nullable=True,default="匿名用户")
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"))

    post = db.relationship("Post",back_populates="comments")
    replies = db.relationship("Reply",back_populates="comment")




class Reply(db.Model):
    __tablename__ = "reply"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    reply = db.Column(db.Text,nullable=False)
    username = db.Column(db.String(100),nullable=True,default="匿名用户")
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    comment_id = db.Column(db.Integer,db.ForeignKey("comment.id"))

    comment = db.relationship("Comment",back_populates="replies")










