from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# make post manageable in administration
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # add table with headings to posts overview
    list_display = ('title', 'slug', 'status', 'created_on')
    # add search bar
    search_fields = ['title', 'content']
    # slug automatically is created from title
    prepopulated_fields = {'slug': ('title',)}
    # add filter to posts overview
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    # add action to table overview additional to delete
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
