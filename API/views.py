import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Questionnaire, QuestionnaireContent
from .serializers import QuestionnaireSerializers, QuestionnaireContentSerializers, QuestionnaireListSerializers


# Create your views here.

def getQuestionnairesList(request):
    queryset = Questionnaire.objects.all()
    return JsonResponse(QuestionnaireListSerializers(queryset, many=True).data, safe=False)


def getAllQuestionnaires(request):
    queryset = Questionnaire.objects.all()
    # print(queryset)
    return JsonResponse(QuestionnaireSerializers(queryset, many=True).data, safe=False)


def getQuestionnairesByUid(request, id):
    queryset = Questionnaire.objects.get(uid=id)
    # print(queryset)
    return JsonResponse(QuestionnaireSerializers(queryset).data, safe=False)

def poss1(request):
    if request.method == 'POST':
        jsn = json.loads(request.POST.get('1', None))  # raw data
        # jsn = json.loads(request.body.decode("utf-8"))  ->form data
        print(jsn)
        return JsonResponse(jsn)
    elif request.method == 'GET':
        return HttpResponse("its get")

#
# class QuestionnairesViewSet(viewsets.ModelViewSet):
#     # lookup_field = 'patientType'
#     queryset = Questionnaire.objects.all().order_by('pk')
#     serializer_class = QuestionnaireSerializers
#
#
# class QuestionnaireContentViewSet(viewsets.ModelViewSet):
#     queryset = QuestionnaireContent.objects.all().order_by('pk')
#     serializer_class = QuestionnaireContentSerializers
