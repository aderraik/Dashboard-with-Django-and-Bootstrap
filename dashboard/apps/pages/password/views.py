from django.shortcuts import render
from django.views import generic

import dashboard.apps.pages.login.views as LoginViews
from dashboard.apps.core.utils import log


class IndexView(LoginViews.IndexView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'password/base.html'
