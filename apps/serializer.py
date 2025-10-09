from rest_framework.fields import CharField, IntegerField, FloatField, BooleanField, ListField
from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField

from apps.models import Project, Product, Article, FAQ, Certificate, Settings, Lead

from rest_framework import serializers


class I18NModelSerializer(serializers.ModelSerializer):
    def get_i18n_value(self, value_dict):
        request = self.context.get("request")
        if not isinstance(value_dict, dict):
            return value_dict
        lang = getattr(request, "LANGUAGE_CODE", None)
        if not lang:
            if request and request.query_params.get("lang"):
                lang = request.query_params.get("lang")
            elif request and request.headers.get("Accept-Language"):
                lang = request.headers.get("Accept-Language").split(",")[0].split("-")[0]
        lang = lang or "uz"
        return value_dict.get(lang, value_dict.get("uz") or value_dict.get("ru"))


class ProjectListModelSerializer(I18NModelSerializer):
    title = SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'slug', 'title', 'cover_image', 'params', 'region')

    def get_title(self, obj):
        return self.get_i18n_value(obj.title)


class ProjectRetrieveModelSerializer(I18NModelSerializer):
    title = SerializerMethodField()
    problems = SerializerMethodField()
    solution = SerializerMethodField()
    result = SerializerMethodField()

    class Meta:
        model = Project
        fields = ('slug', 'title', 'gallery', 'params', 'problems', 'solution', 'result', 'region')

    def get_title(self, obj):
        return self.get_i18n_value(obj.title)

    def get_problems(self, obj):
        return self.get_i18n_value(obj.problems)

    def get_solution(self, obj):
        return self.get_i18n_value(obj.solution)

    def get_result(self, obj):
        return self.get_i18n_value(obj.result)


class ProductModelSerializer(I18NModelSerializer):
    name = SerializerMethodField()
    description = SerializerMethodField()
    features = SerializerMethodField()

    class Meta:
        model = Product
        fields = ('slug', 'name', 'description', 'price_form', 'features', 'image')

    def get_name(self, obj):
        return self.get_i18n_value(obj.name)

    def get_description(self, obj):
        return self.get_i18n_value(obj.description)

    def get_features(self, obj):
        return self.get_i18n_value(obj.features)


class ArticleListModelSerializer(I18NModelSerializer):
    title = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('slug', 'title', 'cover_image', 'published_at')

    def get_title(self, obj):
        return self.get_i18n_value(obj.title)


class ArticleRetrieveModelSerializer(I18NModelSerializer):
    title = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('slug', 'title', 'body', 'tags', 'cover_image', 'published_at')

    def get_title(self, obj):
        return self.get_i18n_value(obj.title)


class FAQModelSerializer(I18NModelSerializer):
    question = SerializerMethodField()
    answer = SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')

    def get_question(self, obj):
        return self.get_i18n_value(obj.question)

    def get_answer(self, obj):
        return self.get_i18n_value(obj.answer)


class CertificateModelSerializer(I18NModelSerializer):
    title = SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ('id', 'title', 'file_url')

    def get_title(self, obj):
        return self.get_i18n_value(obj.title)


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
