from django.utils import timezone
from rest_framework import serializers


class RewardAndRelatedValidator:
    def __call__(self, habit):
        if habit.prize and habit.related:
            raise serializers.ValidationError(
                'Нельзя заполнять одновременно поле вознаграждения и поле связанной привычки.'
            )


class ExecutionTimeValidator:
    def __call__(self, habit):
        if habit.duration > 120:
            raise serializers.ValidationError(
                'Время выполнения должно быть не больше 120 минут.'
            )


class PleasantHabitValidator:
    def __call__(self, habit):
        if habit.related and not habit.related.is_pleasant:
            raise serializers.ValidationError(
                'Связанная привычка должна быть помечена как приятная.'
            )


class PleasantHabitNoRelatedOrPrizeValidator:
    def __call__(self, habit):
        if habit.is_pleasant and (habit.prize or habit.related):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.'
            )


class FrequencyValidator:
    def __call__(self, habit):
        if habit.execution_interval_day < 7:
            raise serializers.ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
            )


class LastPerformedValidator:
    def __call__(self, habit):
        if habit.last_performed:
            days_since_last = (timezone.now().date() - habit.last_performed).days
            if days_since_last > 7:
                raise serializers.ValidationError(
                    'Нельзя не выполнять привычку более 7 дней.'
                )
