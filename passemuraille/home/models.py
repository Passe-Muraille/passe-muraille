from django.db import models

# Create your models here.

class Enquete(models.Model):
	class Meta:
		verbose_name = 'Enquête'
		verbose_name_plural = 'Enquêtes'
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

	class Meta:
		verbose_name = 'Indice à chiffres'
		verbose_name_plural = 'Indices à chiffres'

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
	class Meta:
		verbose_name = 'Indice format libre'
		verbose_name_plural = 'Indices format libre'

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
	class Meta:
		verbose_name = 'Indice à chiffres trouvés'
		verbose_name_plural = 'Indices à chiffres trouvés'

	equipe = models.CharField(max_length=255, verbose_name='Equipe') #connu grâce à la connection
	indice = models.ForeignKey(Indice_chiffres, on_delete=models.CASCADE)
	date_decouverte = models.DateTimeField(verbose_name="Date de découverte")


class Indice_autre_trouves(models.Model):
	class Meta:
		verbose_name = 'Indice format libre trouvés'
		verbose_name_plural = 'Indices format libre trouvés'
		
	equipe = models.CharField(max_length=255, verbose_name='Equipe')
	indice = models.ForeignKey(Indice_autre, on_delete=models.CASCADE)
	date_decouverte = models.DateTimeField(verbose_name="Date de découverte")

class Event(models.Model):
	class Meta:
		verbose_name = 'Timer'
		verbose_name_plural = 'Timer'

	name = models.CharField(max_length=255)
	event_date = models.DateTimeField()


class Indices_trouves(models.Model):
	class Meta:
		verbose_name = 'Indice trouvé'
		verbose_name_plural = 'Indices trouvés'
	nom = models.CharField(max_length=255, verbose_name='Nom')
	equipe = models.CharField(max_length=255, verbose_name='Equipe')
	date_decouverte = models.DateTimeField(verbose_name="Date de découverte")


class Messagerie(models.Model):
	class Meta:
		verbose_name = 'Messagerie'
		verbose_name_plural = 'Messagerie'
	equipe = models.CharField(max_length=255, verbose_name='Equipe')
	message = models.TextField()
	image = models.ImageField(blank=True, null=True, upload_to='images/')
	date_envoie = models.DateTimeField(verbose_name="Date envoie", null=True)