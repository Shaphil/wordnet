from django.db import models


class BanglaWords(models.Model):
    class Meta:
        verbose_name_plural = 'Bangla Words'

    bng_id = models.CharField(max_length=16, primary_key=True)
    bangla_word = models.CharField(max_length=64)

    def __str__(self):
        return self.bangla_word
