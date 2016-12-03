from django.views import generic

from juanwolf_fr import mixins


class ResumeTemplateView(generic.TemplateView, mixins.BirthdayContextMixin):
    template_name = "resume.html"
