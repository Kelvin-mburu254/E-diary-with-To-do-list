from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('user_login', views.user_login, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('manageCategory', views.manageCategory, name='manageCategory'),
    path('editCategory/<int:pid>', views.editCategory, name='editCategory'),
    path('deleteCategory/<int:pid>', views.deleteCategory, name='deleteCategory'),
    path('manageNotes', views.manageNotes, name='manageNotes'),
    path('editNotes/<int:pid>', views.editNotes, name='editNotes'),
    path('viewNotes/<int:pid>', views.viewNotes, name='viewNotes'),
    path('deleteNotesHistory/<int:pid>', views.deleteNotesHistory, name='deleteNotesHistory'),
    path('deleteNotes/<int:pid>', views.deleteNotes, name='deleteNotes'),
    path('searchNotes', views.searchNotes, name='searchNotes'),
    path('profile', views.profile, name='profile'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('logout/', views.Logout, name='logout'),
    path('reminder/', include('reminder.urls')),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)