# Generated by Django 2.2.2 on 2019-06-09 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choose', '0003_choice_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='event',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
