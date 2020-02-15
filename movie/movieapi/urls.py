from django.urls import include, path
from rest_framework import routers
from . import views

#providing the required links to view two models by calling respective view functions

router = routers.DefaultRouter()
router.register(r'Details', views.View_Details)
router.register(r'Comments', views.View_Comments)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]