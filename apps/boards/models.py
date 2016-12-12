from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PublicationAbstractModel(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    weight = models.PositiveIntegerField(
        'Вес',
        help_text='Чем больше, тем приоритетнее',
        default=100)
    enabled = models.BooleanField('Включен', default=True)

    class Meta:
        abstract = True
        ordering = ['-weight']

    def __str__(self):
        return self.title


class BoardTag(PublicationAbstractModel):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class BoardPost(PublicationAbstractModel):

    class CATEGORIES:
        SALE = 'sale'
        BUY = 'buy'

        CHOICES = (
            (SALE, 'Продажа'),
            (BUY, 'Покупка'),
        )

    user = models.ForeignKey(User, verbose_name='Пользователь')
    tags = models.ManyToManyField(BoardTag, verbose_name='Теги', related_name="tags")
    category = models.CharField(
        'Категория', max_length=4,
        choices=CATEGORIES.CHOICES,
    )
    text = models.TextField('Текст')
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'
        ordering = ['-weight', '-create_date']

    def __str__(self):
        return '{}: {}'.format(self.get_category_display(), self.title)

    def get_absolute_url(self):
        return reverse('post_update', args=(self.id,))
