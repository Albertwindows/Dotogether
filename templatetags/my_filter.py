from django import template
from django.utils.safestring import mark_safe
from polls import models
register = template.Library()


@register.filter
def indexof(l,i):
    return l[i]

@register.filter
def oror(f1,f2):
    return f1 or f2

@register.filter
def same(f1,f2):
    return f1 or f2

@register.filter
def haveJoined(user_id,evnet_id):
    join=models.Join.objects.filter(user_id=user_id,event_id=evnet_id)
    if len(join)>0:
        return True
    return False
