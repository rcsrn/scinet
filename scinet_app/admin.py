from django.contrib import admin
from .models import Institution
from .models import Generaluser
from .models import Journal
from .models import Publication
from .models import Writes
from .models import Belongs

admin.site.register(Institution)
admin.site.register(Generaluser)
admin.site.register(Journal)
admin.site.register(Publication)
admin.site.register(Writes)
admin.site.register(Belongs)
