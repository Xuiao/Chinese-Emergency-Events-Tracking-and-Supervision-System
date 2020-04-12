from django.contrib import admin

from crawler.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'time', 'get_read_num', 'content')


