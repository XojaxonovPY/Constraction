from django.contrib import admin
from .models import (
    Project, Product, Article, FAQ,
    Certificate, Settings, Lead
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'region', 'type', 'is_published', 'created_at')
    list_filter = ('region', 'type', 'is_published')
    search_fields = ('slug', 'title__ru', 'title__uz')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def display_title(self, obj):
        return obj.title.get("ru") or obj.title.get("uz") or obj.slug

    display_title.short_description = "Title"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'type', 'price_form', 'is_published', 'created_at')
    list_filter = ('type', 'is_published')
    search_fields = ('slug', 'name__ru', 'name__uz')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def display_name(self, obj):
        return obj.name.get("ru") or obj.name.get("uz") or obj.slug

    display_name.short_description = "Name"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'published_at', 'is_published', 'created_at')
    list_filter = ('is_published', 'published_at')
    search_fields = ('slug', 'title__ru', 'title__uz', 'tags')
    ordering = ('-published_at',)
    readonly_fields = ('created_at', 'updated_at')

    def display_title(self, obj):
        return obj.title.get("ru") or obj.title.get("uz") or obj.slug

    display_title.short_description = "Title"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_question', 'order', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('question__ru', 'question__uz')
    ordering = ('order',)

    def display_question(self, obj):
        return obj.question.get("ru") or obj.question.get("uz")

    display_question.short_description = "Question"


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'order', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title__ru', 'title__uz')
    ordering = ('order',)

    def display_title(self, obj):
        return obj.title.get("ru") or obj.title.get("uz")

    display_title.short_description = "Title"


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'source', 'status', 'created_at')
    list_filter = ('status', 'source')
    search_fields = ('name', 'phone', 'social', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
