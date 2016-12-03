from django.views import generic


class ResumeTemplateView(generic.TemplateView):
    template_name = "resume.html"
