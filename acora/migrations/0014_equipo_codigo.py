# Generated by Django 2.2 on 2019-04-30 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0013_remove_equipo_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='codigo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acora.Partida'),
        ),
    ]
