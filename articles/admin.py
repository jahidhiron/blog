from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline): 
    model = Comment
    # how many shows. it's optional. if we don't mantion, by default 3
    extra = 1



class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)