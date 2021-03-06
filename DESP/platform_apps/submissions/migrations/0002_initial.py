# Generated by Django 3.2.4 on 2021-09-06 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('submissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='last_updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='上次更新者'),
        ),
        migrations.AddField(
            model_name='submission',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization',
                                    verbose_name='机构ID'),
        ),
        migrations.AddField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question',
                                    verbose_name='问题ID'),
        ),
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('question', 'org')},
        ),
    ]
