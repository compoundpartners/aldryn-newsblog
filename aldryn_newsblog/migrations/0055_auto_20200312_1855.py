# Generated by Django 2.2.10 on 2020-03-12 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0054_auto_20200219_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletranslation',
            name='author_2_trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='aldryn_people.Person', verbose_name='second author'),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='author_3_trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='aldryn_people.Person', verbose_name='third author'),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='author_trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='aldryn_people.Person', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='is_featured_trans',
            field=models.BooleanField(db_index=True, default=False, verbose_name='is featured'),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='is_published_trans',
            field=models.BooleanField(db_index=True, default=False, verbose_name='is published'),
        ),
    ]
