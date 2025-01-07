from django.contrib import admin

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
students, _ = Group.objects.get_or_create(name='students')
students_ct, _ = ContentType.objects.get_or_create(app_label='auth', model='User')
is_student, _ = Permission.objects.get_or_create(name='is_student', codename='is_student', content_type=students_ct)
students.permissions.add(is_student)