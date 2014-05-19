from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from election.views import vote_ajax_info,ajax_get_result
from login.views import register,mylogin,mylogout,homepage,changepassword,ajax_get_json
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyLogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^register/$',register),
    (r'^login/$',mylogin),
    (r'^logout/$',mylogout),
    (r'^login/register/$',register),
    (r'^homepage/$',homepage),
    (r'^changepassword/(?P<username>\w+)/$',changepassword),
    url(r'^login/ajax_get_json/$',ajax_get_json,name="ajax_get_json"),
    url(r'^election/vote_ajax_info/$',vote_ajax_info,name="vote_ajax_info"),
    url(r'^election/ajax_get_result/$',ajax_get_result,name="ajax_get_result"),
    url(r'blog/', include('Election.blog.urls')),
    url(r'election/',include('Election.election.urls')),
    url(r'^captcha/', include('Election.captcha.urls')),
   )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
