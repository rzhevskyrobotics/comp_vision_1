## ITMO Computer Vision Couse 2022

---



# Лабораторная работа №1



## Вариант 8. Сложение и вычитание изображений

**Цель работы:** 

Научиться реализовывать один из простых алгоритмов обработки
изображений.



**Задание общее:** 

1. Реализовать программу согласно варианту задания. Базовый алгоритм,
   используемый в программе, необходимо реализовать в 3 вариантах: с
   использованием встроенных функций какой-либо библиотеки (OpenCV,
   PIL и др.) и нативно на Python + |с использованием Numba или C++|.
2. Сравнить быстродействие реализованных вариантов.
3. Сделать отчёт в виде readme на GitHub, там же должен быть выложен
   исходный код.
   
   

**Вариант задания:**

Сложение и вычитание изображений. Задано некоторое изображение
того же размера, что кадр видео. На вход поступает изображение,
программа отрисовывает окно, в которое выводится либо исходное
изображение, либо после сложения или вычитания (переключение по
нажатию клавиши). Базовый алгоритм - сложение и вычитание.



## Теоретическая база

Цифровое изображение — двумерное изображение, представленное в цифровом виде. В зависимости от способа описания, изображение может быть растровым или векторным. 

Векторные изображения математически задаются набором элементарных геометрических построений - примитивов. Само по себе векторное описание абстрактно, и для визуализации его необходимо отобразить на чем-либо(экране, напечтать на бумаге и т.д.) по определенному алгоритму, чаще всего через отображение в виде растровой графики. 

Растровые изображения кодируются прямоугольным двумерным массивом чисел H(высота)*W(ширина), каждое число задает один элемент изображения(пиксель). Для каждого пикселя задаются параметры яркости, цвета и прозрачности(либо используется комбинация этих значений). 

В простейшем случае каждому пикселю присваивается три N-битных числа(где N называется глубиной цвета и отвечает за кол-во доступных оттенков) для каналов R(красный цвет), G(зеленый цвет) и B(синий цвет).  Для реализации сложения и вычитания изображений досточно произвести необходимую арифметическую операцию с каждым каналом для каждого пикселя. Эту операцию можно провести как в обычном цикле, так и применяя встроенные оптимизированные функции различных библиотек. В таком случае, как правило, используются матричные операции.  

Библиотеки для реализации систем компьютерного зрения, например, используемая в работе OpenCV, позволяет оперировать как с отдельными пикселями изображения, так и проводить различные преобразования с изображениями.   

## Описание разработанной системы

Согласно заданию, для решения написано две программы - основная на python и дополнительная на C++. В программе на C++ реализовано только вычитание в простом цикле для сравнения быстродействия. В обоих случаях использовалась библиотека OpenCV. Запуск и компиляция программ произодилиь в среде OS Linux Mint 20.   

В корне проекта представлены две папки - python и cpp, в которых находятся исходные файлы для конкретной реализации. В папке out представлены входное видео, входной фрейм, результат сложения и результат вычитания. Названия и пути к файлам для простоты прописаны в исходниках в виде констант. 

Алгоритм программы на python в общем виде следующий:

1. Импортируем требуемые библиотеки и модули

2. Читаем видеофайл, получаем фрейм по заданной в настройках временной метке

3. Читаем изображение, которое будем вычитать из кадра видео. 

4. Отображаем на экране оригинальное изображение

5. Запускаем цикл ожидания ввода с клавиатуры пользователем. В зависимости от нажатого символа программа может реализовать:
   
   1. "s" вычитание через циклы и операции с пикселями
   
   2. "a" сложение через циклы и операции с пикселями
   
   3. "w" сложение средстами OpenCV
   
   4. "e" вычитание средстами OpenCV
   
   5. "q" завершение цикла
   
   После нажатия символа выполняется команда и отображается на экране результат операции, цикл повторяется до ввода пользователем символа q или закрытия экрана программы. В процессе выполнения операций специальный программный счетчик фиксирует времена входа и выхода в функцию расчета, после чего получает затраченное на работу время. В консоли отображается время исполнения операции в секундах.

6. После завершения основного цикла скрипт уничтожает окна и освобождает память. 
   
   

Алгоритм работы программы на C++:

1. Подключение библиотек.

2. Инициализация переменных для программного таймера

3. Отрытие входного видеопотока из файла, получение фрейма

4. Открытие изображения для вычитания. 

5. Получение временной метки начала операции

6. Операция вычитания с матрицами избражений

7. Получение временной метки завершения операции и печать ее в консоли(в мс)

8. Отображение результата на экране

9. Ожидание ввода пользователем любого символа с клавиатуры. После получения символа программа завершается

Важным моментом реализации арифметических операций с пикселями является требование самостоятельно следить за переполнением 8-битных элементов массива. В предлагаемых программах для защиты от этого реализован специальный механизм - промежуточное приведение к более крупным целочисленным типам.

## Результаты работы и тестирования системы

Входной фрейм видеопотока:

![Input](out/cv_input.png)

Изображение для вычитания:

![SibIn](out/stars.jpg)

Результат сложения:

![Add](out/cv_add.png)

Результат вычитания:

![Sub](out/cv_sub.png)

Время исполнения операции:

|                      | Циклы-python | OpenCV-python | Циклы-C++ |
|:--------------------:| ------------ | ------------- | --------- |
| Время исполнения, мс | 9822         | 51            | 51        |

## Выводы по работе

В ходе работы были реализованы алгоритмы сложения и вычитания изображений средствами python и c++ с библиотекой OpenCV. Выявлено, что использование оптимизированных библиотечных функций предпочтительнее в работе и позволяет существенно ускорить процесс обработки изображений(в данной работе почти в 200 раз) . Кроме того, для ускорения работы предпочтительнее использовать компилируемые языки по типу C++.  

## Использованные источники

1. https://en.wikipedia.org/wiki/Digital_image

2. https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html 

3. https://stackoverflow.com/questions/29611185/avoid-overflow-when-adding-numpy-arrays


