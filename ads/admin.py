from django.contrib import admin
from .models import VehicleModel
from .models import Piece
from .models import Matter
from .models import Ad
from .models import Color
from .models import Picture
from .models import Brand
from .models import Category

admin.site.register(VehicleModel)
admin.site.register(Piece)
admin.site.register(Matter)
admin.site.register(Ad)
admin.site.register(Color)
admin.site.register(Picture)
admin.site.register(Brand)
admin.site.register(Category)
