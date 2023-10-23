import datetime

from .models import Question

from django.test import TestCase
from django.utils import timezone


class QuestionModelTests(TestCase):
    def test_was_published_in_future_with_future_question(self):
        """
        was_published_recently returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_in_future_with_recent_question(self):
        """
        was_published_recently returns True for questions whose pub_date is within the past day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)

    def test_was_published_in_future_with_old_question(self):
        """
        was_published_recently returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)
