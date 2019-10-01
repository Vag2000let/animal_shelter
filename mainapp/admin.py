from django.contrib import admin

from .models import (
    Picture, Category, PetGender, PetSize, PetWool, PetColor, PetCharacter, Pet
)


class PictureInline(admin.TabularInline):
    """ Класс для нескольких изображений на каждый объект """
    model = Picture
    fk_name = 'related_obj'


@admin.register(Pet)
class ProductAdmin(admin.ModelAdmin):
    """ Набор изображений для отдельно взятого питомца """
    inlines = (PictureInline,)


admin.site.register(Category)
admin.site.register(PetGender)
admin.site.register(PetSize)
admin.site.register(PetWool)
admin.site.register(PetColor)
admin.site.register(PetCharacter)
