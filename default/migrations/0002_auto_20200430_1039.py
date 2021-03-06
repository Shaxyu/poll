# Generated by Django 2.2.12 on 2020-04-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='count',
            field=models.IntegerField(default=0, verbose_name='票數'),
        ),
        migrations.AlterField(
            model_name='option',
            name='poll_id',
            field=models.IntegerField(verbose_name='所屬投票主題'),
        ),
        migrations.AlterField(
            model_name='option',
            name='title',
            field=models.CharField(max_length=100, verbose_name='選項文字'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='建立時間'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='desc',
            field=models.TextField(max_length=512, verbose_name='說明'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=100, verbose_name='投票主題'),
        ),
    ]
