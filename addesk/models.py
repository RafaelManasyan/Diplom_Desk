from django.conf import settings
from django.db import models


class Advert(models.Model):
    """Модель объявления, содержащая информацию о товаре, его цене,
    описании, авторе и дате создания.
    """
    title = models.CharField(verbose_name='название товара', max_length=255)
    price = models.IntegerField(verbose_name='цена товара', default=0)
    description = models.TextField(verbose_name='описание товара')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор объявления', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='время и дата создания объявления', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title


class Review(models.Model):
    """Модель отзыва, связывающего пользователя с объявлением.
    Содержит текст отзыва, автора и дату создания.
    """
    text = models.TextField(verbose_name='текст отзыва', max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор отзыва', on_delete=models.CASCADE)
    advert = models.ForeignKey('Advert', verbose_name='комментируемое объявление', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='время и дата создания отзыва', auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return f'{self.author} Дата и время: {self.created_at}'
