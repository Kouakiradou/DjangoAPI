from rest_framework import serializers
from .models import QuestionnaireContent, Questionnaire, AnswerContent, QuestionAnswer


class QuestionnaireContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireContent
        fields = ('qid', 'questionText', 'answerType', 'choices')
        # extra_kwargs = {
        #     'qid': {'validators': []},
        # }


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


class QuestionAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ('qid', 'answerType', 'answer')


class AnswerContentSerializers(serializers.ModelSerializer):
    questionAnswer = QuestionAnswerSerializers(many=True)

    class Meta:
        model = AnswerContent
        fields = ('uid', 'date', 'age', 'questionAnswer')
