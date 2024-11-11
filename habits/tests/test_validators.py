from django.test import TestCase

from habits.validators import RewardAndRelatedValidator
from users.models import User


class RewardAndRelatedValidatorTest(TestCase):

    def setUp(self):
        self.validator = RewardAndRelatedValidator()
        self.user = User.objects.create_user(first_name='test', email='testuser@gmail.com', password='testpass')

    def test_both_prize_and_related(self):
        data = {
            'prize': 'Reward',
            'related': 1
        }
        with self.assertRaisesMessage(
                Exception,
                'Нельзя заполнять одновременно поле вознаграждения и поле связанной привычки.'
        ):
            self.validator(data)

    def test_only_prize(self):
        data = {
            'prize': 'Reward',
            'related': None
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    def test_only_related(self):
        data = {
            'prize': None,
            'related': 1
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')
