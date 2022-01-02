from django.contrib import admin
from .models import CustomUser

# https://dev-yakuza.posstree.com/ko/django/admin/

class TicketAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(CustomUser,TicketAdmin)

# https://pypi.org/project/django-admin-view-permission/

# https://stackoverflow.com/questions/45837617/django-admin-wont-allow-me-to-modify-user-permissions-and-groups
# https://github.com/search?l=Python&q=filter_horizontal+user_permissions&type=Code