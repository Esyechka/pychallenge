from django.contrib import admin
from pychallenge.articles.models import Article, Links


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    list_filter = ('user', 'status', 'timestamp')

@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'article')