from django.shortcuts import render

import dashboard.apps.core.views as CoreView
from dashboard.apps.core.utils import log


class IndexView(CoreView.IndexView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'pagenotfound/base.html'
