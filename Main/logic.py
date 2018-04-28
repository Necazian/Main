import hashlib
import time

import face_recognition


def on_photo(first_photo_url, second_photo_url):
    first_photo = face_recognition.load_image_file(first_photo_url)
    second_photo = face_recognition.load_image_file(second_photo_url)

    first_face_locations = face_recognition.face_locations(first_photo)
    first_encoding = face_recognition.face_encodings(first_photo, first_face_locations)[0]

    second_face_locations = face_recognition.face_locations(second_photo)

    for second_encoding in face_recognition.face_encodings(second_photo, second_face_locations):
        if face_recognition.compare_faces([first_encoding], second_encoding)[0]:
            return True
    return False


def is_only_one(photo_url):
    photo = face_recognition.load_image_file(photo_url)
    if len(face_recognition.face_encodings(photo)) == 1:
        return True
    return False


def encode_photo(request):
    photo = request.FILES['photo'].read()
    return photo


def create_key():
    return str(hashlib.sha1(str(round(time.time() * 1000)).encode('utf-8')).hexdigest())