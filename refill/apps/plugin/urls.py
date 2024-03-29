from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "plugin/main.html"}, name="annex"),
    url(r"^(?P<project-slug>\d+)$", direct_to_template, {"template": "plugin/plugin.html"}, name="plugin"),
    url(r"^(?P<project-slug>\d+)/downloads$", direct_to_template, {"template": "plugin/download-main.html"}, name="downloadannex"),
    url(r"^(?P<project-slug>\d+)/downloads/(?P<artifact-id>\d+)$", direct_to_template, {"template": "plugin/download-artifact.html"}, name="artifactdnld"),
	url(r"^stats/(?P<display_string>\d+)/$", 'plugin.views.text_image'),
)
