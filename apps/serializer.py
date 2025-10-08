from rest_framework.fields import CharField, IntegerField, DictField, FloatField, BooleanField, ListField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Project, Product, Article, FAQ, Certificate, Settings, Lead


class ProjectListModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'slug', 'title', 'cover_image', 'params', 'region')


class ProjectRetrieveModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('slug', 'title', 'gallery', 'params', 'problems', 'problems', 'solution', 'result', 'region')


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('slug', 'name', 'price_form', 'features', 'image')


class ArticleListModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('slug', 'title', 'cover_image', 'published_at')


class ArticleRetrieveModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('slug', 'title', 'body', 'tags', 'cover_image', 'published_at')


class FAQModelSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class CertificateModelSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'title', 'file_url')


class SettingModelSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('phones', 'emails', 'messengers', 'addresses', 'work_hours', 'seo_defaults')


class CladdingSerializer(Serializer):
    type = CharField(required=True)
    thickness_mm = IntegerField(required=True)


class GateSerializer(Serializer):
    type = CharField(required=True)
    with_m = IntegerField(required=True)
    height_m = IntegerField(required=True)
    qty = IntegerField(required=True)


class WindowsSerializer(Serializer):
    qty = IntegerField(required=True)


class CalculatorRequestSerializer(Serializer):
    span_m = FloatField()
    length_m = FloatField()
    height_m = FloatField()
    snow_zone = CharField()
    wind_zone = CharField()
    cladding = CladdingSerializer()
    insulation = CladdingSerializer()
    gates = GateSerializer(many=True)
    windows = WindowsSerializer()
    doors = WindowsSerializer()
    foundation = CharField()
    installation = BooleanField()
    delivery_region = CharField()
    locale = CharField()
    recaptcha_token = CharField()


# apps/serializers.py
class CalculatorResponseSerializer(Serializer):
    price_from = IntegerField()
    price_to = IntegerField()
    currency = CharField()
    steel_tonnage = FloatField()
    lead_time_days = IntegerField()
    bom_summary = ListField(child=CharField())
    note = CharField()


class LeadModelSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'phone', 'message', 'source', 'utm_json')
        read_only_fields = ('id',)
