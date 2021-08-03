from django.urls import path
from Accounts import views

app_name = 'Accounts'

urlpatterns = [path('register/', views.register, name = "register"),
               path('user_login/', views.user_login, name = "user_login"),
               path('user_logout/', views.user_logout, name = "user_logout"),
               path('question_list/',views.QuestionListView.as_view(), name="question_list"),
               path('question/<int:pk>/', views.QuestionDetailView.as_view(), name="question_detail"),
               path('question/new/',views.CreateQuestionView.as_view(), name = "new_question"),
               path('your_answers/', views.AnswerListView.as_view(), name = "your_answers"),
               path('answer/new/<question>/<int:id>/',views.CreateAnswerView.as_view(), name = "new_answer"),
               path('user_profile/<int:pk>/',views.UserProfileView.as_view(), name = "user_profile"),
               path('your_answer/delete_answer/<int:pk>/',views.AnswerDeleteView.as_view(), name = "delete_answer"),
               path('your_questions/', views.YourQuestionsListView.as_view(), name = "your_questions"),
               path('your_answer/delete_question/<int:pk>/',views.QuestionDeleteView.as_view(), name = "delete_question"),
               path('user_profile/edit/<int:pk>/',views.ProfileUpdateView.as_view(), name = "edit_profile"),
               path('your_questions/edit/<int:pk>/',views.QuestionUpdateView.as_view(), name = "edit_question"),
               path('your_answers/edit_answer/<int:pk>/', views.AnswerUpdateView.as_view(), name="edit_answer"),
               path('feedback/', views.FeedbackView.as_view(), name = "feedback"),
               path('thankyou/', views.Thankyou.as_view(), name = 'thanksfeedback'),
               ]
