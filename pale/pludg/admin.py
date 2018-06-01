from django.contrib import admin

# Register your models here.

from . import models

class NewsModalAdmin(admin.ModelAdmin):
    pass

class ObjectAdmin(admin.ModelAdmin):
    model = models.Object
    list_display = ['name', 'get_name', ]

    def get_name(self, obj):
        return obj.category
    get_name.admin_order_field  = 'author'  #Allows column order sorting
    get_name.short_description = 'Author Name'  #Renames column head

    #Filtering on side - for some reason, this works
    #list_filter = ['title', 'author__name']

class ObjectImageAdmin(admin.ModelAdmin):
    model = models.Object
    list_display = ['name']

class NewsArticleAdmin(admin.ModelAdmin):
    model = models.Object
    list_display = ['headline', 'date', ]





admin.site.register(models.NewsArticle, NewsArticleAdmin)
admin.site.register(models.Object, ObjectAdmin)
admin.site.register(models.ObjectImage, ObjectImageAdmin)