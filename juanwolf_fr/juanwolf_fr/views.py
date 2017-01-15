from django.views import generic

from juanwolf_fr import mixins


class IndexView(generic.TemplateView, mixins.BirthdayContextMixin):
    """
    First page of the website. "The famous 'Index'"
    """
    template_name = "index.html"


class AboutView(generic.TemplateView, mixins.BirthdayContextMixin):
    template_name = "about.html"
