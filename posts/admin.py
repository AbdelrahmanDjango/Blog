from django.contrib import admin
from .models import Post, Comment
from django.utils.translation import gettext_lazy
from polymorphic_tree.admin import PolymorphicMPTTParentModelAdmin, PolymorphicMPTTChildModelAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_filter = ['title', 'created_at', 'updated_at', 'publish']
    search_fields = ['title', 'body']
    ordering = ['publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_at', 'active']
    list_filter =  ['created_at', 'updated_at', 'active']

