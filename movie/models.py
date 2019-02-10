from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class MoviesList(models.Model):
    tid = models.CharField(max_length=10, unique= True)
    title = models.CharField(max_length=250,blank=True)
    url = models.CharField(max_length=250,blank=True)
    imdbrating = models.CharField(max_length=10,blank=True)
    year = models.IntegerField(blank=True)
    nrofgenre = models.IntegerField(blank=True)
    gen_action = models.CharField(max_length=100,blank=True)
    gen_adult = models.CharField(max_length=100,blank=True)
    gen_adventure = models.CharField(max_length=100,blank=True)
    gen_animation = models.CharField(max_length=100,blank=True)
    gen_biography = models.CharField(max_length=100,blank=True)
    gen_comedy = models.CharField(max_length=100,blank=True)
    gen_crime = models.CharField(max_length=100,blank=True)
    gen_documentary = models.CharField(max_length=100,blank=True)
    gen_drama = models.CharField(max_length=100,blank=True)
    gen_family = models.CharField(max_length=100,blank=True)
    gen_fantasy = models.CharField(max_length=100,blank=True)
    gen_filmnoir = models.CharField(max_length=100,blank=True)
    gen_gameshow = models.CharField(max_length=100,blank=True)
    gen_history = models.CharField(max_length=100,blank=True)
    gen_horror = models.CharField(max_length=100,blank=True)
    gen_music = models.CharField(max_length=100,blank=True)
    gen_musical = models.CharField(max_length=100,blank=True)
    gen_mystery = models.CharField(max_length=100,blank=True)
    gen_news = models.CharField(max_length=100,blank=True)
    gen_realitytv = models.CharField(max_length=100,blank=True)
    gen_romance = models.CharField(max_length=100,blank=True)
    gen_scifi = models.CharField(max_length=100,blank=True)
    gen_short = models.CharField(max_length=100,blank=True)
    gen_sport = models.CharField(max_length=100,blank=True)
    gen_talkshow = models.CharField(max_length=100,blank=True)
    gen_thriller = models.CharField(max_length=100,blank=True)
    gen_war = models.CharField(max_length=100,blank=True)
    gen_western = models.CharField(max_length=100,blank=True)
    is_subscribed = models.BooleanField(default=False)


class Subscribe(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    movielist = models.ForeignKey(MoviesList,on_delete=None)
    is_subscribed = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    sublike = models.IntegerField(default=0)




















