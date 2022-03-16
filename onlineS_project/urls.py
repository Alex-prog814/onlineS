from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from onlineS_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.product.urls')),
    path('account/', include('applications.account.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
