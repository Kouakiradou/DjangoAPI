from django.contrib import admin
from .models import Questionnaire
from .models import QuestionnaireContent
# Register your models here.

@admin.register(Questionnaire)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

@admin.register(QuestionnaireContent)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'questionText')