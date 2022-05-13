from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from frontend.plugins.form.models import FormPlugin


@plugin_pool.register_plugin
class AccordionPlugin(CMSPluginBase):

    name = "Custom Form"
    model = FormPlugin
    render_template = "form/index.html"
