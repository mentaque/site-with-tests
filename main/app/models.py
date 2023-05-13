from django.contrib.auth.models import User
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    number_of_question = models.IntegerField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestSession(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserAnswer(models.Model):
    testsession = models.ForeignKey(TestSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answers = models.IntegerField()
    all_questions = models.IntegerField()
