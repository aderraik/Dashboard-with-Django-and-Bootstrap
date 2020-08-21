from django.shortcuts import render
from django.views import generic

from dashboard.apps.core.utils import log


class IndexView(generic.TemplateView):
    """
    IndexView:
    """
    module = 'IndexView'

    num_alerts = 2
    num_messages = 5
    user = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user = request.user

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['num_alerts'] = self.num_alerts
        context['num_messages'] = self.num_messages
        context['user'] = {
            'is_authenticated': self.user.is_authenticated,
            'login': self.user.name if self.user.is_authenticated else 'Need login',
        }

        log(self.module, 'get_context_data', 'context=%r' %
            context, file=__file__)

        return context
