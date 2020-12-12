from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import ProduitsDispos

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')


class ProduitsDispoSerializer(ModelSerializer):
    class Meta:
        model = ProduitsDispos
        fields = ('id', 'tigID')