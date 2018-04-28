from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render


@csrf_exempt
def index(request):
    from . import person
    from . import abonent
    from . import admin

    response = None
    if request.method == 'POST':
        # about person
        if request.POST.get("method") == "create_person" and request.POST.get('token'):
            response = person.create_person(request)

        if request.POST.get("method") == "get_all_persons" and request.POST.get('token'):
            response = person.get_all_persons(request)

        if request.POST.get("method") == "delete_person" and request.POST.get('token'):
            response = person.delete_person(request)

        if request.POST.get("method") == "change_person_photo" and request.POST.get('token'):
            response = person.change_person_photo(request)

        if request.POST.get("method") == "find_persons" and request.POST.get('token'):
            response = person.find_persons(request)
        # about abonent/admin
        if request.POST.get('login') and request.POST.get('password'):
            if request.POST["method"] == "login":
                response = abonent.login(request)

        if request.POST.get("method") == "logout" and request.POST.get('token'):
            response = abonent.logout(request)
        # about admin
        if request.POST.get('login') and request.POST.get('password'):
            if request.POST["method"] == "register_abonent":
                response = admin.register_abonent(request)

        if request.POST.get("method") == "delete_abonent" and request.POST.get('token'):
            response = admin.delete_abonent(request)

        if request.POST.get("method") == "get_all_abonents" and request.POST.get('token'):
            response = admin.get_all_abonents(request)

    return JsonResponse(response, safe=False)

def test(request):
    return render(request, 'Main/test.html')
















