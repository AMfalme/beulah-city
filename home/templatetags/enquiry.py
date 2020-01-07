from django import template
from home.models import EnquiryFormSetting
from home.models import ContactFormSetting
register = template.Library()


@register.simple_tag(takes_context=True)
def get_enquiry_form(context):
    request = context['request']
    my_custom_settings = EnquiryFormSetting.for_site(request.site)
    feedback_form_page = my_custom_settings.enquiry_form_page.specific
    form = feedback_form_page.get_form(
        page=feedback_form_page, user=request.user)
    title = feedback_form_page.title
    body = feedback_form_page.intro
    terms = feedback_form_page.terms
    submit = feedback_form_page.submit
    return {'page': feedback_form_page, 'form': form, 'title': title, 'body': body, 'terms': terms, 'submit': submit}





@register.simple_tag(takes_context=True)
def get_contact_form(context):
    request = context['request']
    my_custom_settings = ContactFormSetting.for_site(request.site)
    feedback_form_page = my_custom_settings.contact_form_page.specific
    form = feedback_form_page.get_form(
        page=feedback_form_page, user=request.user)
    title = feedback_form_page.title
    body = feedback_form_page.intro
    submit = feedback_form_page.submit
    return {'page': feedback_form_page, 'form': form, 'title': title, 'body': body, 'submit': submit}