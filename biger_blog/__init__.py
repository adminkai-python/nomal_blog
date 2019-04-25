from flask import Flask
from biger_blog.setting import config
import os

def create_app(config_name=os.getenv("FLASK_ENV")):
    app = Flask("biger_blog")
    app.config.from_object(config[config_name])


    register_commend(app)
    register_extends(app)
    register_smal_blog(app)
    register_context_processor(app)
    return app



from biger_blog.smal_blog.blog import blog_app
from biger_blog.smal_blog.auth import auth_app
from biger_blog.extends import db,moment,bootstrap,ckeditor
import click
from biger_blog.fakers import *



# 注册蓝本
def register_smal_blog(app):
    app.register_blueprint(blog_app)
    app.register_blueprint(auth_app)

# 注册扩展
def register_extends(app):
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    ckeditor.init_app(app)


# 注册钩子函数（模板上下文，错误处理）

def register_context_processor(app):
    @app.context_processor
    def context_category():
        category = Category.query.all()
        return {"category": category}



# 注册自定义命令
def register_commend(app):

    @app.cli.command()
    @click.option("--username",prompt=True)
    @click.option("--password",prompt=True,hide_input=True,confirmation_prompt=True)
    def admin(username,password):
        set_admin(username,password)
        click.echo("管理员创建成功")

    @app.cli.command()
    @click.option("--count",prompt=True)
    def category(count):
        set_category(count)
        click.echo("分类创建成功")

    @app.cli.command()
    @click.option("--count",prompt=True)
    def post(count):
        set_post(count)
        click.echo("文章创建成功")

    @app.cli.command()
    @click.option("--count",prompt=True)
    def commant(count):
        set_comment(count)
        click.echo("评论创建成功")

    @app.cli.command()
    @click.option("--count",prompt=True)
    def reply(count):
        set_reply(count)
        click.echo("回复创建成功")



# 注册日志处理
def register_loggin():
    pass