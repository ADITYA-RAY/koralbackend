from django.urls import include, path
from rest_framework import routers
from quotation import views as quotation_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'quotation', quotation_views.QuotationView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('', include('quotation.urls')),
    path('api/', include(router.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "KORAL"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"
