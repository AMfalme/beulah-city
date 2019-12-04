from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.core.fields import RichTextField

from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


from wagtail.contrib.settings.models import BaseSetting, register_setting

 

class HomePage(Page):
    body = models.CharField(max_length=250, blank=True)
    intro = models.CharField(max_length=250, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    def get_context(self, request):
        projectpages = self.get_children().type(ProjectPage).live()
        context = super(HomePage, self).get_context(request)
        context['projectpages'] = projectpages
        return context


class AboutPage(Page):
    body = models.CharField(max_length=250, blank=True)
    intro = models.CharField(max_length=250, blank=True)
    hero_intro = RichTextField(blank=True)
    about_title = models.TextField(default="Who we are")
    about_paragraph = models.TextField(blank=True)
    projects_overview_title = models.TextField(blank=True)
    projects_overview = models.TextField(blank=True)
    company_overview = models.TextField(blank=True)
    company_overview_paragraph = models.TextField(blank=True)
    company_overview_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    company_pride = models.TextField(blank=True)
    company_pride_paragraph = models.TextField(blank=True)
    company_pride_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero_intro'),
        FieldPanel('about_title'),
        FieldPanel('about_paragraph'),
        FieldPanel('projects_overview_title'),
        FieldPanel('projects_overview'),
        InlinePanel('overview_images', label="Project Details"),
        FieldPanel('company_overview'),
        FieldPanel('company_overview_paragraph'),
        ImageChooserPanel('company_overview_image'),
        FieldPanel('company_pride'),
        FieldPanel('company_pride_paragraph'),
        ImageChooserPanel('company_pride_image')

    ]


class OverviewImages(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.SET_NULL,
                       null=True, related_name='overview_images')
    overview_name = models.TextField(default="P")
    overview_info = models.TextField(blank=True)
    overview_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    panels = [
        FieldPanel('overview_name'),
        FieldPanel('overview_info'),
        ImageChooserPanel('overview_image')
    ]


class ProjectPage(Page):
    project_welcome_title = models.TextField(default="Welcome to")
    project_title = models.TextField(default="Inclusionary space design")
    project_description = models.TextField(default="")
    css_strings = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    project_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    project_information_title = models.TextField(blank=True)
    project_information = models.TextField(blank=True)
    hero_intro = RichTextField(blank=True)
    project_intro = models.TextField(blank=True)
    project_body = RichTextField(blank=True)
    project_image_bottom_section = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    project_pride = models.TextField(blank=True)
    project_pride_paragraph = models.TextField(blank=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        FieldPanel('project_welcome_title'),
        FieldPanel('project_title'),
        FieldPanel('project_description'),
        FieldPanel('css_strings'),
        ImageChooserPanel('project_image'),
        MultiFieldPanel(
            [
                FieldPanel('hero_intro'),
                FieldPanel('project_intro'),
                FieldPanel('project_body'),
                InlinePanel('projects', label="Project map"),

            ]
        ),

        InlinePanel('project_details', label="Project Details"),
        FieldPanel('project_information_title'),
        FieldPanel('project_information'),
        ImageChooserPanel('project_image_bottom_section'),
        FieldPanel('project_pride'),
        FieldPanel('project_pride_paragraph'),
    ]


class Projects(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.SET_NULL,
                       null=True, related_name='projects')
    project_name = models.TextField(blank=True)
    project_info = models.TextField(blank=True)
    project_info_size = models.TextField(blank=True)
    project_paragraph = models.TextField(blank=True)
    project_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    project_brochure = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        FieldPanel('project_name'),
        FieldPanel('project_info'),
        FieldPanel('project_info_size'),
        ImageChooserPanel('project_image'),
        FieldPanel('project_paragraph'),
        DocumentChooserPanel('project_brochure'),
    ]


class Details(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.SET_NULL,
                       null=True, related_name='project_details')
    detail_name = models.TextField(default="P")
    detail_info = models.TextField(blank=True)
    panels = [
        FieldPanel('detail_name', classname="col6"),
        FieldPanel('detail_info', classname="col6"),
    ]


class EnquiryField(AbstractFormField):
	page = ParentalKey('EnquiryPage', on_delete=models.CASCADE, related_name="custom_form_fields")


class EnquiryPage(AbstractEmailForm):
	body = models.CharField(blank=True, max_length=250)
	intro = models.CharField(blank=True, max_length=250)
	terms = RichTextField(blank=True)
	submit = models.CharField(default = "Subscribe", max_length=100)
	content_panels = AbstractEmailForm.content_panels + [
		InlinePanel('custom_form_fields', label= "Enquiry Form"),
		FieldPanel('intro', classname="full"),
		FieldPanel('terms', classname="full"),
		FieldPanel('submit', classname="full")

	] 
	def get_form_fields(self):
		return self.custom_form_fields.all()


@register_setting
class EnquiryFormSetting(BaseSetting):
	enquiry_form_page = models.ForeignKey(
		'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+'
	)
	panels = [
		PageChooserPanel('enquiry_form_page', ['home.EnquiryPage']),
	]

	def view(request):
		custom_form = EnquiryFormSetting.for_site(request.site)