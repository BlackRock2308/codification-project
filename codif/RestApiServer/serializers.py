from rest_framework import serializers
from .models import Etudiant, EtudiantPayment, Codification, Chambre, Pavillon


class PavillonSerializer(serializers.ModelSerializer):
    chambres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pavillon
        fields = '__all__'


class ChambreSerializer(serializers.ModelSerializer):
    pavillon = serializers.StringRelatedField(many=False)

    class Meta:
        model = Chambre
        fields = (
            'id',
            'numero_chambre',
            'etage',
            'occupee',
            'pavillon'
        )

class EtudiantSerializer(serializers.ModelSerializer):
    payments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Etudiant
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtudiantPayment
        fields = '__all__'


class CodificationSerializer(serializers.ModelSerializer):
    # chambre = serializers.StringRelatedField(many=False)
    # etudiant = serializers.StringRelatedField(many=False)

    class Meta:
        model = Codification
        fields = (
            'id',
            'date_codification','annee_scolaire',
            'etudiant','chambre'
        )