import dashboard.apps.core.views as CoreView
from dashboard.apps.core.utils import log

from .models import TableData


class IndexView(CoreView.IndexView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'tables/base.html'

    data = TableData()

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data

        log(self.module, 'get_context_data', 'context=%r' %
            context, file=__file__)

        return context
