from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.views import MyHabitsViewSet, PublicHabitsViewSet


app_name = 'habits'

router = DefaultRouter()
router.register(r'my-habits', MyHabitsViewSet, basename='my_habit')
router.register(r'public-habits', PublicHabitsViewSet, basename='public_habit')

urlpatterns = [
    path('', include(router.urls)),
]
