import uuid
from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name="Nome da Tecnologia")
    icon = models.FileField(
        upload_to='portfolio/images/icons/', 
        blank=True, 
        null=True, 
        verbose_name="Ícone (SVG ou PNG)"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
        ordering = ['name']


class AboutMe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Seu Nome")
    bio = models.TextField(verbose_name="Texto Sobre Mim")
    slug = models.SlugField(max_length=120, unique=True)
    profile_picture = models.ImageField(upload_to='portfolio/images/perfil/', blank=True, null=True, verbose_name="Foto de Perfil")
    email = models.EmailField(max_length=255, verbose_name="Email de contato")
    github_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do GitHub")
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do LinkedIn")
    skills = models.ManyToManyField(Technology, related_name="skills_user", verbose_name="Tecnologias que utilizo")

    def __str__(self):
        return f"Perfil de {self.name}"

    class Meta:
        verbose_name = "Sobre Mim"
        verbose_name_plural = "Sobre Mim"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, verbose_name="Título do Projeto")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="Slug da URL")    
    description = models.TextField(verbose_name="Descrição")
    short_description = models.TextField(verbose_name="Descrição curta para a listagem")
    image = models.ImageField(upload_to='portfolio/images/projetos/', verbose_name="Imagem de Capa")
    repository_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do Repositório")
    live_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do Projeto no Ar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    technologies = models.ManyToManyField(Technology, related_name="projects", verbose_name="Tecnologias Utilizadas")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['created_at']


class Formation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=150, verbose_name="Curso / Formação")
    institution = models.CharField(max_length=150, verbose_name="Instituição")
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(blank=True, null=True, verbose_name="Data de Término (Deixe em branco se estiver cursando)")    

    def __str__(self):
        return f"{self.course} - {self.institution}"

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"
        ordering = ['start_date']


class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, verbose_name="Nome do Certificado")
    issuing_organization = models.CharField(max_length=100, verbose_name="Organização Emissora")
    issue_date = models.DateField(verbose_name="Data de Emissão")
    credential_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link da Credencial")

    def __str__(self):
        return f"{self.title} ({self.issuing_organization})"

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"
        ordering = ['-issue_date']
