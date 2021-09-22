from django.db import models
from django.db.models.fields.related import OneToOneField



class Etudiant(models.Model):
    GENDER_CHOICES = [
        ('H','HOMME'),
        ('F','FEMME')
    ]
    NIVEAU_CHOICES = [
        ('TC1','TC1'),('TC2','TC2'),
        ('DIC1','DIC1'),('DIC2','DIC2'),
        ('DIC3','DIC3')
    ]
    first_name = models.CharField(max_length=300, null= False)
    last_name = models.CharField(max_length=300, null= False)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True,max_length=300)
    niveau = models.CharField(choices=NIVEAU_CHOICES,max_length=30)
    gender = models.CharField(choices= GENDER_CHOICES, max_length=30)
    codifie = models.BooleanField(default=True)

    class Meta:
        ordering=('last_name',)
  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EtudiantPayment(models.Model):

    MONTH_CHOICES = (
                ('JANVIER', 'JANVIER'),('FEVRIER', 'FEVRIER'),
                ('MARS', 'MARS'),('AVRIL', 'AVRIL'),
                ('MAI', 'MAI'),('JUIN', 'JUIN'),
                ('JUILLET', 'JUILLET'),('AOUT', 'AOUT'),
                ('SEPTEMBRE', 'SEPTEMBRE'),('OCTOBRE', 'OCTOBRE'),
                ('NOVEMBRE', 'NOVEMBRE'),('DECEMBRE', 'DECEMBRE'),          
    )

    mois_paye = models.CharField(choices= MONTH_CHOICES, max_length=30)
    date_payment = models.DateField()
    montant_paye = models.IntegerField( null=False)
    etudiant = models.ForeignKey(Etudiant, related_name='payments',on_delete=models.CASCADE)

    class Meta:
        ordering=('date_payment',)
  
    def __str__(self):
        return f"{self.mois_paye} ---> {self.etudiant}"


class Pavillon(models.Model):
    pavillon_name = models.CharField(max_length=200,null=False, unique=True)
    chef_pavillon = models.CharField(max_length=200)

    class Meta:
        ordering=('pavillon_name',)
  
    def __str__(self):
        return f"{self.pavillon_name}"


class Chambre(models.Model):
    ETAGE_CHOICES = [
        ('REZ_DE_CHAUSSE','REZ_DE_CHAUSSE'),
        ('PREMIER_ETAGE','PREMIER_ETAGE'),
        ('DEUXIEME_ETAGE','DEUXIEME_ETAGE')
    ]
    numero_chambre = models.IntegerField()
    etage = models.CharField(max_length=30, choices=ETAGE_CHOICES)
    occupee = models.BooleanField(default=False)
    pavillon = models.ForeignKey(Pavillon, related_name='chambres',on_delete=models.CASCADE)

    class Meta:
        ordering=('numero_chambre',)
  
    def __str__(self):
        return f"{self.numero_chambre} {self.pavillon}"


class Codification(models.Model):
    date_codification = models.DateField()
    annee_scolaire = models.CharField(max_length=60)
    etudiant = OneToOneField(Etudiant, on_delete=models.CASCADE, related_name="etudiant_codifie")
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name='chambres')

    class Meta:
        ordering=('date_codification',)
  
    def __str__(self):
        return f"{self.etudiant} {self.chambre}"
    