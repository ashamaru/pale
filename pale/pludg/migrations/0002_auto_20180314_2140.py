# Generated by Django 2.0 on 2018-03-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pludg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'verbose_name': 'News Artikel'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Objekte'},
        ),
        migrations.AlterModelOptions(
            name='objectimage',
            options={'verbose_name': 'Bilder'},
        ),
        migrations.AddField(
            model_name='objectimage',
            name='name',
            field=models.CharField(default='unnamed', max_length=100),
        ),
    ]