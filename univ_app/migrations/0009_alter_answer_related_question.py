# Generated by Django 4.0.5 on 2022-08-19 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('univ_app', '0008_alter_question_question_alter_question_related_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='univ_app.question'),
        ),
    ]
