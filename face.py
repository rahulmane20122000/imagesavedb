import cv2
import os
import sqlite3

cam=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
counter=0
conn=sqlite3.connect('final.db')
cursor=conn.cursor() 

cursor.execute("""CREATE TABLE IF NOT EXISTS final_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT,data BOLB)""")



while True:
    ret,frame=cam.read()
    k = cv2.waitKey(30)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,h,w) in faces:           
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi=frame[y:y+w,x:x+h]
    
    cv2.imshow('test1',frame)
    
    
   
   
    if k==27:
        img_name="rahul{}.png".format(counter)
        cv2.imwrite(img_name,frame)
        counter +=1
        cursor.execute("""INSERT INTO final_table(name,data) VALUES(?,?)""",(img_name,frame))

    if k==32:
        break
        
    
        
        
conn.commit()
cursor.close()
conn.close()   
cam.release()
cv2.destroyAllWindows()                    
   
   
       
   
                  
               
 

   



