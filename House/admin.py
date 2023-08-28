from django.contrib import admin
from .models import houses
# from .models import post

class housesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(houses, housesAdmin)
# admin.site.register(post)