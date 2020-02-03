from rest_framework import serializers
from .models import QuestionnaireContent, Questionnaire


class QuestionnaireContentSerializers(serializers.ModelSerializer):

    class Meta:
        model = QuestionnaireContent
        fields = ('qid', 'questionText', 'answerType')
        extra_kwargs = {
            'qid': {'validators': []},
        }


class QuestionnaireSerializers(serializers.ModelSerializer):
    questionnaireContent = QuestionnaireContentSerializers(many=True)

    class Meta:
        model = Questionnaire
        fields = ('uid', 'title', 'ages', 'patientType', 'questionnaireContent')
        extra_kwargs = {
            'uid': {'validators': []},
        }


class QuestionnaireListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('uid', 'title')


# class QuestionnaireSerializersNoUid(serializers.ModelSerializer):
#     questionnaireContent = QuestionnaireContentSerializers(many=True)
#
#     class Meta:
#         model = Questionnaire
#         fields = ('title', 'ages', 'patientType', 'questionnaireContent')
