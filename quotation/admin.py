from django.contrib import admin
from .models import Quotation


class QuotationAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email',
                    )
# Register your models here.


admin.site.register(Quotation, QuotationAdmin)
