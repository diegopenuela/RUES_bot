import urllib
import urllib2
import json


#Usa un numero de NIT (value) y consulta el portal web del RUES Colombia para validar info de la empresa
def getruesdata (value):
	#Request URL
	url = 'http://www.rues.org.co/RUES_Web/Consultas/ConsultaNIT_json'

	#Form Data
	#strNIT=900771183&idTipo=SiColombia
	data = urllib.urlencode({'strNIT':value,'idTipo':'SiColombia'})
	
	#Response
	content = urllib2.urlopen(url=url, data=data).read()
	return content
	

#ITesting: Manual input
nit = raw_input("Enter a valid NIT:")

try:
	#Dictionary - JSON
	ruesdata = json.loads(getruesdata(nit))

	#Validar codigo de error en la respuesta del RUES
	errorcode = str(ruesdata['codigo_error'])

	#Error handling - JSON.  '0000' representa una consulta sin errores.
	if(errorcode=='0000'):
		ruesrows = ruesdata['rows']
		print  'Razon Social:', ruesrows[0]['razSol'], 'Ciudad:', ruesrows[0]['desc_camara']
	else:
		print ruesdata['mensaje_error']

except urllib2.URLError:
	print 'Opps. No se puede establecer conexion con el RUES'



