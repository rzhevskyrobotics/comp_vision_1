//  ITMO University Computer Vision Course
//
//  CV Lab 1
//  
//  Author: Rzhevskiy S.S.
//

#include <iostream>
#include <opencv2/opencv.hpp>

//Для временных меток
#include <chrono>

using namespace cv;
using namespace std;


//Время, где ловим фрейм во входном видео
const int MS_FRAME_TIMESTAMP = 10000;


//Функция вычитания. Модифицирует оригинальную матрицу
void substractImage(Mat *sourceImage, Mat *substractImage){

    //Матрично вычесть
    //*resultImage = *sourceImage - *substractImage;

    //Через цикл
    for(int i=0; i<sourceImage->rows; i++){
        for(int j=0; j<sourceImage->cols; j++){
            //По всем трем каналам
            for(int k=0; k < 3; k++){
                int result = int(sourceImage->at<cv::Vec3b>(i,j)[k]) - int(substractImage->at<cv::Vec3b>(i,j)[k]);
                if(result < 0){
                    result = 0;
                }
                sourceImage->at<cv::Vec3b>(i,j)[k] = uint8_t(result);
            }
        }
    }

    return;
}

int main(int argc, char** argv){

    
    //Для измерения времени исполнения
    using chrono::high_resolution_clock;
    using chrono::duration_cast;
    using chrono::duration;
    using chrono::milliseconds;
    

    //Основная программа

    //Ловим фрейм
    VideoCapture cap("big_buck_bunny_720p_5mb.mp4");

    if(!cap.isOpened()){
        cout << "Error opening video stream or file" << endl;
        return -1;
    }

    cap.set(CAP_PROP_POS_MSEC,MS_FRAME_TIMESTAMP);

    //Читаем файл для вычитания
    Mat imageToSubtract = imread("stars.jpg");

    //Открываем фрейм
    Mat originalImage;
    bool success = cap.read(originalImage);

    if(success){
        // Error Handling
        if (originalImage.empty()) {
            cout << "Image File "
                << "Not Found" << endl;
    
            // Тупо ждем
            cin.get();
            return -1;
        }
  
        //Засекаем временную метку
        auto t1 = high_resolution_clock::now();
        //Проиводим вычитаение
        substractImage(&originalImage,&imageToSubtract);

        //Считаем прошедшее время
        auto t2 = high_resolution_clock::now();

        //Мs в int
        auto ms_int = duration_cast<milliseconds>(t2 - t1);

        //Переводим в double
        duration<double, std::milli> ms_double = t2 - t1;

        std::cout << ms_int.count() << "ms\n";
        std::cout << ms_double.count() << "ms\n";

        imshow("Subtracted", originalImage);
    
        // ОБЯЗАТЕЛЬНО НАЖАТЬ НА КЛАВЕ!
        waitKey(0);
    } else{
        cout << "Error while read frame!";
        return -1;
    }

    return 0;
}