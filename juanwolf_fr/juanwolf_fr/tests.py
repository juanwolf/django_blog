import datetime

from django.test import TestCase
from freezegun import freeze_time

from juanwolf_fr import mixins


class BirthdayContextMixinTest(TestCase):

    def setUp(self):
        self.contextInstance = mixins.BirthdayContextMixin()

    @freeze_time("2016-11-26")
    def test_get_age_should_return_age_from_settings_values(self):
        birthday_date = datetime.date(2000, 1, 1)
        age_expected = 16
        with self.settings(BIRTHDAY_DATE=birthday_date):
            age = self.contextInstance.get_age()
            self.assertEqual(age, age_expected)

    def test_get_context_data_should_add_age_entry(self):
        context = self.contextInstance.get_context_data()
        self.assertIsNotNone(context.get('age', None))

    def test_get_context_data_should_contains_the_age_calculated(self):
        context = self.contextInstance.get_context_data()
        age_expected = self.contextInstance.get_age()
        self.assertEqual(context.get('age', None), age_expected)
