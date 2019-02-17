from django.contrib import admin
from .models import Question,Choice,Join,Events,Users,Locations
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Join)
admin.site.register(Events)
admin.site.register(Users)
admin.site.register(Locations)
