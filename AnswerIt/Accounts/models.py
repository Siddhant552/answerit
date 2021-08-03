from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, related_name= "info",on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    qualifications = models.CharField(max_length=100, blank=True)



    def get_absolute_url(self, ):
        return reverse("Accounts:user_profile", kwargs={'pk':self.user.pk})


    def __str__(self):
        return self.user.username

class Question(models.Model):
    user = models.ForeignKey(User,related_name="user_question", on_delete = models.CASCADE)
    question = models.CharField(max_length = 250)
    date_time = models.DateField()

    def answer_count(self):
        return self.answers

    def get_absolute_url(self, ):
        return reverse("Accounts:your_questions")


    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name = "answers", on_delete = models.CASCADE, default = 'None')
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_time = models.DateField()

    def get_absolute_url(self, ):
        return reverse("Accounts:your_answers")

    def __str__(self):
        return self.answer

class Feedback(models.Model):
    feedback = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
