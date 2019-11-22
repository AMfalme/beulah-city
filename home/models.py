from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = models.CharField(max_length=250, blank=True)	
    intro = models.CharField(max_length=250, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    def get_context(self, request):
        projectpages = self.get_children().live()
        context = super(HomePage, self).get_context(request)
        context['projectpages'] = projectpages
        return context
    


class ProjectPage(Page):
    project_welcome_title = models.TextField(default="Welcome to")
    project_title = models.TextField(default="Inclusionary space design")
    project_description = models.TextField(default="")
    css_strings = models.TextField(blank=True)
    project_image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.SET_NULL,null= True, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('project_welcome_title'),
        FieldPanel('project_title'),
        FieldPanel('project_description'),
        FieldPanel('css_strings'),
        ImageChooserPanel('project_image')
    ]

    def first_project_active(self):
        first_page = self.get_children().live().first()
        return first_page