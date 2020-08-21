from django.shortcuts import render
from django.views import generic

from dashboard.apps.core.utils import log


class IndexView(generic.TemplateView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'login/base.html'

    data = None

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data

        return context


class LoginView(generic.TemplateView):
    """
    LoginView:
    """
    module = 'LoginView'
    template_name = 'login/base.html'

    data = None

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data

        return context


class GoogleView(generic.TemplateView):
    """
    GoogleView:
    """
    module = 'GoogleView'
    template_name = 'login/base.html'

    data = None

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data

        return context
