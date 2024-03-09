from django.db import models


class Story(models.Model):
    title = models.CharField('Название', max_length=250)
    summary = models.CharField('Краткое описание', max_length=250, blank=True)
    content = models.TextField('Текст')

    date_publisher = models.DateTimeField('Дата публикации', auto_now=True)
    publisher = models.BooleanField('Публикация', default=True)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

    def get_absolute_url(self):
        return f'/catalog/{self.id}'

    def __str__(self):
        return self.title
