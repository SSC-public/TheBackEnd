from django.contrib import admin
from .models import TranslatedText, DocumentTest
from django.contrib.admin import widgets
from martor.widgets import AdminMartorWidget
from django.db import models
from django_reverse_admin import ReverseModelAdmin, ReverseInlineModelAdmin


class TranslatedTextInlineSmall(ReverseInlineModelAdmin):
    model = TranslatedText
    formfield_overrides = {
        models.TextField: {'widget': widgets.AdminTextInputWidget},

    }


class TranslatedTextInlineLarge(ReverseInlineModelAdmin):
    model = TranslatedText
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(TranslatedText)
class TranslatedTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(DocumentTest)
class DocumentTestAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    inline_reverse = [
        {
            'field_name': 'title',
            'kwargs': {},
            'admin_class': TranslatedTextInlineSmall
        },
        {
            'field_name': 'description',
            'kwargs': {},
            'admin_class': TranslatedTextInlineLarge
        },
    ]
