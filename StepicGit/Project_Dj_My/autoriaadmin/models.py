from django.db import models

class CarModel(models.Model):

    car_model = models.CharField(
        max_length=250,
        verbose_name='Модель автомобиля',
        unique=True
    )

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модель авто'


class CarMarka(models.Model):
    car_marka = models.CharField(
        max_length=250,
        verbose_name='Марка автомобиля',
        unique=True
    )

    car = models.ForeignKey(CarModel,  # задается название
                            # класса зависимости
                            on_delete=models.CASCADE,
                            related_name='модели',
                            verbose_name='таблица моделей')

    def __str__(self):
        return self.car_marka


    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марка авто'


class Car(models.Model):

    title = models.CharField(
        max_length=250,
        verbose_name='Модель автомобиля из названия в авториа',
        null=True
    )

    price = models.CharField(
        max_length=250,
        verbose_name='цена автомобиля',
        null=True
    )

    currency = models.CharField(
        max_length=100,
        verbose_name='Валюта',
        null=True
    )

    miles = models.CharField(
        max_length=250,
        verbose_name='пробег автомобиля',
        null=True
    )

    phone = models.CharField(
        max_length=250,
        verbose_name='Номер телефона',
        null=True
    )

    url = models.URLField(
        verbose_name='Ссылка на объявление',
        null=True
    )

    public_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    car_info_marka = models.ForeignKey(CarMarka,
                              on_delete=models.CASCADE,
                              related_name='марки',
                              verbose_name='таблица марок авто')

    car_info_model = models.ManyToManyField(CarModel,
                                            related_name='models')

    def __str__(self):
        return self.title


    # для того, чтобы в админке название было не из названия класса Cars,
    # а так, как мне удобно "Автомобили"
    class Meta:
        verbose_name = 'Автомобили'
        verbose_name_plural = 'Автомобили'
