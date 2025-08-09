from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
        default='student'
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username


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


class MentorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='mentor_profile')
    subjects = models.ManyToManyField(SubjectTag, blank=True)
    learning_types = models.ManyToManyField(LearningTypeTag, blank=True)
    bio = models.TextField(blank=True)
    available_days = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"MentorProfile({self.user.username})"