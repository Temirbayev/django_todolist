from django.db import models

# Create your models here.


class User(models.Model):
    """
    user_id (Primary Key): Уникальный идентификатор пользователя.
    username: Имя пользователя.
    password: Захешированный пароль пользователя.
    email: Адрес электронной почты пользователя.
    """
    username = models.CharField(max_length=10, verbose_name='Имя')
    password = models.CharField(max_length=10, verbose_name='Пароль')
    email = models.EmailField(max_length=200, null=True, verbose_name='Почта')

    def __str__(self):
        return self.username


class Task(models.Model):
    """
    Task представляет собой задачу в списке дел и содержит следующие поля:

    Title: Заголовок задачи.
    Description: Описание задачи (необязательное поле).
    Deadline: Срок выполнения задачи.
    Created_at: Дата и время создания задачи.
    Completed: Флаг, указывающий, выполнена ли задача.
    User: Ссылка на пользователя, которому принадлежит задача, с использованием ForeignKey.
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TimeEntry(models.Model):
    """
    TimeEntry представляет запись о времени, проведенном над задачей, и содержит следующие поля:

    Task: Ссылка на задачу, для которой записано время, с использованием ForeignKey.
    Start_time: Время начала работы над задачей.
    End_time: Время завершения работы над задачей.
    Comment: Комментарий или описание проделанной работы (необязательное поле).
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.task
