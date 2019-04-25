from faker import Faker
from biger_blog.models import *
import random

fake = Faker("zh_CN")

def set_admin(username,password):
     admin = Admin(username=username)
     admin.set_password(password)
     db.session.add(admin)
     db.session.commit()



def set_category(count=10):
    for i in range(int(count)):
        category = Category(category_name=fake.word())
        db.session.add(category)
    db.session.commit()



def set_post(count=50):
    for i in range(int(count)):
        post = Post(title=fake.sentence(),body=fake.text(2000),timestamp=fake.date_time_this_year(),category_id=random.randint(1,Category.query.count()))
        db.session.add(post)
    db.session.commit()


def set_comment(count=500):
    for i in range(int(count)):
        comment = Comment(comment=fake.sentence(),username=fake.name(),timestamp=fake.date_time_this_year(),post_id=random.randint(1,Post.query.count()))
        db.session.add(comment)
    db.session.commit()

def set_reply(count=2000):
    for i in range(int(count)):
        reply = Reply(reply=fake.sentence(),username=fake.name(),timestamp=fake.date_time_this_year(),comment_id=random.randint(1,Comment.query.count()))
        db.session.add(reply)
    db.session.commit()












