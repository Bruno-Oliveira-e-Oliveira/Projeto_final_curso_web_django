# Generated by Django 2.0.7 on 2018-07-14 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_parametros'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentoRot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]
