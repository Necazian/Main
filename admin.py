from django.contrib import admin
from .models import Abonent, Person, Admin
from Main import logic

admin.site.register(Person)
admin.site.register(Abonent)
admin.site.register(Admin)


def login_is_unique(login):
    for a in Abonent.objects.all():
        if login == a.login:
            return False
    for a in Admin.objects.all():
        if login == a.login:
            return False
    return True


def is_admin(request):
    try:
        Admin.objects.get(token=request.POST.get('token'))
        return True
    except:
        return False


def register_abonent(request):
    if is_admin:
        if login_is_unique(request.POST.get('login')):
            token = logic.create_key()
            abonent = Abonent(login = request.POST.get('login'),
                              password = request.POST.get('password'),
                              token = token)
            abonent.save()
            return {'token': token}
    return None


def delete_abonent(request):
    if is_admin:
        try:
            abon = Abonent.objects.get(id=request.POST.get('abonent_id'))
        except:
            return None
        persons = Person.objects.filter(abonent_id=abon.id)
        for p in persons:
            pers = Person.objects.get(id=p.id)
            import os
            os.remove(pers.photo)
            pers.delete()
        abon.delete()
        return True
    return None


def get_all_abonents(request):
    if is_admin:
        abonents = []
        for a in Abonent.objects.all():
            abon = {}
            abon['id'] = a.id
            abon['login'] = a.login
            abon['password'] = a.password
            abon['token'] = a.token
            abonents.append(abon)
        return {'abonents': abonents}
    return None
