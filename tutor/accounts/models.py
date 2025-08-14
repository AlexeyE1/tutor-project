from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    email_confirmed = models.BooleanField(default=False)
    
    # Общие поля для всех пользователей
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    
    class Meta:
        abstract = True


class SubjectTag(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('history', 'History'),
        ('computer_science', 'Computer Science'),
    ]

    name = models.CharField(choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.name


class LearningTypeTag(models.Model):
    LEARNING_TYPE_CHOICES = [
        ('Подготовка к ОГЭ/ЕГЭ', 'Подготовка к ОГЭ/ЕГЭ'),
        ('Помощь с домашним заданием', 'Помощь с домашним заданием'),
        ('Углубленное изучение', 'Углубленное изучение'),
    ]

    name = models.CharField(choices=LEARNING_TYPE_CHOICES)

    def __str__(self):
        return self.name


class StudentProfile(CustomUser):
    education_level = models.CharField(max_length=50, blank=True)
    interests = models.TextField(blank=True)
    learning_goals = models.TextField(blank=True)

class TeacherProfile(CustomUser):
    experience_years = models.PositiveIntegerField(default=0)
    certificates = models.ManyToManyField('Certificate', blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    subjects = models.ManyToManyField(SubjectTag, blank=True)
    learning_types = models.ManyToManyField(LearningTypeTag, blank=True)
    available_times = models.ManyToManyField('TimeSlot')
    verification_documents = models.FileField(upload_to='verification_docs/', blank=True)


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_received = models.DateField()
    document = models.FileField(upload_to='certificates/')


class TimeSlot(models.Model):
    day_of_week = models.IntegerField(choices=[(i, day) for i, day in enumerate(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])])
    start_time = models.TimeField()
    end_time = models.TimeField()