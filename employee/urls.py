from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path('view_emp',view_emp),
    path("add_emp",add_emp),
    path("remove_emp",remove_emp),
    path("remove_emp/<int:emp_id>/",remove_emp),
    path("update_emp",update_emp),
    path("update_emp/<int:emp_id>/",update_emp),
    path("search_emp",search_emp)
    
]
