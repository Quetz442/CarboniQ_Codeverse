"""
URL configuration for CarboniQ_Codeverse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mviews
from authapp import views as aviews

urlpatterns = [
    path('admin/', admin.site.urls),
]


mainappurl = [
path('homepage/', mviews.homepage, name='homepage'),
]

authappurl = [
    path('', aviews.landingpage, name="landingpage"),
    path('home/', aviews.landingpage, name='home'),
    path('login/', aviews.loginpage, name='login'), 
    path('signup/', aviews.signuppage, name="signup"),
    path('view_profile/<int:user_id>/', aviews.view_profile, name='view_profile'),
    path('edit_profile/<int:user_id>/', aviews.edit_profile, name='edit_profile'),
    path('logout/', aviews.user_logout, name='logout'),
    path('avatar_selection/', aviews.avatar_selection, name='avatar_selection'),
    path('update-avatar/', aviews.update_avatar, name='update_avatar'),
    path('add_friend/<int:user_id>/', aviews.add_friend, name='add_friend'),
    path('friends_list/', aviews.friends_list, name='friends_list'),
    path('accept_request/<int:request_id>/', aviews.accept_request, name='accept_request'),
    path('decline_request/<int:request_id>/', aviews.decline_request, name='decline_request'),
    path('search/', aviews.search_users, name='search_users'),
]



urlpatterns = mainappurl + authappurl + urlpatterns