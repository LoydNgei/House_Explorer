# Generated by Django 4.2.2 on 2023-08-02 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('House', '0005_houses_is_featured'),
    # ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='House.houses')),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
