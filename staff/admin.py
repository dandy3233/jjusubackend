from django.contrib import admin
from .models import StaffMember, ImageCollage

class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'image')
    search_fields = ('name', 'role')

class ImageCollageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    search_fields = ('title',)

admin.site.register(StaffMember, StaffMemberAdmin)
admin.site.register(ImageCollage, ImageCollageAdmin)