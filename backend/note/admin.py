from django.contrib import admin
from note.models import Note, Tag

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('tags',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'author')
    search_fields = ('name','author__username' )
