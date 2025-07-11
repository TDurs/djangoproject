# Generated by Django 5.2 on 2025-07-02 23:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_almacenlibros_datecompleted_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacenlibros',
            name='critica_de_internet',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='Calificación del 1 al 10'),
        ),
        migrations.CreateModel(
            name='LibroFavorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado_en', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.almacenlibros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'libro')},
            },
        ),
    ]
