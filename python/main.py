# -*- coding: utf-8 -*-

# ===============================================================================
# 
#                               CV Lab 1
#
#       Author: Rzhevskiy S.S. ITMO University
# 
# ===============================================================================

import cv2
import numpy as np
import time

#Входное изображение
INPUT_IMAGE = "stars.jpg"

IMAGE_HEIGHT = 720
IMAGE_WIDTH = 1280

#Входное видео
INPUT_VIDEO = "big_buck_bunny_720p_5mb.mp4"

#Остановка в мс для фрейма
TIMESTAMP_MS = 10000


#Сложить используя средства "pure" python
def addImage_PurePy(input_image1, input_image2):
    #Копируем
    out_img_arr = np.empty_like(input_image1)
    out_img_arr[:] = input_image1
    #Реализуем сложение(без защиты от разности размеров)
    for i in range(0,IMAGE_HEIGHT):
        for j in range(0,IMAGE_WIDTH):
            for k in range(0,3):
                #Защита от переполнения
                value1 = np.int16(out_img_arr[i,j,k])
                value2 = np.int16(input_image2[i,j,k])
                result = value1 + value2
                if result > 255:
                    result = 255
                result = np.uint8(result)
                out_img_arr[i,j,k] = result

    return out_img_arr

def subImage_PurePy(input_image1, input_image2):
    #Копируем
    out_img_arr = np.empty_like(input_image1)
    out_img_arr[:] = input_image1
    #Реализуем сложение(без защиты от разности размеров)
    for i in range(0,IMAGE_HEIGHT):
        for j in range(0,IMAGE_WIDTH):
            for k in range(0,3):
                #Защита от переполнения
                value1 = np.int16(out_img_arr[i,j,k])
                value2 = np.int16(input_image2[i,j,k])
                result = value1 - value2
                if result < 0:
                    result = 0
                result = np.uint8(result)
                out_img_arr[i,j,k] = result

    return out_img_arr

#Сложить используя средства Numpy
def addImage_Numpy(input_image1, input_image2):
    #Очень хочется, но тогда результат будет другой вследствие переполнения 0xFF
    #out_img_arr = input_image1 + input_image2

    #Создаем копию
    image_out = np.empty_like(input_image1)
    image_out[:] = input_image1

    #Такой вот хук для защиты от переполнения
    image_out = np.add(input_image1,input_image2, dtype = np.uint16);
    mask = image_out > 255
    image_out[mask] = 255
    image_out = np.uint8(image_out)
    

    return image_out

#Вычесть используя средства Numpy
def subImage_Numpy(input_image1, input_image2):
    #Очень хочется, но тогда результат будет другой вследствие переполнения 0xFF
    #out_img_arr = input_image1 - input_image2

    #Создаем копию
    image_out = np.empty_like(input_image1)
    image_out[:] = input_image1

    #Такой вот хук для защиты от переполнения
    image_out = np.subtract(input_image1,input_image2, dtype = np.int16);
    mask = image_out < 0
    image_out[mask] = 0
    image_out = np.uint8(image_out)
    
    return image_out

#Сложить и вычесть используя средства OpenCV
#Технически, тоже самое, что и сложить через Numpy... https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html
def addImage_OpenCV(input_image1, input_image2):
    return cv2.add(input_image1, input_image2)

def subImage_OpenCV(input_image1, input_image2):
    return cv2.subtract(input_image1, input_image2)

#
#   Основная логика работы
#

if __name__ == "__main__":
    vidcap = cv2.VideoCapture(INPUT_VIDEO)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,TIMESTAMP_MS)
    success,image = vidcap.read()

    if success:
        image2 = cv2.imread('stars.jpg')

        cv2.imshow("Image",image)
        
        while 1:

            key = cv2.waitKey(1)

            # q - выход из программы
            if key & 0xFF == ord('q'):
                print("Done!")
                break

            # a - сложение циклами
            elif key & 0xFF == ord('a'):
                start_time = time.time()
                cv2.destroyAllWindows()
                image_out = addImage_PurePy(image, image2)
                cv2.imshow("Image",image_out)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("add image")

            # s - вычитаение циклами
            elif key & 0xFF == ord('s'):
                start_time = time.time()
                cv2.destroyAllWindows()
                image_out = subImage_PurePy(image,image2)
                cv2.imshow("Image",image_out)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("sub image")

            # w - сложение OpenCV
            elif key & 0xFF == ord('w'):
                start_time = time.time()
                cv2.destroyAllWindows()
                image_out = addImage_OpenCV(image, image2)
                cv2.imshow("Image",image_out)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("add OCV image")

            # e- вычитание OpenCV
            elif key & 0xFF == ord('e'):
                start_time = time.time()
                cv2.destroyAllWindows()
                image_out = subImage_OpenCV(image, image2)
                cv2.imshow("Image",image_out)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("sub OCV image")

            #Если случайно закрыл чудотворным крестом и все повисло
            if cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:        
                break
            


    # When everything done, release the capture
    vidcap.release()
    cv2.destroyAllWindows()