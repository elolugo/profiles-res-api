from django.db import models

#standard imports for overwriting the default authentication system of Django
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#import for the manager of the User model
from django.contrib.auth.models import BaseUserManager

# importing the settings of the whole of this Django project
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for User profiles, how Django handles this custom user model"""

    def create_user(self, email, name, password=None):
        """create new user profile. What Django will do when creating a new user through the command line"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) # (XXXX@YYY.com) lowercase the mail portion -> YYYY
        user = self.model(email=email, name=name) # creates a new UserProfile object and sets the email and name
        user.set_password(password) #hashing the password string into the UserProfile object

        user.save(using=self._db) #saving the new user in the database

        return user

    def create_superuser(self, email, name, password):
        """create new super user profile. What Django will do when creating a new super user through the command line"""
        user = self.create_user(email, name, password) # creates a new user with the mail and name provided

        user.is_superuser = True #set the status of super user as true
        user.is_staff= True #set the status of staff member as true

        user.save(using=self._db) #saving the new super user in the database

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) #every email in the system must be unique
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #default value is true
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() #how Django handles this custom user model

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self): #
        """for the user listing by their email address in the Django Admin page"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
