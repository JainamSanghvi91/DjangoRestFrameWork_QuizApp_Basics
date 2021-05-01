from rest_framework.serializers import ModelSerializer
from qv1.models import Question,Quiz

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        # fields = '__all__'
        exclude = ('url',)
class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'  