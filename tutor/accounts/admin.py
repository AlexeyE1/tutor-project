from django.contrib import admin
from .models import CustomUser, TeacherProfile, StudentProfile, SubjectTag, Certificate, LearningTypeTag


# Register your models here.
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(SubjectTag)
admin.site.register(Certificate)
admin.site.register(LearningTypeTag)
