from django.urls import include, path

import users
import customer
import credits
import calls
import supports

urlpatterns = [
    path(r'users/', include('users.urls', namespace='users')),
    path(r'customer/', include('customer.urls', namespace='customer')),
    path(r'credits/', include('credits.urls', namespace='credits')),
    path(r'calls/', include('calls.urls', namespace='calls')),
    path(r'supports/', include('supports.urls', namespace='supports')),
]
