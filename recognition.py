import face_recognition
import cv2 as cv
import numpy as nump
import csv
import recognition_image_load as recog_img_load
import recognition_time as recog_time

known_face_names, known_face_encodings = recog_img_load.img_load()
 
students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

current_date = recog_time.curr_date()

file_name = current_date + ".csv"

file = open(file_name, "w+", newline="")
writer = csv.writer(file)

video_capture = cv.VideoCapture(0)

while True :
    _, frame = video_capture.read()
    small_frame = cv.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:,:,::-1]

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        print(face_locations)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings :
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = nump.argmin(face_distance)


            if (matches[best_match_index]) :
                name = known_face_names[best_match_index]

            face_names.append(name)

            if (name in known_face_names) :
                if (name in students) :
                    students.remove(name)
                    current_time = recog_time.curr_time()
                    writer.writerow([name, current_time])
    
    

       

        if(len(face_locations)!=0):
            face_loc = face_locations[0]
            x1,y1,x2,y2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            x1,y1,x2,y2 = 4*x1, 4*y1, 4*x2, 4*y2

            cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),thickness = 2)
            cv.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv.FILLED)

            cv.putText(frame, str(name), (x1+6,y2-6), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), thickness = 2)
        
    cv.imshow("Attendance System", frame)
    
    if (cv.waitKey(1) & 0xFF == ord('q')) :
        break

video_capture.release()
cv.destroyAllWindows()
file.close()    



