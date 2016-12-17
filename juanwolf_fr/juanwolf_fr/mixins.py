from datetime import date

from django.views import generic
from django.conf import settings


class BirthdayContextMixin(generic.base.ContextMixin):
    """
    Add into the context the age of the owner of the website.
    To change this value please have a look at the BIRTHDAY_DATE setting.
    """

    def get_age(self):
        today = date.today()
        years_delta = today.year - settings.BIRTHDAY_DATE.year
        is_before_birthday = (today.month, today.day) < (
            settings.BIRTHDAY_DATE.month, settings.BIRTHDAY_DATE.day
        )
        return years_delta - int(is_before_birthday)

    def get_context_data(self, **kwargs):
        context = super(BirthdayContextMixin, self).get_context_data(**kwargs)
        context['age'] = self.get_age()
        return context
