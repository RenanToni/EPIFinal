"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.frente),
    path('cadastrarEPI/', views.cadastrarEPI),
    path('atualizarEPI/<int:id>', views.atualizarEPI),
    path('cadastrarColaborador/', views.cadastrarColaborador),
    path('atualizarColaborador/<int:id>', views.atualizarColaborador),
    path('registrar/', views.registrar),
    path('relatorioEPI/', views.relatorioEPI),
    path('relatoriosColaborador/', views.relatorioColaborador),
    path('colaboradorAtualizar', views.colaboradorAtualizar),
    path('EPIatualizar', views.EPIatualizar),
    path('deletarEPI/<int:id>', views.deletarEPI),
    path('deletarColaborador/<int:id>', views.deletarColaborador),
    path('atualizarRegistro/<int:id>', views.atualizarRegistro),

]
