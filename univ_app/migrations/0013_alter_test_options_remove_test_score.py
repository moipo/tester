# Generated by Django 4.1.1 on 2022-09-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ_app', '0012_alter_answer_related_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={},
        ),
        migrations.RemoveField(
            model_name='test',
            name='score',
        ),
    ]
