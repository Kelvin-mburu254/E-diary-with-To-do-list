from django.urls import path
from reminder import reminder_views

app_name = 'reminder'

urlpatterns = [
    # urls for template
    path('', reminder_views.ReminderList.as_view(), name='tasks'),
    path('task/add/', reminder_views.ReminderCreate.as_view(), name='task_add'),
    path('task-update/<int:pk>/',
         reminder_views.ReminderUpdate.as_view(), name='task_update'),
    path('task/assign/', reminder_views.ReminderAssign.as_view(), name='task_assign'),
    path('task/<int:pk>/delete/',
         reminder_views.ReminderDelete.as_view(), name='task_delete'),
    path('task/<int:pk>/finish/',
         reminder_views.finish_task, name='finish_task'),
    # urls for API
    path('api/', reminder_views.ReminderListAPI.as_view()),
    path('api/<int:pk>/', reminder_views.ReminderDetailAPI.as_view()),
    path('api/add/', reminder_views.ReminderCreateAPI.as_view()),
    path('api/<int:pk>/finish/', reminder_views.finish_task_API),
]
