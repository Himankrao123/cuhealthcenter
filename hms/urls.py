# from django.contrib import admin
from django.urls import path
# from django.urls.conf import include
from hms import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [    
    path("", views.index, name="index"),
    path("service", views.service, name="service"),
    path("contact_us", views.contactus, name="contactus"),
    path("accounts/<slug:slug>", views.accounts, name="signednup"),
    path("logout",views.logoutacc,name="logoutacc"),
    path("profile", views.profile, name="profile"),
    path("newappointment", views.newappointment , name="newappointment"),
    path("documents", views.documents , name="documents"),
    path("update/<slug:slug>", views.update, name="update"),
    path("doctor/<slug:slug>",views.docinfo,name="docinfo"),
    path("profile/edit",views.profileedit,name="profileedit"),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)