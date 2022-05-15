from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from frontend.plugins.authorCustomForm.forms import AuthorCustomForm
from frontend.plugins.authorCustomForm.models import \
    AuthorCustomFormPluginModel


@plugin_pool.register_plugin
class AuthorCustomFormPlugin(CMSPluginBase):
    name = "Custom Form (author)"
    module = "learn"
    model = AuthorCustomFormPluginModel
    render_template = "authorCustomForm/index.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(AuthorCustomFormPlugin, self).render(
            context, instance, placeholder)
        request = context.get('request')
        form = AuthorCustomForm()
        context.update({
            'form_author': form,
            'form_action': '',
            'form_method': 'POST'
        })
        return context
