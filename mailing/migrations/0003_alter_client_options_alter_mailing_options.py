# Generated by Django 4.2.2 on 2024-08-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_client_owner_mailing_owner_message_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': [('watch-list-client', 'Может просматривать список пользователей сервиса.')], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('watch-mailings', 'Может просматривать любые рассылки'), ('deactivate-mailings', 'Может отключять рассылки')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
