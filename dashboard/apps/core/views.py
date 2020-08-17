from django.shortcuts import render
from django.views import generic

from dashboard.apps.core.utils import log


class IndexView(generic.ListView):
    """
    IndexView:
    """
    module = 'IndexView'

    num_alerts = 2
    num_messages = 5

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['num_alerts'] = self.num_alerts
        context['num_messages'] = self.num_messages

        # log(self.module, 'get_context_data', 'context=%r' % context, file = __file__)

        return context
