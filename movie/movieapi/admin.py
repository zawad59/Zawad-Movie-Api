from django.contrib import admin

#registering models into admin

from .models import Details
from .models import Comments
admin.site.register(Comments)
admin.site.register(Details)
