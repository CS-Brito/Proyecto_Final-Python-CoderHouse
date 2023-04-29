from django.http import HttpResponse
from django.template import Context, Template


def pruebaTemplate(self):
    
    miHtml = open("C:/Users/cs-br/OneDrive/Documentos/Repositorio/Proyecto-Final/dietetica/AppDietetica/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
    