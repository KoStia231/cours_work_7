from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from users.models import User


class MyHabitsViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(first_name='test', email='testuser@gmail.com', password='testpass')

        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')


def test_get_my_habits(self):
    Habit.objects.create(
        autor=self.user,
        title='Habit 1',
        place='Home',
        duration=30,
        time_action=timezone.now().time(),
        action='Action 1',
        is_pleasant=False
    )
    Habit.objects.create(
        autor=self.user,
        title='Habit 2',
        place='Work',
        duration=45,
        time_action=timezone.now().time(),
        action='Action 2',
        is_pleasant=True
    )

    url = reverse('habits:my_habit-list')
    response = self.client.get(url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)


def test_create_habit(self):
    url = reverse('habits:my_habit-list')
    data = {
        'title': 'New Habit',
        'place': 'Gym',
        'duration': 60,
        'time_action': '12:00:00',
        'action': 'Workout',
        'is_pleasant': False
    }
    response = self.client.post(url, data, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Habit.objects.count(), 1)
    self.assertEqual(Habit.objects.get().title, 'New Habit')
    self.assertEqual(Habit.objects.get().autor, self.user)
