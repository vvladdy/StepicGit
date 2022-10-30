from django.contrib import admin

from .models import Car, CarModel, CarMarka

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','phone', 'url', 'public_date')
    list_filter = ('price', 'public_date') # фильтр для отображения элементов в
    # админке

class CarModelBlock(admin.ModelAdmin):
    list_display = ('car_model', )

class CarMarkaBlock(admin.ModelAdmin):
    list_display = ('car_marka', )

admin.site.register(CarModel, CarModelBlock)
admin.site.register(CarMarka, CarMarkaBlock)





