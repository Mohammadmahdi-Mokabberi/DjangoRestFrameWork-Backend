from django.contrib import admin
from .models import AboutModel, AlbumModel, ImageModel, StoryModel, VideoModel



class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'birthday']
    list_display_link = ['id']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'published']
    list_display_link = ['id']
    list_editable = ['name', 'published']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_linke = ['id']
    list_editable = ['name']


class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_display_link = ['id']
    list_editable = ['name', 'published']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_display_link = ['id']
    list_editable = ['name', 'published']
###########################################
admin.site.register(AboutModel, AboutAdmin)
admin.site.register(AlbumModel, AlbumAdmin)
admin.site.register(ImageModel, ImageAdmin)
admin.site.register(StoryModel, StoryAdmin)
admin.site.register(VideoModel, VideoAdmin)