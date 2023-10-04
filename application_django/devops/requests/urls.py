from django.urls import include, path
from .views import RequestListApiView as request_view
from he
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('request/', request_view.as_view(), name='requests_detail_view'),
]