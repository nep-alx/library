from django.contrib import admin
from .models import *

'''
@admin.register(Loan)
class CopyAmdin(admin.ModelAdmin):
    list_display = ('book', 'loanStart', 'loanDuration', 'student')
'''

for m in [Book, File, Author, Student]:
    admin.site.register(m)