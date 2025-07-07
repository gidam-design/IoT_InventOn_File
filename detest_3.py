config = picam2.create_video_configuration(main={"size": (300,300), "format": ">
picam2.configure(config)
picam2.start()
time.sleep(0.1)

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
