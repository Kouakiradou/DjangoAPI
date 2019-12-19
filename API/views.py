import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Questionnaire, QuestionnaireContent
from .serializers import QuestionnaireSerializers, QuestionnaireContentSerializers


# Create your views here.

def getQuestionairesList(request):
    jsn = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    return JsonResponse(jsn)


class QuestionnairesViewSet(viewsets.ModelViewSet):
    # lookup_field = 'patientType'
    queryset = Questionnaire.objects.all().order_by('pk')
    serializer_class = QuestionnaireSerializers


class QuestionnaireContentViewSet(viewsets.ModelViewSet):
    queryset = QuestionnaireContent.objects.all().order_by('pk')
    serializer_class = QuestionnaireContentSerializers


def getQuestionnairesById(request, nid):
    queryset = Questionnaire.objects.get(pk=nid)
    print(queryset)
    return JsonResponse(QuestionnaireSerializers(queryset).data, safe=False)

def poss1(request):
    if request.method== 'POST':
        jsn = json.loads(request.POST.get('1', None))  # raw data
        # jsn = json.loads(request.body.decode("utf-8"))  ->form data
        print(jsn)
        return JsonResponse(jsn)
    elif request.method=='GET':
        return HttpResponse("its get")

