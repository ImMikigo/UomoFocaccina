#--------------------------------------------------------------------------------------------------

from django.db import models

#--------------------------------------------------------------------------------------------------

class Esame (models.Model) :

    id           = models.AutoField     (primary_key = True)

    data_ora     = models.DateTimeField ()
    tipo         = models.CharField     (max_length = 255, default = "prova")
    esito        = models.CharField     (max_length = 255)
    struttura    = models.CharField     (max_length = 255)
    file_referto = models.FileField     (null = True)
    cda2         = models.TextField     (null = True)

    paziente     = models.ForeignKey    ('Paziente', null = True, on_delete = models.CASCADE)

class Paziente (models.Model) :

    codice_fiscale = models.CharField (primary_key = True, max_length = 16)

    nome           = models.CharField (max_length=255)
    cognome        = models.CharField (max_length=255)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------