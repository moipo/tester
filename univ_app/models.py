from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100 )
    slug = models.SlugField(max_length = 120 , blank = True, null = True)


    description = models.TextField(blank = True )
    # creator = models.ForeignKey("User", on_delete=models.PROTECT, null=True, default=1)
    score = models.IntegerField(default = 0)
    link = models.CharField(max_length=1000, default = '')

    def save(self, *args, **kwargs):
        if self.slug is None: #if title is changed => slug is generated.
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/articles/{self.slug}/'
        #<a href = "/articles/{{x.id}}/ =>
        #<a href = "{{x.get_absolute_url}}">


def test_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")
    print(args,kwargs) #instance = Test instance
    print(sender,instance)
    if instance.slug is None: #if title is changed => slug is generated.
        instance.slug = slugify(instance.title)
    # super().save(*args, **kwargs)
    pass

pre_save.connect(test_pre_save, sender = Test)
#pre_save is going to connect to test_pre_save() every time the model
#Test is saved

def test_post_save(sender, instance, created, *args, **kwargs): #is called after Test is saved
    print("post_save")
    print(args,kwargs)
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

post_save.connect(test_post_save, sender = Test)




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
