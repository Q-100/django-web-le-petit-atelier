from django.urls import path, include
from le_petit_atelier import views

app_name = "le_petit_atelier"
urlpatterns = [

    # 여기서 path가 ''인 이유는 메인의 urls에서 이미
    # path('le_petit_atelier/', include('le_petit_atelier.urls')),로 처리했기때문에
    # 여기의 urls에 path('le_petit_atelier/'로하면 결국
    # le_petit_atelier/le_petit_atelier/ 가 되기 때문에 앞에서 처리한걸 뒤에서 또할필요없음
    # test
    path('', views.index, name='index'),
    path("<int:question_id>", views.detail, name='detail'),
    path("answer/create/<int:question_id>", views.answer_create, name="answer_create"),
    path("question/create/", views.question_create, name="question_create"),
]
