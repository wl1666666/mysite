# Generated by Django 2.2 on 2019-04-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='在这里写影片的描述', max_length=100)),
                ('image', models.ImageField(default='default.gif', upload_to='images/')),
                ('director', models.CharField(default='这里写影片的导演', max_length=100)),
                ('title', models.CharField(default='影片标题', max_length=50)),
            ],
        ),
    ]
