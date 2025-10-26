from django.db import models

from django.db import models

class SiteConfiguration(models.Model):
    phone_number = models.CharField("Основной номер телефона", max_length=20)
    work_hours = models.CharField("Часы работы", max_length=100)
    email = models.EmailField("Email для связи")
    vk_link = models.URLField("Ссылка на ВКонтакте", blank=True)
    instagram_link = models.URLField("Ссылка на Instagram", blank=True)
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"