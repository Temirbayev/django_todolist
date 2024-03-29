
**Имя проекта:** "ToDo Time Tracker"

**Описание:**
Веб-приложение для учета времени, потраченного на выполнение задач в формате "Список дел" (To-Do List). 
Пользователь сможет создавать задачи, назначать им сроки выполнения, отмечать их выполнение и вести учет времени, проведенного над каждой задачей.

**Функциональность:**
1. Регистрация и аутентификация пользователей.
2. Добавление, редактирование и удаление задач в списке дел.
3. Установка сроков выполнения для каждой задачи.
4. Отметка задач как выполненных или невыполненных.
5. Ведение учета времени, проведенного над задачами. Пользователь может запускать и останавливать таймер для каждой задачи.
6. Подробная статистика: сколько времени было потрачено на каждую задачу, какие задачи выполнены в срок, а какие - нет.
7. Фильтры и сортировка задач по различным параметрам (по дате, по статусу, по времени выполнения).
8. Уведомления и напоминания о приближающихся сроках выполнения задач.

**Технологии:**
1. Django для создания веб-приложения.
2. База данных (например, PostgreSQL) для хранения информации о задачах, пользователях и времени.
3. Frontend с использованием HTML, CSS, JavaScript, Bootstrap.
4. Использование Django REST framework для создания API для взаимодействия с фронтендом.
5. Развертывание проекта на сервере.

Этот проект предоставляет возможность практически применить навыки работы с Django, 
базами данных, веб-разработкой и управлением временем, а также создать полезное приложение для себя и других пользователей.


Таблица "Пользователи" (Users):

user_id (Primary Key): Уникальный идентификатор пользователя.
username: Имя пользователя.
password: Захешированный пароль пользователя.
email: Адрес электронной почты пользователя.
Таблица "Задачи" (Tasks):

task_id (Primary Key): Уникальный идентификатор задачи.
title: Заголовок задачи.
description: Описание задачи.
deadline: Срок выполнения задачи.
created_at: Дата и время создания задачи.
completed: Флаг, указывающий, выполнена ли задача.
user_id (Foreign Key): Связь с пользователем, которому принадлежит задача.
Таблица "Учет времени" (TimeEntries):

time_entry_id (Primary Key): Уникальный идентификатор записи о времени.
task_id (Foreign Key): Связь с задачей, над которой проводилось время.
start_time: Время начала работы над задачей.
end_time: Время завершения работы над задачей.
comment: Комментарий или описание проделанной работы.
user_id (Foreign Key): Связь с пользователем, который провел время над задачей.
Таблица "Уведомления" (Notifications):

notification_id (Primary Key): Уникальный идентификатор уведомления.
user_id (Foreign Key): Связь с пользователем, которому адресовано уведомление.
message: Текст уведомления.
timestamp: Время отправки уведомления.
Таблица "Статистика" (Statistics):

statistic_id (Primary Key): Уникальный идентификатор статистики.
user_id (Foreign Key): Связь с пользователем, для которого собирается статистика.
task_completed_count: Количество выполненных задач.
total_time_spent: Общее время, проведенное над задачами.
average_completion_time: Среднее время выполнения задач.

Cхема проекта->
![Схема ToDoList](https://github.com/Temirbayev/django_todolist/assets/60303183/e318ef0c-da95-4684-98da-873be11a050b)
