from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Other URL patterns...
    path('',views.signup_view,name='signup_view'),
    path('create-expense/', views.create_expense, name='create_expense'),
    path('login/', views.login_view, name="login_view"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('view-expenses/', views.view_expenses, name='view_expenses'),
    path('edit-expense/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
