# Generated by Django 4.2.6 on 2023-10-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0006_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default='<empty_text>', max_length=4096),
        ),
    ]
