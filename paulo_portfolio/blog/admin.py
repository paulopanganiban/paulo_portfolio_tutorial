from django.contrib import admin

# Register your models here.
from .models import Category, Post
# EXAMPLE

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['question_text']}),
#                  ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
#     # yung hanging coma ay tuple sa python. research about this
#     inlines = [ChoiceInline]

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)