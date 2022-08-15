from django.db import models


# Create your models here.


class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    was_chosen = models.BooleanField(default=False)
    is_right = models.BooleanField(default=False)
    related_question = models.ForeignKey("Question", on_delete=models.PROTECT)


class Question(models.Model):
    question = models.CharField(max_length=1000)
    importance = models.IntegerField(default = 5)
    related_test = models.ForeignKey("Test", on_delete=models.CASCADE)
    answered_correctly = models.BooleanField(default = False)

class Test(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField(blank = True )
    creator = models.ForeignKey("User", on_delete=models.PROTECT)
    score = models.IntegerField(default = 0)
    link = models.CharField(max_length=1000, default = '')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class User(models.Model):  # play with ORM
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    taken_tests = models.ManyToManyField("Test")

    def __str__(self):
        return self.nickname
