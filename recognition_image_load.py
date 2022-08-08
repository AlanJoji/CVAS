import os
import face_recognition

def img_load() :
    DIR = r'Images'

    if not os.path.exists(DIR):
        os.makedirs(DIR)

    known_face_names = []
    known_face_encodings = []

    no_of_files = len(os.listdir(DIR))

    if (no_of_files > 0) :
        for image_file in os.listdir(DIR) :
            image_path = os.path.join(DIR, image_file)

            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]

            known_face_names.append(image_file[:-4])
            known_face_encodings.append(encoding)
    else :
        quit()

    return(known_face_names, known_face_encodings)
