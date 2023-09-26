import cv2
import numpy as np
import types
import sys

def toBinary(data):
    if type(data)==str:
        binaryData=""
        for i in data:
            binaryData+='{0:08b}'.format(ord(i))
        return binaryData
    elif type(data)==int or type(data)==np.uint8:
        return format(data,"08b")
    elif type(data)==bytes or type(data)==np.ndarray:
        return [format(i,"08b") for i in data]

def hideMessage(image, data):
    data+='\0'
    binaryData=toBinary(data)
    index=0
    length=len(binaryData)
    for values in image:
        for pixel in values:
            r,g,b=toBinary(pixel)

            if index<length:
                pixel[0]=int(r[:-1]+binaryData[index],2)
                index+=1
            if index<length:
                pixel[1]=int(g[:-1]+binaryData[index],2)
                index+=1
            if index<length:
                pixel[2]=int(b[:-1]+binaryData[index],2)
                index+=1
            if index>=length:
                break
    return image

def revealMessage(image):

    binaryData=""
    for values in image:
        for pixel in values:
            r,g,b=toBinary(pixel)
            binaryData+=r[-1]
            binaryData+=g[-1]
            binaryData+=b[-1]
    byteData= [ binaryData[i:i+8] for i in range(0, len(binaryData),8)]

    hiddenData=""
    for byte in byteData:
        hiddenData+=chr(int(byte,2))
        if hiddenData[-1]=='\0':
            break
    return hiddenData[:-1]

def encodeData():
    imageName=input("Enter image name")
    image=cv2.imread(imageName)
    data=input("Enter Message to be Hidden")
    print(type(image))
    newImageName=input("Enter name of new image")
    stegoImage=hideMessage(image,data)
    cv2.imwrite(newImageName,stegoImage)

def decodeData():
    image=cv2.imread(imageName)
    cv2.imshow("StegoImage",image)
    text=revealMessage(image)
    print(text)

def Stego():
    encodeData()
    decodeData()
Stego()
#sys.stdout.close()