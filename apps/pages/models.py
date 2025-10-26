from django.db import models

from django.db import models

class Review(models.Model):
    author_name = models.CharField("Имя автора", max_length=100)
    text = models.TextField("Текст отзыва")
    image = models.ImageField("Фотография отзыва/автора", upload_to='reviews/')
    is_published = models.BooleanField("Опубликовать на сайте", default=True)
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author_name}"

class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=255)
    answer = models.TextField("Ответ")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Вопросы-ответы (FAQ)"
        ordering = ['order']

    def __str__(self):
        return self.question