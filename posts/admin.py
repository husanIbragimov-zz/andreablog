from django.contrib import admin
from .models import Tag, Category, Comment, Post


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'category', 'created_at')
    list_filter = ('created_at', 'category', 'tags')
    search_fields = ('title', )
    prepopulated_fields = ({'slug': ('title', )})
    filter_horizontal = ('tags', )
    list_per_page = 8


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'posts', 'name', 'email', 'created_at')


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

