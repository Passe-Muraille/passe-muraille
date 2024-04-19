from django.db import models

# Create your models here.

class Enquete(models.Model):
	titre = models.CharField(max_length=255, verbose_name='Titre de l\'enquête')
	ville = models.CharField(max_length=35, verbose_name='Ville')
	description = models.TextField(verbose_name='Description de l\'enquête')
	date = models.DateField(verbose_name="Date")
	victime = models.CharField(max_length=255, verbose_name='Victime')
	lieu = models.CharField(max_length=255, verbose_name='Lieu')
	questions = models.TextField(verbose_name='Questions')
	def __str__(self):
		return "{}".format(self.titre)

class Indice_chiffres(models.Model):
	nom = models.CharField(max_length=35, verbose_name='Nom')
	code =  models.IntegerField(verbose_name='Code')
	enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
	contenu_textuel = models.TextField(verbose_name='Contenu textuel', null=True, blank=True)
	contenu_image = models.ImageField(verbose_name='Image (ou bien unique, ou bien qui sera à la suite du texte)', null=True, blank=True)
	contenu_audio = models.FileField(verbose_name='Audio', null=True, blank=True) #upload_to...
	contenu_video = models.FileField(verbose_name='Vidéo', null=True, blank=True) #upload_to...

	def __str__(self):
		return "{}".format(self.nom)
	
class Indice_autre(models.Model):
	nom = models.CharField(max_length=35, verbose_name='Nom')
	code =  models.CharField(max_length=35, verbose_name='Code')
	enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
	contenu_textuel = models.TextField(verbose_name='Contenu textuel', null=True, blank=True)
	contenu_image = models.ImageField(verbose_name='Image (ou bien unique, ou bien qui sera à la suite du texte)', null=True, blank=True)
	contenu_audio = models.FileField(verbose_name='Audio', null=True, blank=True) #upload_to...
	contenu_video = models.FileField(verbose_name='Vidéo', null=True, blank=True) #upload_to...

	def __str__(self):
		return "{}".format(self.nom)

class Indice_chiffres_trouves(models.Model):
	equipe = models.CharField(max_length=255, verbose_name='Equipe') #connu grâce à la connection
	indice = models.ForeignKey(Indice_chiffres, on_delete=models.CASCADE)
	date_decouverte = models.DateField(verbose_name="Date de découverte")

class Indice_autre_trouves(models.Model):
	equipe = models.CharField(max_length=255, verbose_name='Equipe')
	indice = models.ForeignKey(Indice_autre, on_delete=models.CASCADE)
	date_decouverte = models.DateField(verbose_name="Date de découverte")

class Event(models.Model):
	name = models.CharField(max_length=255)
	event_date = models.DateTimeField()