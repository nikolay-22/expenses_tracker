from django.urls import path

from expenses_tracker.expenses_app.views import index, profile, edit_profile, delete_profile, create_expense, \
    edit_expense, delete_expense

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('create/', create_expense, name='create_expense'),
    path('edit/<int:pk>', edit_expense, name='edit_expense'),
    path('delete/<int:pk>', delete_expense, name='delete_expense'),
]