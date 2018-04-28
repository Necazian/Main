from WebSite.settings import BASE_DIR
from .models import Person, Abonent, Admin
from . import logic
import os


def load_image(photo_encode):
    file_name = logic.create_key() + '.jpg'
    f = open(BASE_DIR + '/media/' + file_name, 'wb')
    f.write(photo_encode)
    return BASE_DIR + '/media/' + file_name


def get_abonent_id_by_token(request):
    try:
        return Abonent.objects.get(token=request.POST.get('token')).id
    except:
        try:
            Admin.objects.get(token=request.POST.get('token'))
            return request.POST.get('abonent_id')
        except:
            return None


def create_person(request):
    abonent_id = get_abonent_id_by_token(request)
    if not abonent_id:
        return None
    photo_encode = logic.encode_photo(request)
    photo_url = load_image(photo_encode)
    if not logic.is_only_one(photo_url):
        os.remove(photo_url)
        return None

    person = Person(abonent_id=abonent_id,
                    name=request.POST.get('name'),
                    photo=photo_url)
    person.save()
    return True


def get_all_persons(request):
    abonent_id = get_abonent_id_by_token(request)
    if abonent_id:
        persons = Person.objects.filter(abonent_id=abonent_id)
    else:
        return None

    arr = []
    for p in persons:
        arr.append({'id': p.id, 'name': p.name})
    return {'persons': arr}


def delete_person(request):
    abonent_id = get_abonent_id_by_token(request)
    if not abonent_id:
        return None
    error = True
    for p in Person.objects.filter(abonent_id=abonent_id):
        if str(p.id) == str(request.POST.get('person_id')):
            error = None
    if error:
        return None

    if not error:
        pers = Person.objects.get(id=request.POST.get('person_id'))
        os.remove(pers.photo)
        pers.delete()
    return True


def change_person_photo(request):
    abonent_id = get_abonent_id_by_token(request)
    photo_encode = logic.encode_photo(request)
    photo_url = load_image(photo_encode)
    error = True
    for p in Person.objects.filter(abonent_id=abonent_id):
        if str(p.id) == str(request.POST.get('person_id')):
            error = None
    if not logic.is_only_one(photo_url) or not abonent_id or error:
        os.remove(photo_url)
        return None

    pers = Person.objects.get(id=request.POST.get('person_id'))

    os.remove(pers.photo)
    pers.photo = photo_url
    pers.save()
    return True


def find_persons(request):
    abonent_id = get_abonent_id_by_token(request)
    if not abonent_id:
        return None
    photo_encode = logic.encode_photo(request)
    photo_url = load_image(photo_encode)
    all_persons = Person.objects.filter(abonent_id=abonent_id)
    found_persons = []

    for p in all_persons:
        if logic.on_photo(p.photo, photo_url):
            found_persons.append({'id': p.id, 'name': p.name})

    os.remove(photo_url)
    return {'persons': found_persons}