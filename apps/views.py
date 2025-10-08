from http import HTTPStatus

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response

from apps.models import Project, Product, Article, FAQ, Certificate, Settings
from apps.pagenation import ProjectPagination
from apps.serializer import CalculatorResponseSerializer, CalculatorRequestSerializer
from apps.serializer import CertificateModelSerializer, SettingModelSerializer, LeadModelSerializer
from apps.serializer import ProductModelSerializer, ArticleListModelSerializer, ArticleRetrieveModelSerializer
from apps.serializer import ProjectListModelSerializer, ProjectRetrieveModelSerializer, FAQModelSerializer


@extend_schema(tags=['projects'], parameters=[
    OpenApiParameter(name='region', type=str),
    OpenApiParameter(name='type', type=str, enum=Project.Type.values, description="Filter by type")

])
class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListModelSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        region = self.request.query_params.get('region')
        type_ = self.request.query_params.get('type')
        if region:
            queryset = queryset.filter(region__iexact=region)
        if type_:
            queryset = queryset.filter(type=type_)
        return queryset.order_by('-created_at')


@extend_schema(tags=['products'])
class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectRetrieveModelSerializer
    lookup_field = 'slug'


@extend_schema(tags=['products'])
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


@extend_schema(tags=['articles'], parameters=[
    OpenApiParameter(name='tag', type=str),
])
class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.filter(is_published=True).order_by('-published_at')
    serializer_class = ArticleListModelSerializer
    pagination_class = ProjectPagination  # yoki boshqa pagination

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__contains=[tag])
        return queryset  # ✅ majburiy


@extend_schema(tags=['articles'])
class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleRetrieveModelSerializer
    lookup_field = 'slug'


@extend_schema(tags=['faq'])
class FAQListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer


@extend_schema(tags=['certificates'])
class CertificateListAPIView(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateModelSerializer


@extend_schema(tags=['settings'])
class SettingGenericAPiView(GenericAPIView):
    serializer_class = SettingModelSerializer

    def get(self, request):
        setting = Settings.objects.first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)


@extend_schema(tags=['calculator'], responses=CalculatorResponseSerializer)
class CalculateGenericAPiView(GenericAPIView):
    serializer_class = CalculatorRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        base_price = 50000 + (data['span_m'] * data['length_m'] * 10)
        price_from = int(base_price * 1.04)
        price_to = int(base_price * 1.35)
        response_data = {
            "price_from": price_from,
            "price_to": price_to,
            "currency": "USD",
            "steel_tonnage": round(data['span_m'] * data['length_m'] * 0.02, 2),
            "lead_time_days": 35,
            "bom_summary": ["Каркас", "Покрытие", "Фурнитура", "Ворота", "Фундамент"],
            "note": "Расчёт предварительный. Точная цена после проектных работ."
        }
        return Response(response_data, status=HTTPStatus.OK)


@extend_schema(tags=['lead'])
class LeadGenericAPiView(GenericAPIView):
    serializer_class = LeadModelSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok'}, status=HTTPStatus.CREATED)
