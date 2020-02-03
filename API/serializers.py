from rest_framework import serializers
from .models import QuestionnaireContent, Questionnaire


class QuestionnaireContentSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = QuestionnaireContent
        fields = ('id', 'questionText', 'answerType')


class QuestionnaireSerializers(serializers.ModelSerializer):
    questionnaireContent = QuestionnaireContentSerializers(many=True)

    class Meta:
        model = Questionnaire
        fields = ('uid', 'title', 'ages', 'patientType', 'questionnaireContent')


class QuestionnaireListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('uid', 'title')


class QuestionnaireSerializersNoUid(serializers.ModelSerializer):
    questionnaireContent = QuestionnaireContentSerializers(many=True)

    class Meta:
        model = Questionnaire
        fields = ('title', 'ages', 'patientType', 'questionnaireContent')
