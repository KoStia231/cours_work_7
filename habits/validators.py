from django.utils import timezone
from rest_framework import serializers

from habits.models import Habit


class RewardAndRelatedValidator:
    def __call__(self, value):
        if value.get('prize') and value.get('related'):
            raise serializers.ValidationError(
                'Нельзя заполнять одновременно поле вознаграждения и поле связанной привычки.'
            )


class ExecutionTimeValidator:
    def __call__(self, value):
        if value.get('duration', 0) > 2:
            raise serializers.ValidationError(
                'Время выполнения должно быть не больше 2 минут.'
            )


class PleasantHabitValidator:
    def __call__(self, value):
        related_id = value.get('related')
        if related_id:
            related_habit = Habit.objects.filter(id=related_id).first()
            if related_habit and not related_habit.is_pleasant:
                raise serializers.ValidationError(
                    'Связанная привычка должна быть помечена как приятная.'
                )


class PleasantHabitNoRelatedOrPrizeValidator:
    def __call__(self, value):
        if value.get('is_pleasant') and (value.get('prize') or value.get('related')):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.'
            )


class FrequencyValidator:
    def __call__(self, value):
        if value.get('execution_interval_day', 0) > 7:
            raise serializers.ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
            )


class LastPerformedValidator:
    def __call__(self, value):
        if value.get('last_performed'):
            days_since_last = (timezone.now().date() - value['last_performed']).days
            if days_since_last > 7:
                raise serializers.ValidationError(
                    'Нельзя не выполнять привычку более 7 дней.'
                )
