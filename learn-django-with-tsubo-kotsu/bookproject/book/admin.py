from django.contrib import admin
from .models import Book,Review
#from .models import SampleModel

#admin.site.register(SampleModel)
admin.site.register(Book)
admin.site.register(Review)