from email.headerregistry import Group
from django.contrib import admin
from .models import Books, Song


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['b_name']
admin.site.register(Books,BookAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display=['s_name']
admin.site.register(Song,SongAdmin)





