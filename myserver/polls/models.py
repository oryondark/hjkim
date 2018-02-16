from django.db import models

# Create your models here.

class Question(models.Model):
    qs_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

class Choice(models.Model):
    qs = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Userinfo(models.Model):
    u_name = models.CharField(max_length=50)
    u_hobby = models.CharField(max_length=100)
    print(u_name)

class Userbirth(models.Model):
    user = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    u_birth = models.IntegerField()
    print(u_birth)


