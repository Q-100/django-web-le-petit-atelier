from django.db import models


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문 제목(글자 수를 제한하고싶을 때는 CharField 사용
    content = models.TextField()  # 본문(글자수 제한없음)
    create_date = models.DateTimeField()  # 날짜


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 어떤 질문에 대한 답변(다른 모델을 속성으로 가지면 ForeignKey를 사용)
    content = models.TextField() # 본문
    create_date = models.DateTimeField() # 날짜
