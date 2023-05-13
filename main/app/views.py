from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from app.models import Test, TestSession, Question, Answer, UserAnswer, Result


@login_required
def main_page(request):
    tests = Test.objects.all()
    return render(request, 'index.html', {'tests': tests})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login_page.html', {'form': form})


@login_required
def start_test_page(request, test_id):
    test = Test.objects.get(id=test_id)
    session = TestSession.objects.filter(user=request.user, test=test).last()
    first_q = Question.objects.filter(test=test).first()
    if request.method == 'POST' and 'starting' in request.POST:
        session = TestSession.objects.create(user=request.user, test=test)
        return redirect('question_page', test_id=test_id, session_id=session.id, question_id=first_q.id)
    elif request.method == 'POST' and 'continue' in request.POST:
        last_user_answer = UserAnswer.objects.filter(testsession=session).last()
        try:
            return redirect('question_page', test_id=test_id, session_id=session.id,
                            question_id=last_user_answer.question.id)
        except:
            return redirect('question_page', test_id=test_id, session_id=session.id,
                            question_id=first_q.id)
    return render(request, 'start_test_page.html', {'session': session})


@login_required
def question_page(request, test_id, session_id, question_id):
    test = Test.objects.get(id=test_id)
    question = Question.objects.get(id=question_id, test=test)
    answers = Answer.objects.filter(question=question)
    counter = Question.objects.filter(test=test).count()
    if request.method == 'POST' and 'save' in request.POST:
        session = TestSession.objects.get(id=session_id)
        answer_id = request.POST.get('answer')
        answer = Answer.objects.get(id=answer_id)
        try:
            user_answer = UserAnswer.objects.get(testsession=session, question=question)
            user_answer.answer = answer
            user_answer.save()
        except:
            UserAnswer.objects.create(testsession=session, answer=answer, question=question)
        current_q_number = question.number_of_question
        try:
            next_q = Question.objects.get(test=test, number_of_question=current_q_number + 1)
            return redirect('question_page', test_id=test_id, session_id=session.id, question_id=next_q.id)
        except:
            return redirect('end_test_page', test_id=test_id, session_id=session.id)
    return render(request, 'question_page.html', {'question': question, 'answers': answers, 'test_id': test_id,
                                                  'session_id': session_id, 'counter': counter})


@login_required
def end_test_page(request, test_id, session_id):
    test = Test.objects.get(id=test_id)
    session = TestSession.objects.get(id=session_id)
    questions = Question.objects.filter(test=test)
    answers = UserAnswer.objects.filter(testsession=session)
    if request.method == 'POST' and 'ending' in request.POST:
        all_questions = questions.count()
        right_answers = 0
        for answer in answers:
            if answer.answer.correct:
                right_answers += 1
        Result.objects.create(test=test, user=request.user, right_answers=right_answers, all_questions=all_questions)
        TestSession.objects.get(id=session_id).delete()
        return redirect('/')
    return render(request, 'end_test_page.html', {'questions': questions, 'answers': answers, 'session_id': session_id,
                                                  'test_id': test_id})


@login_required
def results_page(request, test_id):
    test = Test.objects.get(id=test_id)
    results = Result.objects.filter(test=test, user=request.user)[::-1]
    return render(request, 'results_page.html', {'results': results})

