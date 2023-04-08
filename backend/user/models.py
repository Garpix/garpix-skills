from garpix_user.models import GarpixUser


class User(GarpixUser):
    USERNAME_FIELDS = ('email',)
