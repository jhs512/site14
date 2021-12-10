from django.contrib import admin

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'subject']
    search_fields = ['subject', 'content']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'question_id', 'content']

admin.site.register(Answer, AnswerAdmin)