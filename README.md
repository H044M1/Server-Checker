# Server-Checker
Тестовое задание для стажера на направление «Автотестирование (Python)»
Задание: Реализовать консольную программу для тестирования доступности серверов по HTTP
протоколу. Программа должна замерять время выполнения запроса и выводить итоговую
статистику по скорости ответа сервера.
Для выполнения запросов по http протоколу была использована библиотека requests(потому что с ней я был уже более менее знаком)
Для обработки аргументов командной строки я использовал библиотеку argparse

### Краткое описание основного функционала программы:  
1. Парсинг аргументов командной строки – принимает список хостов, количество запросов, путь к файлу с хостами и файл для сохранения результатов.  
2. Чтение хостов из файла – если передан файл, программа загружает хосты из него.  
3. Проверка доступности хостов – выполняет указанное количество HTTP-запросов к каждому хосту и фиксирует результаты.  
4. Анализ времени отклика – вычисляет минимальное, максимальное и среднее время ответа.  
5. Корректность хостов – проверяет корректность URL с помощью регулярного выражения.  
6. Вывод результатов – отображает статистику успешных, неудачных запросов и ошибок, а также сохраняет результаты в файл (если указан).

### Инстуркции по запуску:
1.Запуск с указанием хостов через аргумент ключ -H (список хостов через запятую): python checker.py -H https://ya.ru,https://google.com
2. Запуск с указанием файла с хостами (по одному хосту в строке, ключ -F): python checker.py -F hosts.txt
3. Добавление количества запросов (ключ -C): python checker.py -H https://ya.ru -C 5
4. Сохранение результата в файл (ключ -O): python checker.py -H https://ya.ru -O result.txt

### Примеры вывода:
1.![image](https://github.com/user-attachments/assets/7e3c0052-e78b-494e-a58a-fbfae0f2a91e)
2.![image](https://github.com/user-attachments/assets/f927ab3c-e128-4c4e-9182-ee6f153119f5)

3.![image](https://github.com/user-attachments/assets/993b9b2c-0d0d-4053-bffc-9a8238a36c84)
4.![image](https://github.com/user-attachments/assets/06fca8cc-671f-4fd6-8b2b-b69224d8926f)

5.![image](https://github.com/user-attachments/assets/392b1e79-c4f3-4f14-952f-c1ea98306a75)
6.![image](https://github.com/user-attachments/assets/fa89884b-aab5-4713-8ccd-557c2f7266e4)

7.![image](https://github.com/user-attachments/assets/dd81b4cd-df71-4820-9289-8b46497a901e)
8.![image](https://github.com/user-attachments/assets/7b04e1b1-7b31-4dab-9b8e-994933bfc9c9)

9.![image](https://github.com/user-attachments/assets/526180be-6be8-401a-bc86-a474343c57d2)
