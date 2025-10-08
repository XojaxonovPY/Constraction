from django.db.models import Model, JSONField, BooleanField, CharField, URLField, DateField, Index
from django.db.models import DecimalField, DateTimeField, TextField, IntegerField
from django.db.models.enums import TextChoices


class Project(Model):
    class Type(TextChoices):
        COLD = 'cold', 'Cold'
        WARM = 'warm', 'Warm'
        SANDWICH = 'sandwich', 'Sandwich'
        POLYCARBONATE = 'polycarbonate', 'Polycarbonate'

    slug = CharField(max_length=160, unique=True)
    title = JSONField()
    region = CharField(max_length=120)
    cover_image = URLField()
    gallery = JSONField()
    type = CharField(max_length=32, choices=Type.choices)
    params = JSONField()
    problems = JSONField()
    solution = JSONField()
    result = JSONField()
    commissioned_at = DateField()
    is_published = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['slug'], name='idx_project_slug'),
            Index(fields=['region'], name='idx_project_region'),
            Index(fields=['type'], name='idx_project_type'),
            Index(fields=['is_published'], name='idx_project_published'),
        ]

    def __str__(self):
        return self.title.get("ru") or self.title.get("uz") or str(self.slug)


class Product(Model):
    class Type(TextChoices):
        COLD = 'cold', 'Cold'
        WARM = 'warm', 'Warm'
        SANDWICH = 'sandwich', 'Sandwich'
        POLYCARBONATE = 'polycarbonate', 'Polycarbonate'

    slug = CharField(max_length=160, unique=True)
    name = JSONField()
    description = JSONField()
    features = JSONField(default=list)
    image = URLField()
    price_form = DecimalField(max_digits=10, decimal_places=2)
    type = CharField(max_length=32, choices=Type.choices)
    is_published = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['slug'], name='idx_product_slug '),
            Index(fields=['type'], name='idx_product_type'),
            Index(fields=['is_published'], name='idx_product_published')
        ]

    def __str__(self):
        return self.name.get("ru") or self.name.get("uz") or str(self.slug)


class Article(Model):
    slug = CharField(max_length=160, unique=True)
    title = JSONField()
    body = TextField()
    tags = JSONField()
    cover_image = URLField()
    published_at = DateField()
    is_published = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['slug'], name='idx_article_slug '),
            Index(fields=['published_at'], name='idx_article_published_at'),
            Index(fields=['is_published'], name='idx_article_published')
        ]

    def __str__(self):
        return self.title.get("ru") or self.title.get("uz") or str(self.slug)


class FAQ(Model):
    question = JSONField()
    answer = JSONField()
    order = IntegerField(default=0)
    is_published = BooleanField(default=True)

    class Meta:
        indexes = [
            Index(fields=['order'], name='idx_faq_order'),
            Index(fields=['is_published'], name='idx_faq_published')
        ]


class Certificate(Model):
    title = JSONField()
    file_url = URLField()
    order = IntegerField(default=0)
    is_published = BooleanField(default=True)

    class Meta:
        indexes = [
            Index(fields=['order'], name='idx_certificate_order'),
            Index(fields=['is_published'], name='idx_certificate_published')
        ]

    def __str__(self):
        return self.title.get("ru") or self.title.get("uz")


class Settings(Model):
    phones = JSONField()
    emails = JSONField()
    messengers = JSONField()
    addresses = JSONField()
    work_hours = JSONField()
    seo_defaults = JSONField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)


class Lead(Model):
    class StatusType(TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in progress', 'In progress'
        DONE = 'done', 'Done'

    class SourceType(TextChoices):
        HERO = 'hero', 'Hero'
        CONTACT = 'contact', 'Contact'
        CALCULATOR = 'calculator', 'Calculator'

    name = CharField(max_length=120)
    phone = CharField(max_length=64)
    social = CharField(max_length=128)
    message = TextField()
    source = CharField(max_length=32, choices=SourceType.choices)
    utm_json = JSONField()
    status = CharField(max_length=32, choices=StatusType.choices, default=StatusType.NEW)
    taken_by_tg_user_id = CharField(max_length=64)
    telegram_chat_id = CharField(max_length=64)
    telegram_message_id = CharField(max_length=64)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['status'], name='idx_lead_status'),
            Index(fields=['source'], name='idx_lead_source'),
            Index(fields=['created_at'], name='idx_lead_created_at'),
        ]
