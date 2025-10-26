from django.db import models

class Service(models.Model):

    ICON_CHOICES = [
        ('cleaning_services', 'Веник и совок'),
        ('construction', 'Строительные инструменты'),
        ('diamond', 'Бриллиант (Генеральная уборка)'),
        ('house', 'Дом'),
        ('cottage', 'Коттедж'),
        ('apartment', 'Квартира'),
        ('window', 'Окно'),
        ('chair', 'Кресло (Химчистка)'),
        ('bug_report', 'Жук (Дезинсекция)'),
        ('eco', 'Экология'),
        ('health_and_safety', 'Безопасность'),
    ]
        
    title = models.CharField("Название услуги", max_length=200)
    slug = models.SlugField("URL (автоматически)", max_length=200, unique=True, help_text="Генерируется из названия. Лучше не трогать.")
    short_description = models.TextField("Краткое описание (для карточек на главной)", max_length=300)
    price_display = models.CharField("Отображаемая цена", max_length=100, help_text="Пример: 'от 140 ₽/м²' или 'от 500 ₽'")
    icon = models.CharField("Иконка", max_length=100, default='cleaning_services', help_text="Название иконки с сайта Google Fonts.")

    # Поля для детальной страницы
    hero_image = models.ImageField("Фоновое изображение ('шапка')", upload_to='services/hero/', blank=True, null=True, help_text="Будет фоном на странице этой услуги.")
    full_description = models.TextField("Полное описание услуги", help_text="Основной текст, который будет на странице услуги.")

    # SEO
    meta_title = models.CharField("SEO Title", max_length=255, blank=True, help_text="Если оставить пустым, будет использовано название услуги.")
    meta_description = models.TextField("SEO Description", blank=True, help_text="Краткое описание для поисковиков.")
    
    is_visible = models.BooleanField("Отображать на сайте", default=True)
    order = models.PositiveIntegerField("Порядок сортировки", default=0, help_text="Чем меньше число, тем выше услуга в списке.")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Основные услуги"
        ordering = ['order']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = self.title
        
        if not self.meta_description:
            self.meta_description = self.short_description.strip()

        super().save(*args, **kwargs)

class ServiceChecklistItem(models.Model):
    text = models.CharField("Текст пункта", max_length=255)
    category = models.CharField("Категория (таб)", max_length=100, help_text="Например: 'Жилые комнаты', 'Кухня'")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="checklist_items")

    class Meta:
        verbose_name = "Пункт в чек-листе"
        verbose_name_plural = "Пункты в чек-листах"

    def __str__(self):
        return f"{self.service.title} - {self.text}"

class AdditionalServiceCategory(models.Model):
    title = models.CharField("Название категории доп. услуг", max_length=100)
    order = models.PositiveIntegerField("Порядок сортировки", default=0)

    class Meta:
        verbose_name = "Категория доп. услуг"
        verbose_name_plural = "Категории доп. услуг"
        ordering = ['order']

    def __str__(self):
        return self.title

class AdditionalServiceItem(models.Model):
    title = models.CharField("Название доп. услуги", max_length=200)
    price = models.CharField("Цена", max_length=100)
    category = models.ForeignKey(AdditionalServiceCategory, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"

    def __str__(self):
        return self.title