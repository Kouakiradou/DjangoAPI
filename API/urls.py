from django.urls import path, include
from . import views
from rest_framework import routers

# route = routers.DefaultRouter()
# route.register(r'getQuestionnairesList', views.QuestionnairesViewSet)


urlpatterns = [
    # path('', include(route.urls)),
    path('<int:nid>/', views.getQuestionnairesById, name='getQuestionnairesById'),
     path('poss/', views.poss1)
    # path('a/', views.QuestionnairesViewSet),
]