from __future__ import unicode_literals
from django.db import models

# Create your models here.
#下面是博主资料的数据模型

class bloger (models.Model):
	bloger_nickname = models.CharField(max_length=50)
	bloger_email = models.EmailField
	bloger_image = models.ImageField



#下面是文章的数据模型
class article (models.Model):
	article_title = models.CharField(max_length=50)
	article_pub_time = models.DateTimeField('date published')
	article_text = models.TextField(max_length=9999)


##下面是账号的数据模型
class account (models.Model):
	user_nickname = models.CharField(max_length=50)
	user_email = models.EmailField
	user_regested_time = models.DateTimeField('time regested')
	user_last_login_time = models.DateTimeField('date login')