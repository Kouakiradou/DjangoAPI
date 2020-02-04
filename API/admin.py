from django.contrib import admin
from .models import Questionnaire, AnswerContent, QuestionAnswer
from .models import QuestionnaireContent


# Register your models here.

@admin.register(Questionnaire)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(QuestionnaireContent)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'questionText')


@admin.register(AnswerContent)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'uid')


@admin.register(QuestionAnswer)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'qid')
