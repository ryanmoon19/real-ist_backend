from django.conf.urls import include, path

accounts_urlpatterns = [
    path(r'^api/v1/', include('djoser.urls')),
    path(r'^api/v1/', include('djoser.urls.authtoken')),
]
