from django.urls import path
from django.urls.conf import include

from dashboard.apps.frontend.views import IndexView
from dashboard.apps.pages.login.views import LoginView, GoogleView

app_name = 'app'

urlpatterns = [
    path('', 				IndexView.as_view(),	name='index'),
    path('login',			LoginView.as_view(),	name='login'),
    path('google',			GoogleView.as_view(),	name='google'),

    path('pages/',			include('dashboard.apps.pages.urls')),
    path('components/',		include('dashboard.apps.components.urls')),
    path('utilities/',		include('dashboard.apps.utilities.urls')),
]
