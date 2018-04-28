from .models import Abonent, Admin
from . import logic


def login(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    token = None
    try:
        a = Abonent.objects.get(login = login, password = password)
        a.token = token = logic.create_key()
        a.save()
    except:
        try:
            a = Admin.objects.get(login=login, password=password)
            a.token = token = logic.create_key()
            a.save()
        except:
            return None
    return {'token': token}


def logout(request):
    try:
        a = Abonent.objects.get(token = request.POST.get('token'))
        a.token = ""
        a.save()
    except:
        try:
            a = Admin.objects.get(token=request.POST.get('token'))
            a.token = ""
            a.save()
        except:
            return None
    return True