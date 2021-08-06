from django.db import models


class BanglaWords(models.Model):
    class Meta:
        verbose_name_plural = 'Bangla Words'

    bng_id = models.CharField(max_length=16, primary_key=True)
    bangla_word = models.CharField(max_length=64)

    def __str__(self):
        return self.bangla_word


class BanglaEnglishRelations(models.Model):
    class Meta:
        verbose_name_plural = 'Bangla English Relations'

    bng_id = models.OneToOneField(
        'BanglaWords', primary_key=True, on_delete=models.CASCADE)
    eng_id = models.ForeignKey('EnglishWords', on_delete=models.CASCADE)


class EnglishWords(models.Model):
    class Meta:
        verbose_name_plural = 'English Words'

    eng_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=64)
    bangla_word = models.ManyToManyField(
        BanglaWords, through=BanglaEnglishRelations)

    def __str__(self):
        return self.word
