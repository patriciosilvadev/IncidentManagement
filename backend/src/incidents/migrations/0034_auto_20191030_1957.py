# Generated by Django 2.2.6 on 2019-10-30 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0033_auto_20191030_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ('created_date',), 'permissions': (('CAN_CHANGE_ASSIGNEE', 'Can directly change assignee'), ('CAN_REVIEW_INCIDENTS', 'Can review created incidents'), ('CAN_VIEW_REPORTS', 'Can view inciddent reports'), ('CAN_CLOSE_INCIDENT', 'Can close incident'), ('CAN_MANAGE_INCIDENT', 'Can manage incident'), ('CAN_VERIFY_INCIDENT', 'Can verify incident'), ('CAN_RUN_WORKFLOW', 'Can run incident workflows'))},
        ),
    ]
