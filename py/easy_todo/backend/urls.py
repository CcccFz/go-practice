from django.conf.urls import url, include


urlpatterns = [
    url('^api/todos/', include('todo.urls')),
]
