# Generated by Django 3.0.5 on 2020-11-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id_aula', models.IntegerField(primary_key=True, serialize=False)),
                ('capacidad', models.IntegerField()),
            ],
            options={
                'db_table': 'aula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
                ('horario1', models.CharField(db_column='Horario', max_length=45)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(db_column='Nombres', max_length=45)),
                ('apellidos', models.CharField(db_column='Apellidos', max_length=45)),
                ('telefono', models.IntegerField(db_column='Telefono')),
                ('direccion', models.CharField(db_column='Direccion', max_length=45)),
            ],
            options={
                'db_table': 'docente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id_grupo', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'grupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=45)),
                ('hora_inicio', models.DateField()),
                ('hora_fin', models.DateField()),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario2',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False)),
                ('hora_inicio', models.DateField()),
                ('hora_fin', models.DateField()),
            ],
        ),
    ]
