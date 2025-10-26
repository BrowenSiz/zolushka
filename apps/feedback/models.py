from django.db import models

from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('closed', 'Закрыта'),
    )
    name = models.CharField("Имя клиента", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    message = models.TextField("Сообщение (детали заявки)", blank=True)
    status = models.CharField("Статус заявки", max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField("Дата и время", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка с сайта"
        verbose_name_plural = "Заявки с сайта"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.name} ({self.phone})"