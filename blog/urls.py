from django.contrib import admin
from django.urls import path
from posts.views import task_create, task_update, task_delete, task_search, task_detail
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from users.views import register, user_login, profile_update, delete_profile, profile

urlpatterns = [
    # path('', index, name = "index"),
    path('admin/', admin.site.urls),
    path('task/<int:id>', task_detail, name = "task_detail"),
    path('task/create', task_create, name = "task_create"),
    path('search/', task_search, name = "task_search"),
    path('task/update/<int:id>', task_update, name = "task_update"),
    path('task/delete/<int:id>', task_delete, name = "task_delete"),
    path('user/<int:id>', profile, name = "profile"),
    path('user/update/<int:id>', profile_update, name = "profile_update"),
    path('user/delete/<int:id>', delete_profile, name = "delete_profile"),
    path('', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('logout', LogoutView.as_view(next_page = 'register'), name = "logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)