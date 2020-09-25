from django.db import models
from django.core.validators import MinLengthValidator
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# AbstractUser : 기존 장고의 유저모델을 가져와서 사용한다. --> 틀을 그대로 쓰면됨
# AbstractBaseUser : 새로운 유저 모델을 만들어서 사용한다. --> 처음부터 다 내가 만들어야됨
class UserAccountsManager(BaseUserManager):

    def create_user(self, user_id, name, password=None):

        if not user_id:
            raise ValueError("ID가 없습니다.")

        user = self.model(user_id=user_id, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id, name, password):

        user = self.create_user(user_id, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserAccounts(AbstractBaseUser, PermissionsMixin):
    """유저 계정 모델"""

    user_id = models.CharField(validators=[MinLengthValidator(2)], max_length=16, primary_key=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    objects = UserAccountsManager()

    USERNAME_FIELD = 'user_id' # 해당필드를 User_ID의 값으로 지정해서 사용할 수 있다고함
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ['user_id']
        verbose_name = "useraccount"
