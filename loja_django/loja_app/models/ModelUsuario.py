from django.contrib.auth.models import User


class ModelUsuario(User):
    def __unicode__(self):
        return self.first_name

    def __srt__(self):
        return self.first_name
