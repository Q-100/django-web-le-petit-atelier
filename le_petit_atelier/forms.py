from django import forms
from .models import Question
from .models import Answer


class QuestionForm(forms.ModelForm):
    """
    장고폼은 forms.From을 상속받으면 폼, forms.ModelForm을 상속받으면 모델폼이라함
    모델폼은 모델과 연결된 폼이며 모델 폼객체를 저장하면 연결된 모델의 데이터를 저장할 수 있음
    """

    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            "subject": "제목",
            "content": "내용",
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = {'content'}
        labels = {
            "content": "답변내용",
        }
