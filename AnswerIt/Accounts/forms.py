from django import forms
from django.contrib.auth.models import User
from Accounts.models import UserProfileInfo, Question, Answer, Feedback

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields= ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('name','age','qualifications')


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question',)

        widgets = {
            'question': forms.TextInput(attrs={'class': 'textinputclass'}),
        }


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)

        widgets = {
            'answer': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('feedback',)

        widgets = {
            'feedback': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
