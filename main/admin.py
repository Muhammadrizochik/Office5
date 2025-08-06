from django.contrib import admin
from django.contrib.auth.models import User, Group

class UserAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class GroupAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)