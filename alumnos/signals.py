from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, post_init
import base64
import os

from .models import User, Alumnos
from django.contrib.auth.models import Group

@receiver(post_save, sender=Alumnos)
def create_user_profile(sender, instance, created, update_fields, **kwargs):
    info = str(instance).split(",")
    if created:
        usuario = User.objects.create_user(username=(info[0] + "_" + info[1][1:]), password=info[2][1:])
        print(info[2][1:])
        usuario.save()
        my_group = Group.objects.get(name='Alumnos') 
        my_group.user_set.add(usuario)
        alumno = Alumnos.objects.get(dni=info[2][1:])
        alumno.user = usuario
        with open(("media/"+str(instance.imagen)), "rb") as img:
            alumno.binario = base64.b64encode(img.read())
        alumno.save()
        os.remove(("media/"+str(instance.imagen)))
        #crear relacion del usuario creado con el alumno. Modificar del instance el campo user y igualarlo al id del usuario creado
    else:
        usuario = User.objects.get(username=instance.user)
        usuario.username = (info[0] + "_" + info[1][1:])
        usuario.save()
        try:
            alumno = Alumnos.objects.get(dni=info[2][1:])
            with open(("media/"+str(instance.imagen)), "rb") as img:
                alumno.binario = base64.b64encode(img.read())
                alumno.save()
                os.remove(("media/"+str(instance.imagen)))
        except:
            pass
        """if os.path.exists("media/"+str(instance.imagen)):
            print (instance.binario)
            os.remove(("media/"+str(instance.imagen)))
        if os.path.exists("media/"+str(instance.imagen)):
            alumno = Alumnos.objects.get(dni=info[2][1:])
            with open(("media/"+str(instance.imagen)), "rb") as img:
                print("segundo open")
                alumno.binario = base64.b64encode(img.read())
                alumno.save()
                os.remove(("media/"+str(instance.imagen)))"""
        """except:
                print("no pudo abrir")"""
    

@receiver(post_delete, sender=Alumnos)
def delete_related_journal(sender, instance, **kwargs):
    info = str(instance).split(",")
    try:
        u = User.objects.get(username =(info[0] + "_" + info[1][1:]))
        u.delete()
    except User.DoesNotExist:
        print("EL USUARIO NO EXISTE POR LO TANTO NO SE PUEDE ELIMINAR")
    except: 
        print("error con usuario")

"""@receiver(post_save, sender=User, dispatch_uid='user.save_user_profile')
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""

# Crear eliminar user profile. Asi, cuando se elimine un alumno, tambien se elimine su respectivo 
i = 0
@receiver(post_init, sender=Alumnos)
def info_upload(sender, instance, **kwargs):
    #print("---> init: ",instance)
    pass