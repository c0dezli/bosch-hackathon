# Generated by Django 2.2.3 on 2019-07-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.TextField()),
                ('y', models.TextField()),
                ('z', models.TextField()),
                ('time', models.TextField()),
                ('label', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Message',
            },
        ),
    ]
