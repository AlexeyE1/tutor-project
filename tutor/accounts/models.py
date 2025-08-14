from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    email_confirmed = models.BooleanField(default=False)

    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class SubjectTag(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('history', 'History'),
        ('computer_science', 'Computer Science'),
    ]
    name = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.get_name_display()


class LearningTypeTag(models.Model):
    LEARNING_TYPE_CHOICES = [
        ('Подготовка к ОГЭ/ЕГЭ', 'Подготовка к ОГЭ/ЕГЭ'),
        ('Помощь с домашним заданием', 'Помощь с домашним заданием'),
        ('Углубленное изучение', 'Углубленное изучение'),
    ]
    name = models.CharField(max_length=50, choices=LEARNING_TYPE_CHOICES)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    education_level = models.CharField(max_length=50, blank=True)
    interests = models.TextField(blank=True)
    learning_goals = models.TextField(blank=True)

    def __str__(self):
        return f"Student: {self.user.username}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher_profile")
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    experience_years = models.PositiveIntegerField(default=0)
    certificates = models.ManyToManyField('Certificate', blank=True)
    subjects = models.ManyToManyField(SubjectTag, blank=True)
    learning_types = models.ManyToManyField(LearningTypeTag, blank=True)
    available_times = models.ManyToManyField('TimeSlot')
    verification_documents = models.FileField(upload_to='verification_docs/', blank=True)

    def __str__(self):
        return f"Teacher: {self.user.username}"


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    date_received = models.DateField()
    document = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    DAYS = [(i, day) for i, day in enumerate(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])]
    day_of_week = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time}"