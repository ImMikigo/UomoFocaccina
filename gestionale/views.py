#--------------------------------------------------------------------------------------------------

import datetime
from random import randint

#--------------------------------------------------------------------------------------------------

from django.http       import HttpResponse, JsonResponse
from gestionale.models import Esame , Paziente

#--------------------------------------------------------------------------------------------------

def index (request) :

    paziente = Paziente.objects.get (codice_fiscale = "AXAXAXAX")

    esame = Esame ()

    esame.data_ora     = datetime.datetime.now ()
    esame.tipo         = 'test'
    esame.esito        = 'esito2'
    esame.struttura    = 'struttura3'
    esame.paziente     = paziente
    
    esame.save ()

    return HttpResponse ("")

#--------------------------------------------------------------------------------------------------

def index2 (request) :

    esami = Esame.objects.all ()

    result = []

    for esame in esami :
        result.append ({
            'data_ora' : str(esame.data_ora),
            'tipo'     : esame.tipo
            })

    return JsonResponse (result, safe = False)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------