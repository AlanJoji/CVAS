import os
import face_recognition

def img_load() :

    if not os.path.exists('Images'):
        os.makedirs('Images')
    DIR = r'Images'

    known_face_names = []
    known_face_encodings = []

    for image_file in os.listdir(DIR) :
        image_path = os.path.join(DIR, image_file)
        #print(image_path)

        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]

        known_face_names.append(image_file[:-4])
        known_face_encodings.append(encoding)

    return(known_face_names, known_face_encodings)
