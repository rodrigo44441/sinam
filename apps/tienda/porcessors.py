from ..empresa.models import Empresa, Faq, RedesSociales, Nosotros


def processorsdatos(request):
	dic = {'variable' : Empresa.objects.all()}
	return dic


def processorsfaq(request):
	dic = {'variablefaq' : Faq.objects.all()}
	return dic


def processorsredes(request):
	dic = {'variableredes' : RedesSociales.objects.all()}
	return dic


def processorsnosotros(request):
	dic = {'variablenosotros' : Nosotros.objects.all()}
	return dic