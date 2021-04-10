from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
urlpatterns = [
    # path('', views.navbar, name = "navbar"),
    path('',views.index,name='Index'),
    path('my-profile/',views.my_profile, name='my-profile'),
    path('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    path('create/profile',views.create_profile, name='create-profile'),
    
    path('update/profile',views.update_profile, name='update-profile'),
    path('blog/',views.blog, name='blog'),
    path('new/blogpost',views.new_blogpost, name='new-blogpost'), 
    path('view/blog/(\d+)',views.view_blog,name='view_blog'),
    path('business',views.businesses, name='business'),
    path('new/business',views.new_business, name='new-business'),
    path('health',views.health, name='health'),
    path('authorities',views.authorities, name='authorities'),
    path('notifications',views.notification, name='notifications'),
    path('new/notification',views.new_notification, name='new-notification'),
    path('search/',views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)