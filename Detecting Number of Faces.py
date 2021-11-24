import cv2 as cv

## Assigned video in cap
cap = cv.VideoCapture('faces.mp4')
# Using the haar Cascade frontal face
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 3)
    count = str(len(faces))
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    faces = str(faces)
    cv.rectangle(frame, ((0, frame.shape[0] - 25)), (270, frame.shape[0]), (255, 255, 255), -1)
    cv.putText(frame, "Number of faces detected: " + count, (0, frame.shape[0] - 10),
                cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

    if ret==True:

        # write the  frame
        out.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release after completing task
cap.release()
out.release()

#Destroy all windows for closing after completion of task
cv.destroyAllWindows()