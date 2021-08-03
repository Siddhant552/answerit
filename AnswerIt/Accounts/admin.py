from django.contrib import admin
from Accounts.models import UserProfileInfo, Question, Answer, Feedback
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Feedback)
