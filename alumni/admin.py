from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
alumni, _ = Group.objects.get_or_create(name='alumni')
alumni_ct, _ = ContentType.objects.get_or_create(app_label='auth', model='user')
is_alumnus, _ = Permission.objects.get_or_create(name='is_alumnus', codename='is_alumnus', content_type=alumni_ct)
alumni.permissions.add(is_alumnus)