#!/home/luotajyz/public_html/cgi-bin/ties4080/vt2/venv/bin/python
#muuta edelliselle riville oikea polku omaan venv-ympÃ¤ristÃ¶Ã¶n
# -*- coding: utf-8 -*-
# suorittaa Flask-sovellukset CGI-ohjelmina users.jyu.fi-palvelimella
import sys
from wsgiref.handlers import CGIHandler
from werkzeug.debug import DebuggedApplication

try:
  from vt2 import app as application

  if __name__ == '__main__':
         handler = CGIHandler()
         application.debug = True
         handler.run(DebuggedApplication(application))

except:
  #koska tÃ¤nne pÃ¤Ã¤dyttÃ¤essÃ¤ ei werkzeug toimi tÃ¤ytyy itse tulostaa http-protokollan
  #edellyttÃ¤mÃ¤ otsake. STDOUT menee tÃ¤ssÃ¤ tapauksessa suoraan selaimelle
  print("Content-Type: text/plain;charset=UTF-8\n")
  print("Syntaksivirhe:\n")
  for err in sys.exc_info():
        print(err)
