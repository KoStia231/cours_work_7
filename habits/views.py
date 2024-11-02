from rest_framework import viewsets

from habits.models import Habit
from habits.paginators import MyPageNumberPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class MyHabitsViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с собственными привычками пользователя.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(autor=self.request.user)


class PublicHabitsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для работы с публичными привычками.
    """
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(is_public=Habit.IsPublicHabit.OPEN).exclude(autor=user)
