from django.views import generic

from dashboard.apps.core import views
from dashboard.apps.core.utils import log


class IndexView(generic.TemplateView):
	"""
	IndexView:
	"""
	module = 'IndexView'
	template_name = 'login/base.html'
	ss = 10

	year = 2020
	support_email = 'info@exmaple.com'
	title = 'Dashborad'
	data = None

	def get_queryset(self):
		log(self.module, 'get_queryset', file=__file__)

		return self.data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = self.data
		context['title'] = self.title
		context['year'] = self.year
		context['support_email'] = self.support_email

		return context


class LoginView(views.IndexView):
	"""
	LoginView:
	"""
	module = 'LoginView'
	template_name = 'frontend/index.html'

	def get_queryset(self):
		log(self.module, 'get_queryset', file=__file__)

		return self.data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context


class LogoutView(views.IndexView):
	"""
	LogoutView:
	"""
	module = 'LogoutView'
	template_name = 'login/base.html'

	user = None
	data = None

	def get_queryset(self):
		log(self.module, 'get_queryset', file=__file__)

		return self.data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = self.data

		log(self.module, 'get_context_data', 'context=%r' % context, file=__file__)

		return context


class GoogleView(IndexView):
	"""
	GoogleView:
	"""
	module = 'GoogleView'
	template_name = 'login/base.html'

	data = None
