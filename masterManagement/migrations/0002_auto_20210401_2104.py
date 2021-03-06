# Generated by Django 3.1.7 on 2021-04-01 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='メモ')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memos', to='masterManagement.book', verbose_name='書籍')),
            ],
        ),
        migrations.DeleteModel(
            name='Impression',
        ),
    ]
