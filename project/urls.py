from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.shortcuts import render

from registration.backends.simple.views import RegistrationView

from accounts.forms import RegistrationFormWithoutUsername

admin.autodiscover()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = []

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^t/(.*)$', render),
    url(r'^', include('boards.urls')),
    url(
        r'^accounts/register/$',
        RegistrationView.as_view(form_class=RegistrationFormWithoutUsername),
        name='registration_register'
    ),
    url(r'^accounts/', include('registration.backends.simple.urls'))
]
