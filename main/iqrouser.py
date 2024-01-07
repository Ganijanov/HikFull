from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Email field must be set')
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', 'Name')
        extra_fields.setdefault('last_name', 'L name')
        extra_fields.setdefault('phone_num', '+998 *** ** **')
        extra_fields.setdefault('type', 1)
        extra_fields.setdefault('passport_ser', None)
        extra_fields.setdefault('passport_JSHSHR', None)
        extra_fields.setdefault('finger_id', None)
        extra_fields.setdefault('telegram', None)
        extra_fields.setdefault('birthday', '2000-10-10')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
