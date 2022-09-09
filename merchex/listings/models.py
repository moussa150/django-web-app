from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.forms import CharField
from django import forms



class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE_ROCK='AR'

    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(choices=Genre.choices ,max_length=5)
    biography=models.fields.CharField(max_length=100)
    year_formed=models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active=models.fields.BooleanField(default=True)
    officiel_homepage=models.fields.URLField(null=True, blank=True)
    # like_new=models.fields.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}'



class BandForm(forms.ModelForm):
    class Meta:
        model=Band
        # fields= '__all__'
        exclude=('active','officiel_homepage')







class Annonce(models.Model):

    class Type(models.TextChoices):
        RECORDS='R'
        CLOTHING='C'
        POSTERS='P'
        MISC='M'


    titre=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=200)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2022)]
    )
    type=models.fields.CharField(choices=Type.choices,max_length=20)
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
