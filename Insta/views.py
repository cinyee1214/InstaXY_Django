from django.views.generic import TemplateView

#HelloWorld is-a TemplateView

class HelloWorld(TemplateView):
    template_name = 'test.html'
