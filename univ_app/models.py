from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField(blank = True )
    # creator = models.ForeignKey("User", on_delete=models.PROTECT, null=True, default=1)
    score = models.IntegerField(default = 0)
    link = models.CharField(max_length=1000, default = '')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.TextField(default = "")
    importance = models.IntegerField(default = 5, validators=[
        MaxValueValidator(10),
        MinValueValidator(1),
    ])
    related_test = models.ForeignKey("Test", on_delete=models.CASCADE, null=True )
    answered_correctly = models.BooleanField(default = False)

    def __str__(self):
        return self.question

    #property

    def get_test_questions(the_test:Test):
        the_questions = Question.objects.filter(related_test = the_test)
        return the_questions


class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    was_chosen = models.BooleanField(default=False)
    is_right = models.BooleanField(default=False)
    related_question = models.ForeignKey("Question", on_delete=models.PROTECT, null = True)


    def get_answers(the_question:Question):
        the_answers = Answer.objects.filter(related_question = the_question)
        return the_answers

    def __repr__(self):
        return self.answer

    def __str__(self):
        return self.answer


# class User(models.Model):  # play with ORM
#     nickname = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     taken_tests = models.ManyToManyField("Test")
#
#     def __str__(self):
#         return self.nickname
