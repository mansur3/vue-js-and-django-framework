"""
URL configuration for banker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/banner/', include('bank.urls')),
    path('api/service/', include('service.urls')),
    path('api/about-us/', include('aboutus.urls')),
    path('api/team-member/', include('team_member.urls')),
    path('api/gallery/', include('gallery_data.urls')),
    path('api/work-flow/', include('work_flow.urls')),
    path('api/service-section/', include('service_section.urls')),
    path('api/testimonial/', include('testimonial.urls')),
    path('api/contact-us', include('contact_us.urls'))
]
