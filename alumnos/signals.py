from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import User, Alumnos
from django.contrib.auth.models import Group

@receiver(post_save, sender=Alumnos)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        info = str(instance).split(",")
        usuario = User.objects.create_user(username=(info[0] + "_" + info[1][1:]), password=info[2][1:])
        usuario.save()
        my_group = Group.objects.get(name='Alumnos') 
        my_group.user_set.add(usuario)
        alumno = Alumnos.objects.get(dni=info[2][1:])
        alumno.user = usuario
        print(bytes(bytearray(instance.archivo)))
        alumno.foto = bytes(bytearray(instance.archivo))
        alumno.save()
        #crear relacion del usuario creado con el alumno. Modificar del instance el campo user y igualarlo al id del usuario creado

"""@receiver(post_save, sender=User, dispatch_uid='user.save_user_profile')
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""