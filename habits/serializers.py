from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    RewardAndRelatedValidator,
    ExecutionTimeValidator,
    PleasantHabitValidator,
    FrequencyValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardAndRelatedValidator(),
            ExecutionTimeValidator(),
            PleasantHabitValidator(),
            FrequencyValidator()
        ]
