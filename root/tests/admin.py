from django.contrib import admin
from .models import Test, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionInline(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Register your models here.
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
