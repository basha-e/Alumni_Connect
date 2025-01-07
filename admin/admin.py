from django.contrib import admin
from .models import Event
# Register your models here.
admin.site.register(Event)

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

admins, _ = Group.objects.get_or_create(name='admins')
admins_ct = ContentType.objects.get(app_label='auth', model='user')
is_admin, _ = Permission.objects.get_or_create(name='is_admin', codename='is_admin', content_type=admins_ct)
admins.permissions.add(is_admin)
is_admin.save()
admin,_ = User.objects.get_or_create(username='admin')
admin.set_password('root')
admin.groups.add(admins)
admin.save()
admin.has_perm('auth.is_admin')