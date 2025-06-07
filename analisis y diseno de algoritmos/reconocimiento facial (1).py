import cv2

#nos aseguramos que Open CV esta correctamente instalado y la version que tenemos.
print(cv2 .__version__)

#variable que se encargara de almacenar lo que vea en la camara 
captura = cv2 .VideoCapture(0)

#la variable "detector_de_rostros" contendra el modelo que me ayudara a detectar los rostros
#si la camara esta viendo la camara o no
detector_de_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#print(captura.read())
#print("--------------")
#print(captura.read())

while True:
   #esto almacenara lo siguiente:
   #retenido: un valor booleano que indicara si la camara ha capturado algo
   #frame: es un valor 
    retenido, frame = captura.read()

    #if retenido == True:
     #   print(frame)


    imagen_byc = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mi_cara = detector_de_rostros.detectMultiScale(imagen_byc, 1.1, 5)
    print(mi_cara)

    cv2.flip(frame, 1)

    #cv to color 

    #imshow -> image show
    cv2.imshow("FACE DETECTOR", imagen_byc)

#agregamos una forma de salir del programa 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


#0: hace referencia a la camara de la computadora
#1: camara extra 
#2: camara extra 

#por defecto es 0