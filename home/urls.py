from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import(
	buscar_sacramentos_view,
	)

urlpatterns = patterns('',
	url(r'^$',TemplateView.as_view(template_name='index.html'), name='index'),
	url(r'^home/$', login_required(TemplateView.as_view(template_name='home.html'),login_url='/login/'), name='home'),   
	url(r'^accesibilidad/$', login_required(TemplateView.as_view(template_name='accesibilidad.html'),login_url='/login/'), name='accesibilidad'),   
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^buscar/$', buscar_sacramentos_view, name='buscar'),   
)