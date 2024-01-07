# B.B.R
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from  .iqrouser import CustomUserManager

class Subject(models.Model):
    subject_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.subject_name


class IqroUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    # Otchestva
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    s_name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255)
    
    type = models.SmallIntegerField(choices=(( 1,"Super"),(2,'admin'),(3,'head teacher'),(4,'teacher')) )
    birthday = models.DateField()
    passport_ser = models.CharField(max_length=255, unique=True)
    passport_JSHSHR = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    Subject = models.ManyToManyField(Subject, related_name='teacher', default=None)
    finger_id = models.CharField(max_length=255, unique=True)
    telegram = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta():
        db_table = 'iqro_user'

            
    def __str__(self):
        return f'{self.first_name} {self.s_name}  {self.last_name}'
    

class Cla_ss(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    teacher = models.OneToOneField(IqroUser, on_delete=models.CASCADE, related_name='class_teacher')

    def __str__(self):
        return self.title


class Pupil(models.Model):
    f_name = models.CharField(max_length=255)
    s_name = models.CharField(max_length=255, null=True, blank=True)
    l_name = models.CharField(max_length=255)
    cla_ss = models.ForeignKey(Cla_ss, on_delete=models.CASCADE, related_name='class_pupil')
    finger_id = models.CharField(max_length=255, unique=True)
    telegram = models.CharField(max_length=255)
     
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    

class Finger_Print(models.Model):
    arrived = models.DateTimeField(null=True, blank=True)
    left = models.DateTimeField(null=True, blank=True)
    users = models.ForeignKey(IqroUser, on_delete=models.SET_NULL, null=True, blank=True)
    pupil = models.ForeignKey(Pupil, on_delete=models.SET_NULL , null=True, blank=True)

    @property
    def status(self):
        if self.arrived and self.left:
            return False
        return True


class Monitoring(models.Model):
    cla_ss = models.ForeignKey(Cla_ss, models.CASCADE, related_name='class_monitoring')
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, related_name='monitoring_pupil')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='monitoring_subject')
    grade = models.PositiveIntegerField()
    data = models.DateField()
    file = models.FileField(upload_to='monitoring_files/')
    
    def __str__(self):
        return f"{self.pupil} - {self.subject} - {self.cla_ssW}"


class Table(models.Model):
    teacher = models.ForeignKey(IqroUser, on_delete=models.CASCADE, related_name='table_teacher')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_title')
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher} {self.subject}"


class LessonTime(models.Model):
    enter = models.BooleanField(default=False)
    epsont = models.BooleanField(default=True)
    leate = models.CharField(max_length=99)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, related_name='lesson_pupil')
    teacher = models.ForeignKey(IqroUser, on_delete=models.CASCADE, related_name='lesson_teacher')

    def __str__(self):
        return f'{self.pupil} { self.teacher}'


class AboutTeacher(models.Model):
    video = models.FileField(upload_to='About_teacher/Video')
    photo = models.FileField(upload_to='About_teacher/Photo')
    degry = models.SmallIntegerField()
    certificat = models.FileField(upload_to='About_teacher/Cerificat')
    teacher = models.ForeignKey(IqroUser, on_delete=models.CASCADE, related_name="about_teacher")

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name}"
        