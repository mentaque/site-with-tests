from django.urls import path

from app.views import main_page, start_test_page, question_page, end_test_page, login_page, results_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('accounts/login/', login_page, name='login_page'),
    path('<int:test_id>/', start_test_page, name='start_test_page'),
    path('<int:test_id>/<int:session_id>/<int:question_id>/', question_page, name='question_page'),
    path('<int:test_id>/<int:session_id>/ending/', end_test_page, name='end_test_page'),
    path('<int:test_id>/results', results_page, name='results_page'),
]