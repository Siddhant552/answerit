from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from Accounts.forms import UserForm, UserProfileInfoForm
from django.shortcuts import render
from Accounts.forms import UserForm,UserProfileInfoForm, QuestionForm, AnswerForm, FeedbackForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from Accounts.models import UserProfileInfo, Question, Answer, Feedback
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'signup.html', {'user_form':user_form,
                                            'profile_form':profile_form,
                                            'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Accounts:question_list'))
            else:
                return HttpResponse("<h1>Account not active :(</h1>")

        else:
            print("Someone tried to login and failed.")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("<h1>Invalid login details supplied.</h1>")

class QuestionListView(ListView):
    model = Question


    def get_queryset(self):
        return Question.objects.filter(date_time__lte=timezone.now()).order_by('-date_time')

class QuestionDetailView(DetailView):
    model = Question





class CreateQuestionView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    form_class = QuestionForm

    model = Question
    def post(self, request):
        print(request.POST['question'])
        q = Question()
        q.question = request.POST['question']
        q.date_time = timezone.now()
        q.user = request.user
        q.save()

        return redirect('Accounts:question_list')

class Thankyou(LoginRequiredMixin, TemplateView):
    template_name = "Accounts/thankyou.html"

class FeedbackView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = FeedbackForm
    model = Feedback
    def post(self, request):
        f = Feedback()
        f.user = request.user
        f.feedback = request.POST['text']
        f.save()

        return redirect('Accounts:thanksfeedback')


class CreateAnswerView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AnswerForm
    model = Answer


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context['view'].kwargs['question']
        context['question'] = question
        return context
    def post(self, request, **kwargs):

        a = Answer()
        a.answer = request.POST['answer']
        a.date_time = timezone.now()
        a.author = request.user
        a.question = Question.objects.get(id = self.kwargs['id'])
        a.save()
        return redirect('Accounts:question_detail', pk=Question.objects.get(id = self.kwargs['id']).pk)



class YourQuestionsListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Question
    template_name_suffix = '_your'
    def get_queryset(self):
        u = self.request.user.username
        queryset = Question.objects.filter(user__username__iexact=u)
        context_object_name = 'your_questions_list'
        return queryset


class AnswerListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    model = Answer

    def get_queryset(self):
        u = get_object_or_404(User, username=self.request.user.username)
        queryset = Answer.objects.filter(author__username__iexact=u)
        context_object_name = 'answer_list'
        return queryset


class UserProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'Accounts/user_profile.html'
    def get(self, request, **kwargs):
        user = User.objects.get(pk = kwargs['pk'])

        return render(request, self.template_name, {'u': user})




class AnswerDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Answer
    success_url = reverse_lazy("Accounts:your_answers")

#   <img class="profilepic" src="{{user.info.picture.url}}" alt="aaaa" style="display:block;margin-left:auto;margin-right:auto;" >


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Question
    success_url = reverse_lazy("Accounts:your_questions")



class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    form_class = UserProfileInfoForm
    model = UserProfileInfo

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = QuestionForm
    model = Question

class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = AnswerForm
    model = Answer
