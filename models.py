from django.db import models
import datetime
from django.utils import timezone


class Locations(models.Model):
    location_name=models.CharField(max_length=30)
    def __str__(self):
        return self.location_name


class Join(models.Model):
    user = models.ForeignKey('Users',on_delete="CASCADE")
    event = models.ForeignKey('Events',on_delete='CASCADE')
    is_inviter = models.BooleanField(null=False)

class Events(models.Model):
    initiator=models.ManyToManyField(
        'Users',
        through='Join',
        through_fields=('event_id','user_id')
    )
    event_title=models.CharField(max_length=30,null=True)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now_add=True)
    submit_time=models.DateTimeField(default=timezone.now())
    event_text=models.CharField(max_length=200)
    location=models.ForeignKey('Locations',to_field='id',on_delete='CASCADE',related_name='events_in_here')

    def __str__(self):
        return self.event_text


class Users(models.Model):
    SEX_CHOICES=(
        ('男','男'),
        ('女','女'),
    )
    user_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=2,default='男',choices=SEX_CHOICES)
    email=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(default=18)
    password=models.CharField(max_length=40,default='123456')
    phone_number=models.CharField(max_length=11,null=True)


    def __str__(self):
        return self.name
    def getObject(self):
        return self


class testClass(models.Model):
    t_id=models.ForeignKey('Users',to_field='user_id',on_delete='CASCADE',related_name='t_id')
    t_tid=models.ForeignKey('Users',to_field='user_id',on_delete='CASCADE',related_name='t_tid')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes=models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
