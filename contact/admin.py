from django.contrib import admin
from .models import GetInTouch, Subscribe


class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'created_at')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(GetInTouch, GetInTouchAdmin)
admin.site.register(Subscribe, SubscribeAdmin)

