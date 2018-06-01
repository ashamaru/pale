from django.db import models

# Create your models here.


class NewsArticle(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(verbose_name='Überschrift', max_length=200)
    date = models.DateTimeField(verbose_name='Datum')
    start_tp = models.DateTimeField(verbose_name='Start Zeitpunkt')
    end_tp = models.DateTimeField(verbose_name='End Zeitpunkt')
    short_desc = models.TextField(verbose_name='Beschreibung')
    content = models.TextField(verbose_name='Inhalt')

    class Meta:
        verbose_name = "News Artikel"
        verbose_name_plural = "News Artikel"


class Object(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    category = models.CharField(verbose_name='Kategorie', max_length=100, default='Gewerbeimmobilie')
    location = models.CharField(verbose_name='Ort', max_length=100, default='Germany')
    short_desc = models.TextField(verbose_name='Kurzbeschreibung')
    description = models.TextField(verbose_name='Beschreibung')
    info_overview = models.TextField(verbose_name='Info Übersicht')
    images_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Objekt"
        verbose_name_plural = "Objekte"


class ObjectImage(models.Model):
    name = models.CharField(max_length=100, default='unnamed')
    category = models.CharField(max_length=100, default='none')
    object = models.ForeignKey('Object', on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = "Bild"
        verbose_name_plural = "Bilder"