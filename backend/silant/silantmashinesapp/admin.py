from django.contrib import admin

from silantmashinesapp.models import (
    Mashine, Maintence, Complaints
)

admin.site.register(Mashine)
admin.site.register(Maintence)
admin.site.register(Complaints)