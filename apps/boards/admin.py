from django.contrib import admin

from .models import BoardTag
from .models import BoardPost


class BoardTagAdmin(admin.ModelAdmin):
    pass


class BoardPostAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'title', 'weight', 'enabled', 'user',
        'category', 'create_date', 'update_date', 'tag_list'
    ]
    list_editable = ['weight', 'enabled']

    def tag_list(self, obj):
        return ', '.join(obj.tags.all().values_list('title', flat=True))
    tag_list.short_description = 'Теги'


admin.site.register(BoardTag, BoardTagAdmin)
admin.site.register(BoardPost, BoardPostAdmin)