from django.contrib import admin
from .models import Technology, Project, AboutMe, Formation, Certificate

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'live_url')
    search_fields = ('title', 'description')
    list_filter = ('technologies', 'created_at')
    filter_horizontal = ('technologies',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'slug')
    filter_horizontal = ('skills',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('course', 'institution', 'start_date', 'end_date')
    search_fields = ('course', 'institution')
    list_filter = ('institution',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date')
    search_fields = ('title', 'issuing_organization')
    list_filter = ('issuing_organization',)