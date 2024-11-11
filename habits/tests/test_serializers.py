from datetime import time
from django.test import TestCase
from habits.serializers import HabitSerializer
from users.models import User


class HabitSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name='test', email='testuser@gmail.com', password='testpass')

    def test_valid_data(self):
        data = {
            'autor': self.user.id,
            'title': 'Test Habit',
            'place': 'Home',
            'duration': 2,
            'time_action': time(12, 0),  # Используем объект time вместо строки
            'action': 'Do something',
            'is_pleasant': False
        }
        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid(), f"Errors: {serializer.errors}")

    def test_invalid_data(self):
        data = {
            'autor': self.user.id,
            'title': '',  # Пустое значение
            'place': 'Home',
            'duration': -10,  # Неверное значение для duration
            'time_action': '25:00:00',  # Неверный формат времени
            'action': 'Do something',
            'is_pleasant': False
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        # Проверяем ошибку по полю title
        self.assertIn('title', serializer.errors)

        # Проверяем, есть ли ошибка по полю duration
        self.assertIn('duration', serializer.errors)
        self.assertIn('Убедитесь, что это значение больше либо равно 0.', serializer.errors['duration'])

        # Проверяем ошибку по времени
        self.assertIn('time_action', serializer.errors)