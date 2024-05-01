from django.contrib import admin

from silantaccountsapp.models import (
    SilantUser, SilantRolesAccess,SilantClients,
    SilantManagers, SilantServiveCompanies
)

admin.site.register(SilantUser)
admin.site.register(SilantRolesAccess)
admin.site.register(SilantClients)
admin.site.register(SilantManagers)
admin.site.register(SilantServiveCompanies)
