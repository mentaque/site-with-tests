from django.contrib import admin

from app.models import UserAnswer, TestSession, Answer, Question, Test, Result

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestSession)
admin.site.register(UserAnswer)
admin.site.register(Result)
