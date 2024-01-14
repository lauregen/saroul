from django.db import models
from django.core.validators import RegexValidator


register_validator = RegexValidator(
    r"[A-HJ-NP-TV-Z]{2}[\s-]{0,1}[0-9]{3}[\s-]{0,1}[A-HJ-NP-TV-Z]{2}|[0-9]{2,4}[\s-]{0,1}[A-Z]{1,3}[\s-]{0,1}[0-9]{2}",
    "Your string should contain letter A in it."
)


class Category(models.Model):

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    name = models.CharField(max_length=300, null=True, verbose_name="name")

    def __str__(self):
        return self.name



class Brand(models.Model):

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    name = models.CharField(max_length=300, null=True, verbose_name="name")

    BRAND_TYPES = [
        ("V", "vehicle"),
        ("P", "Piece"),

    ]
    name = models.CharField(max_length=60)
    brand_type = models.CharField(max_length=1, choices=BRAND_TYPES)


    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    class Meta:
        verbose_name = ("vehiclemodel")
        verbose_name_plural = ("vehiclemodels")

    model = models.TextField(max_length=300, null=True, verbose_name="model")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='vehicles')
    registration_number = models.CharField(max_length=300, verbose_name="registration_number",
                                           validators=[register_validator], blank=True, null=True)
    year = models.CharField(max_length=4, null=True, verbose_name="year")
    TYPE = (
        ('CTD', 'Citadine'),
        ('BLN', 'Berline'),
        ('SUV', 'SUV'),
        ('4x4', '4*4'),
        ('PKP', 'Pick-up'),
        ('VE', 'VE'),
        ('VH', 'VH')

    )
    type = models.CharField(max_length=200, null=True, choices=TYPE)

    def __str__(self):
        return f"{self.brand} {self.model}"

        if self.year:
            return self.model + ' (' + self.year + ')'
        else:
            return self.model

class Piece(models.Model):

    class Meta:
        verbose_name =("piece")
        verbose_name_plural =("pieces")

    vehicles = models.ManyToManyField(VehicleModel, through='Ad', blank=True, null=True)
    references = models.CharField(max_length=300, null=True, verbose_name="references")
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="width")
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="length")
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="height")
    category = models.ForeignKey(Category, on_delete= models.PROTECT, related_name= 'pieces')


    def __str__(self):
        return self.references






class Ad(models.Model):
    class Meta:
        verbose_name = ("ad")
        verbose_name_plural = ("ads")

    name = models.CharField(max_length=300, null=True, verbose_name="name")
    title = models.CharField(max_length=300, null=True, verbose_name="title")
    description = models.CharField(max_length=2000, null=True, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    piece = models.ForeignKey(Piece, on_delete=models.PROTECT, blank=True, null=True)
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.PROTECT, blank=True, null=True)




class Color(models.Model):

    class Meta:
        verbose_name =("color")
        verbose_name_plural =("colors")

    name = models.CharField(max_length=300, null=True, verbose_name="name")

    def __str__(self):
        return self.name

class Matter(models.Model):

    class Meta:
        verbose_name =("matter")
        verbose_name_plural =("matters")

    matter = models.CharField(max_length=2000, null=True, verbose_name="matter")
    colors = models.ManyToManyField('Color')

    def __str__(self):
        return self.matter

class Picture(models.Model):
    class Meta:
        verbose_name = "picture"
        verbose_name_plural = "pictures"

    picture = models.ImageField(upload_to='images/' ,null=True, blank=True)
    ad = models.ForeignKey(Ad, models.DO_NOTHING, verbose_name='images')
    filename = models.TextField(blank=True, null=True)



