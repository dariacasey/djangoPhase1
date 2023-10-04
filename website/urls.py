from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
'''
Notes: 
- The second path call for accounts/ deals with authentication stuff
'''

urlpatterns = [
    path("admin/", admin.site.urls),
    # where root URL points
    path("", include("home.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # is the name not an error?
    path('classes/', include("classes.urls"), name='create_class'),
    path('lessons/', include('lessons.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
