import dashboard.apps.core.views as CoreView
from dashboard.apps.core.utils import log


class IndexView(CoreView.IndexView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'buttons/base.html'

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)

        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        log(self.module, 'get_context_data', 'context=%r' %
            context, file=__file__)

        return context
