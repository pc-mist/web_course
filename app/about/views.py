# -*- coding: utf8 -*-
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about/index.html'
