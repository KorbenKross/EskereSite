from pyexpat import model


class Song(model.Model):
    name = model.CharField(max_length=125)
    audio_file = model.FileField()