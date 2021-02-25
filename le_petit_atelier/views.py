from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone


# Create your views here.

def index(request):
    """
    order_by : 조회한 데이터를 특정 속성으로 정렬함
    create_date : 작성일시순으로 정렬(-가 붙었으므로 역순으로 정렬)
    context : render함수가 템플릿을 HTML로 변환하는 과정에서 사용되는 데이터
    render : context에 있는 Quesiton 모델 데이터를 html로 변환함(이런 파일을 템플릿이라함)
    :param request:
    :return:
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'le_petit_atelier/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)  # 페이지가 없으면 404페이지 반환
    context = {'question': question}
    return render(request, "le_petit_atelier/question_detail.html", context)


def answer_create(request, question_id):
    """
    request.POST.get("content") : request로 넘어온 데이터를 추출하는 코드
        -> request로 넘어온 데이터 중 name이 content인 값
    question.answer_set.create : Question모델을 통해 Answer모델 데이터를 생성하기 위한 코드
        -> Answer모델이 Question 모델을 참조하고있어서 question.answer_set 같은 표현 가능
    :param request: detail.html에서 textarea에 입력된 데이터가 담겨서 넘어옴
    :param question_id: URL 매핑 정보값이 넘어옴
    :return
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get("content"), create_date=timezone.now())
    return redirect("le_petit_atelier:detail", question_id=question.id)
