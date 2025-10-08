from django.urls import path

from apps.views import *

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<str:slug>', ProjectRetrieveAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('articles/', ArticleListAPIView.as_view()),
    path('articles/<str:slug>', ArticleRetrieveAPIView.as_view()),
    path('faq/', FAQListAPIView.as_view()),
    path('certificate/', CertificateListAPIView.as_view()),
    path('settings/', SettingGenericAPiView.as_view()),
    path('calculator/', CalculateGenericAPiView.as_view()),
    path('lead/', LeadGenericAPiView.as_view()),
]
