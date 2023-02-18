from django.db import models
# import classes needed for custom user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# custom user manager
class Lctec_CustomUserManager(BaseUserManager):



    # called when creating user through terminal and presumably drf
    # only pass in req params, all other unrequired params like
    # first/lastname, favorite color, etc. will be held in **extra_fields param
    def create_user(self, email, username, password, **extra_fields):
        
        print('\n\n\nCREATING USER \n\n\n')
        if not email:
            raise ValueError("Email must be provided")
        if not username:
            raise ValueError("Username must be provided")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # called when creating superuser through terminal and presumably drf
    def create_superuser(self, email, username, password, **extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)
    

# Custom User Model; define fields you want to be included in User Model, can be updated changed later
class Lctec_User(AbstractBaseUser, PermissionsMixin):

    # define fields you want to be included in User Model, can be updated changed later
    # authenticate with either username or email
    email = models.EmailField(db_index=True, max_length=100, unique=True)
    username = models.CharField(db_index=True, max_length=64, unique=True)

    # non-req'd fields
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    favorite_color = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # if user is allowed access to admin site. 
    is_staff = models.BooleanField(default=False)
    # if user is currently active
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # connect user class to manager class
    objects = Lctec_CustomUserManager()

    # choose wisely, password resets will use this field
    # needs to have unique=True
    USERNAME_FIELD = 'username'
    # used by python manage.py createsuperuser and presumably drf for token authentication
    # should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'favorite_color']

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True