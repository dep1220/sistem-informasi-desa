# Generated by Django 5.2.4 on 2025-07-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('nik', models.CharField(help_text='Nomor Induk Kependudukan', max_length=16, unique=True)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('agama', models.CharField(max_length=50)),
                ('pekerjaan', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('tanggal_dibuat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Warga',
                'verbose_name_plural': 'Data Warga',
            },
        ),
    ]
