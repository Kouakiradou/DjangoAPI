from rest_framework import serializers
from .models import QuestionnaireContent, Questionnaire


class QuestionnaireContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireContent
        fields = ('id', 'questionText', 'answerType')


class QuestionnaireSerializers(serializers.ModelSerializer):
    questionnaireContent = QuestionnaireContentSerializers(many=True)

    class Meta:
        model = Questionnaire
        fields = ('id', 'title', 'ages', 'patientType', 'questionnaireContent')


