from django.contrib import admin
from core.models import Applicant

from django.db.models.functions import Lower, Upper
from import_export.admin import ExportActionMixin

@admin.register(Applicant)
class UniversalAdmin(ExportActionMixin, admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def get_ordering(self, request):
        return [Upper("fbUrl")]  # sort case insensitive
