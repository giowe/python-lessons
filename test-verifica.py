# Se la libreria spalla non e' installata eseguire sul terminale il comando `pip install spalla --user`

from spalla import Verifica # importi la libreria

Verifica.firma("Nome Cognome") # firmi la verifica, questa operazione è obbligatoria almeno una volta

Verifica.stampa_esercizi() # stampa sul terminale l'elenco degli esercizi disponibili in questa verifica

Verifica.stampa_voto() # stampa il vostro voto attuale

es = Verifica.inizia_esercizio(1) # restituisce l'esercizio numero 1

print(es) # mostra la consegna dell'esercizio e i dati sui quali lavorare

print(es.dati) # sono i dati forniti per l'esercizio corrente

es.consegna(x) # dove x è il risultato da voi elaborato per l'esercizio corrente
