#LUCA PALMIERI E RICCARDO MALAVOLTI 26/01/17
print("la tua missione se vorrai accettarla sara di infiltrarti in un sottomarino russo e di rubare piani militari")
print()
nome = input("nome agente: ")
print()
print()
print("ti trovi a circa 5 miglia dall'obiettivo")
print("devi scegliere come entrarci")
print("A. dal portellone principale")
print("B. dal vano per i missili")
risposta1 = input().upper()

if risposta1 == "A":
  print("entrando, hai fatto scattare l'allarme, ora i soldati ti stanno cercando")
  print("i piani si trovano nel centro di comando")
  print("ti trovi davanti a tre percorsi")
  print("in quale vai?")
  print("A. porta davanti a te")
  print("B. corridoio a destra")
  print("C. corridoio a sinistra")
  risposta2 = input().upper()
  
  if risposta2 == "A":
    print("appena superata la porta, si attiva il blocco delle porte")
    print("quindi devi andare a cercare il pannello di controllo al piano di sotto per sbloccare le porte \nprima di poter arrivare alla sala comando")
    print("trovi per terra un pass per entrare nell'armeria")
    print("sei davanti alle scale ,al piano di sopra c'e' l'armeria")
    print("A. scendi")
    print("B. sali")
    risposta3 = input().upper()
        
    if risposta3 == "A":
      print("vedi da lontano la porta del pannello di controllo ma ci sono due guardie davanti alla porta \noltre a due che ti si avvicinano da dietro \ndevi scegliere in fretta")
      print("l'unica tua arma e' la tua forza, pero' vedi un condotto dell'aria alla tua destra")
      print("A. tenti uno scontro fisico")
      print("B. ti infili nel condotto dell'aria")
      risposta4 = input().upper()
		 
      if risposta4 == "A" :
        print("riesci a disarmare tre guardie [prendendo le armi] e ad entrare nella stanza ma un uomo [ancora armato] assedia la porta") 
        print("riesci a sbloccare le porte e di conseguenza altri uomini, sentendo degli spari, possono raggiungerti")
        print("blocchi le comunicazioni con la radio")		   
        input("premi invio per sfondare la porta e fare fuoco")
        print("hai bloccato la prima squadra ma tra poco ne arriveranno altre")
        print("devi andartene!!!!!")
        print("A. percorri 2 piani e vai nell'armeria")
        print("B. ti nascondi in una delle stanze")
        print("C. continui a correre imbracciando il fucile")
        risposta5 = input().upper()
  
        if risposta5 == "A" or risposta3 == "B":
          print("raggiungi l'armeria, prendi e ricarichi le armi")
          print("sei pronto all'irruzione nel centro di comando")
          print("A. dalla botola sul pavimento")
          print("B. dalla tromba dell'ascensore")
          risposta6 = input().upper()

          if risposta6 == "A":
            print("ti trovi proprio sotto la botola ma una valigetta ti blocca l'uscita")
            print("se apri la botola la valigia fara' rumore e attirera' i soldati su di te")
            print("A: esci ugualmente")
            print("B. torni indietro e cerchi un'altra entrata")
            risposta7 = input().upper()
     
            if risposta7 == "A":
              print("con un movimento rapido riesci ad aprire la botola e a non far cadere la valigia")
              print("ora che sei nel centro di comando devi neutralizzare la combinazione della cassa forte per prendere i piani")
              print("A. cerchi di sottrarre la chiave al collo del capitano")
              print("B. fai fuoco sulla ciurma")
              print("C. forzi la serratura della cassa forte")
              risposta8 = input().upper()
            
              if risposta8 == "A":
                print("muovendoti furtivamente ti nascondi nella cabina del capitano e attendi che arrivi")
                print("spegni la luce e aspetti che qualcuno entri")
                print("dopo alcune ore, improvvisamente entra una persona nella stanza")
                print("il fucie e' troppo lontano")
                print("che cosa fai?!?!?!")
                print("A. prendi la coperta del letto e la lanci conto di lui")
                print("B. ti lanci contro di lui cercando di atterrarlo")
                print("C. ti butti sotto il letto")
                risposta9 = input().upper()
         
                if risposta9 == "A":
                  print("afferri la coperta, lo blocchi e lo leghi per terra")
                  print("ti accorgi che pero' non e' il capitano")
                  print("fortunatamente sei riuscito a bendare e a imbavagliare l'uomo ma non sai cos'altro fare")				  
                  print("A. gli rubi l'uniforme e entri nel centro i comando")
                  print("B. togli il bavaglio all'uomo per farti dire dove si trova la chiave di riserva")
                  print("C. torni nel centro di comando e minacci tutti con una granata a salve")
                  risposta10 = input().upper()
			      
                  if risposta10 == "A":
                    print("in questo momento puoi aggirarti liberamente per i corridoii")
                    print("devi cercare informazioni per capire dove si trova il comandante")
                    print("A. chiedi al addetto al telescopio")
                    print("B. chiedi al armiere")
                    print("C. chiedi al primo ufficiale")
                    risposta11 = input().upper()
                    
                    if risposta11 == "A":
                      print("il mio unico compito e' guardare, non faccio altro")
                      print()
                      print("B. chiedi al armiere")
                      print("C. chiedi al primo ufficiale")
                      risposta12 = input().upper()
                      
                      if risposta12 == "B":
                        print("in questo periodo non posso sparare a nessuno che rabbia!!!!")
                        print()
                        print("C. chiedi al primo ufficiale")
                        risposta13 = input().upper()
			            
                        if risposta13 == "C":
                          print("mediamente il capitano va a mensa alle 13:30")
                          print("TU: che ore sono?")
                          print("12:45")
							
                      if risposta12 == "C":
                        print("mediamente il capitano va a mensa alle 13:30")
                        print("TU: che ore sono?")
                        print("12:45") 					
						  
                    if risposta11 == "B":
                      print("A. chiedi al addetto al telescopio")
                      print("C. chiedi al primo ufficiale")
                      risposta14 = input().upper()
					  
                      if risposta14 == "A":
                        print("il mio unico compito e' guardare, non faccio altro")
                        print()
                        print("C. chiedi al primo ufficiale")
                        risposta15 = input().upper()
						
                        if risposta15 == "C":
                          print("mediamente il capitano va a mensa alle 13:30")
                          print("TU: che ore sono?")
                          print("12:45")
						  
                      if risposta14 == "C":
                        print("mediamente il capitano va a mensa alle 13:30")
                        print("TU: che ore sono?")
                        print("12:45")					  
					  
					  
                    if risposta11 == "C":
                      print("mediamente il capitano va a mensa alle 13:30")
                      print("TU: che ore sono?")
                      print("12:45")
			    
                    print("ora che hai scoperto dove si trova il capo non ti resta che sottrarli la chiave")
                    print()
                    print()
                    print("sei riuscito a sottrarli la chiave facendo finta di pulirli la giacca dopo averliela sporcata")
                    print()
                    print()
                    print()
                    print()
					
                  if risposta10 == "B":
                    print("l'uomo sotto tua minaccia ti rivela che il comandante pranza alle 13:00")
                    print("tu guardi l'ora e vedi che manca poco piu' di un quarto d'ora")
                    print("ti dirigi in mensa, senza grandi difficolta' riesci a sottrarli la chiave")
					
                  if risposta10 == "C":
                    print("minacciandoli, prendi una ragazza e la tieni come ostaggio")
                    print("il primo ufficiale ti dice che il capitano si trova in mensa")
                    print("stai sigillando la porta ma pensi cosa fare con la ragazza")
                    print("A. la lasci con gli altri della ciurma")
                    print("B. la porti con te in mensa")
                    risposta16 = input().upper()
					
                    if risposta16 == "A":
                      print("corri in mensa e tramite uno strtagemma riesci a sottrarli i codici")
					  
                    if risposta16 == "B":
                      print("ti dirigi in mensa con la ragazza e la usi come ostaggio")
                      print("il capitano ti consegna la chiave e tu riesci a uscire dal sottomarino con i codici")

                if risposta9 == "B":
                  print("mentre stai correndo contro di lui, lui si accorge di te")
                  print("ti afferra e ti lancia per terra")
                  print("estrae la pistola e fa fuoco")
                  print("agente" + nome + " morto sul campo")
				
                if risposta9 == "C":
                  print("prendendo il fucile ti lanci sotto al letto ma lui si accorge di te")
                  print("ti afferra per la gola")
                  print("premi X per liberarti")
                  input("riesci a liberarti e a farlo svenire con un pugno")
                  print("gli rubi l'uniforme....ora ti puoi aggirare rapidamente nel sottomarino")
                  print("devi cercare informazioni per capire dove si trova il comandante")
                  print("A. chiedi al addetto al telescopio")
                  print("B. chiedi al armiere")
                  print("C. chiedi al primo ufficiale")
                  risposta17 = input().upper()
                    
                  if risposta17 == "A":
                      print("il mio unico compito e' guardare, non faccio altro")
                      print()
                      print("B. chiedi al armiere")
                      print("C. chiedi al primo ufficiale")
                      risposta18 = input().upper()
                      
                      if risposta18 == "B":
                        print("in questo periodo non posso sparare a nessuno che rabbia!!!!")
                        print()
                        print("C. chiedi al primo ufficiale")
                        risposta19 = input().upper()
			            
                        if risposta19 == "C":
                          print("mediamente il capitano va a mensa alle 13:30")
                          print("TU: che ore sono?")
                          print("12:45")
							
                      if risposta18 == "C":
                        print("mediamente il capitano va a mensa alle 13:30")
                        print("TU: che ore sono?")
                        print("12:45") 					
						  
                  if risposta17 == "B":
                      print("A. chiedi al addetto al telescopio")
                      print("C. chiedi al primo ufficiale")
                      risposta20 = input().upper()
					  
                      if risposta20 == "A":
                        print("il mio unico compito e' guardare, non faccio altro")
                        print()
                        print("C. chiedi al primo ufficiale")
                        risposta21 = input().upper()
						
                        if risposta21 == "C":
                          print("mediamente il capitano va a mensa alle 13:30")
                          print("TU: che ore sono?")
                          print("12:45")
						  
                      if risposta20 == "C":
                        print("mediamente il capitano va a mensa alle 13:30")
                        print("TU: che ore sono?")
                        print("12:45")					  
					  
					  
                  if risposta17 == "C":
                      print("mediamente il capitano va a mensa alle 13:30")
                      print("TU: che ore sono?")
                      print("12:45")

              if risposta8 == "B":
                print("inizi col sparare per terra per spaventare i soldati")
                print("li minacci afferrando uno degli ufficiali")
                print("il capitano si fa avanti consegnandoti la combinazione della cassa forte")
                print()
                print("sei riuscito ad ottenere i codici....complimenti!!")
           
              if risposta8 == "C":
                print("sei riuscito a sentire che la cassa forta si trova nella cabina del capitano")
                print("ti dirigi nella stanza, estrai la cassa forte")
                print("A. cerchi un uscita dal sottomarino con la cassa forte ancora chiusa")
                print("B. cerchi di forzare la serratura")
                risposta22 = input().upper()
				
                if risposta22 == "A":
                  print("stai per uscire da dove sei entrata ma ti cade la cassa forte per terra")
                  print("il rumore attira l'attenzione dei soldati che convergono su di te e ti catturano")
                  print("il soldato " + nome + ", e' deceduto sul campo")				  
				
                if risposta22 == "B":
                  print("devi cercare l'oggetto migliore per romperla")
                  print("A. il martello")
                  print("B. una 'parete'")
                  print("C. ' l'acqua '")
                  risposta23 = input().upper()
				  
                  if risposta23 =="A":
                    print("colpendolo ripetutamente non riesci ad aprire la serratura")
                    print("aumentando la forza, aumenti anche il rumore e per cio' attiri l'attenzione")
                    print("i soldati convergono su di te e ti catturano")
                    print("il soldato " + nome + ", e' deceduto sul campo")	
				  
                  if risposta23 == "B":
                    print("appoggi un materasso contro la porta e scagli la cassaforte contro uno spigolo")
                    print("il materasso attutisce il rumore")
                    print("la cassa forte fortunatamente si apre e riesci ad ottenere i codici")

                  if risposta23 == "C":
                    print("riesci a friggere il sistema elettrico e di conseguenza riesci ad aprire la cassaforte")
                    print("tuttavia parte del codice e' stato rovinato")
                    print("percio' la missione non e' totalmente completata")

            if risposta7 == "B":
              print("trovi un condotto dell'aria che ti permette di sentire una conversazione in cui il capitano \n parla al primo ufficiale")
              print("senti che i primi tre numeri sono 16 06 68 88 X 98 ")
              print("cerchi la cassaforte in giro nel sottomarino")
              print()
              print()
              print("dopo alcune ore la trovi nella cabina del capitano")
              print("cerchi di inserire la combinazione")
              print("se inserisci un numero sbagliato scattera' l'allarme")
              print()
              print("A. 95")
              print("B. 97")
              print("C. 96")
              print("D. 87")
              print("E. 89")
              print("F. 90")
              risposta24 = input().upper()
			  
              if risposta24 == "D":
                print("cassaforte sbloccata")
			  
              else:
                print("password sbagliata")
                print("allarme scattata")
                print("missione fallita")

          if risposta6 == "B":
            print("sei nella tromba dell'ascensore e stai osservando il centro di controllo")
            print("ma ad un certo punto	senti che l'ascensore si attiva....sta salendo!!!!")
            print("devi scegliere che cosa fare...")
            print("A. infili una sarpa negli ingranaggi")
            print("B. salti sull'ascensore e cerchi di entrarci tramite una grata")
            risposta25 = input().upper()
			
            if risposta25 == "A":
              print("la scarpa vine frantumata in un secondo")
              print("l'ascensore e' ormai a pochi metri da te")
              print("A. ne infili un altra")
              print("B. infili il fucile")
              print("c. entri nell'ascensore")
              risposta26 = input().upper()
			  
              if risposta26 == "A":
                print("muori schiacciato")
				
              if risposta26 == "B":
                print("l'ascnesore si e' bloccato")
                print("ora pero' l'uomo all'interno sta' cercando di capire perche'")
                print("A. apri le porte ed esci dalla tromba dell'ascensore")
                print("B. entri dentro la cabina dalla grata")
                risposta27 = input().upper()
				
                if risposta27 == "A":
                  print("sie uscito, ti trovi un piano sopra la sala comando")
                  print("ma ormai molti uomini sono in allerta e ti stanno cercando")
                  print("A. abbandoni la missione")
                  print("B. ti dirigi velocemente all'areria per fare scorte di proiettili")
                  risposta28 = input().upper()
				  
                  if risposta28 == "B":
                    print("ora armato vai verso il centro di comando")
                    input()
                    print("davanti alla porta c'e' un soldato")
                    input()
                    print("corri verso di lui")
                    input()
                    print("estrai i coltello")
                    input()
                    print("lo sollevi per e gambe")
                    input()
                    print("lo minacci col coltello alla gola")
                    input()
                    print("ti fai rivelare dove si trova il capitano")
                    input()
                    print("sai che si trova in mensa")
                    print("vai da lui lo addormenti con un sonnfero")
                    print("gli rubi la combinazione e recuperi piani")
				
              if risposta25 == "B" or risposta26 == "C" or risposta27 == "B":
                print("aggredisci la guardia, sisemi l'ascensore e rubi al soldati l'uniforme")
                print("entri nella sala comando, acherando le telecamere scopri che il capitano si trova in mensa")
                print("vai subito da lui lo addormenti con un sonnfero")
                print("gli rubi la combinazione e recuperi piani")
				
        if risposta5 == "B":
          print("tutte le porte delle caine son sigillate")
          print("percio' devi.....")
          print("A. correre imbracciando il fucile")
          risposta29 = input().upper()
				
        if risposta5 == "C" or risposta29 == "A":
          print("stai correndo tra i corridoi facendoti largo tra le squadre che arrivano")
          print("raggiungi la sala comando e ti sigilli dentro")
          print("prendi come ostaggio il capitano")
          print("riesci a farti comunicare la posizione e la combinazione della cassaforte")
          input()
          print("riuscendo cosi' a recuperare i piani")

  if risposta2 == "B" or risposta2 == "C":
    print("ti trovi davanti al centro di comando")
    print("A. entrarci")
    risposta30 = input().upper()
	
    if risposta30 == "A":
      print("fortunatamente vedi che non ci sono soldati ma solo addetti informatici")
      print("pero' in quel momento entra una squadra di 4 uomini con davanti il capitano del sommergibile")
      print("A. ti butti dietro a una scrivania inpugnando il fucile")
      print("B. fai direttamente fuoco sui soldati")
      risposta31= input().upper()
	  
      if risposta31 == "A":
        print("i soldati entrano e non si accorgono d te percio' hai ancra l'occasione di sparare")
        print("A. spari")
        print("B. rimani ancora nascosto")
        risposta32 = input().upper()
		
        if risposta32 == "A" or risposta31 == "B":
          print("riesci a uccidere i quattro uomini ma il capitano e ancora vivo")
          print("ti colpisce su una spalla e corre verso di te")
          print("cadendo hai perso il fucile")
          print("estrai il coltello")
          print()
          input()
          print("il capitano ti salta addosso")
          print()
          input()
          print("col ginocchi di blocca la mano")
          print()
          input()
          print("ti punta la pistola alla testa e......")
          print("premi A per afferrargli il braccio")
          input()
          print("premi ripetutament X per rubargli la pistola")
          input()
          input()
          input()
          input()
          print("hai la pistola....cosa fai.....")
          print("A. lo minacci per farti dare i codici della cassaforte dove sono contenuti i file")
          print("B. lo uccidi e rubi la cassaforte")
          risposta33 = input().upper()
		  
          if risposta33 == "A":
            print("ti dice i codici e riesci ad ottenere i file")
			
          if risposta33 == "B":
            print(" dopo averlo ucciso la ciurma ti assale e ti arrestano")

        if risposta32 == "B":
          print("dopo appena qualche secondo gli uomini ti trovano e ti fanno loro prigioniero per interrogarti")

    if risposta4 == "B":
      print("stai strisciando nel condotto quando senti un uomo che parla dei codici della cassa forte")
      print("ne riesci asentire sulo una parte te ne manca uno")
      print("arrivi al pannello di controllo e sblocchi le porte....")
      print(".....TO BE CONTINUE.......")
	  
if risposta1 == "B":
  print("Hai deciso di entrare dal vano dei missili, posto sulla prua del sottomarino")
  print("ed hai a disposizione delle mine subacquee o una fiamma ossidrica \n Cosa vuoi usare?")
  print("A. fiamma ossidrica")
  print("B. mina subacquea")
  risposta40 = input().upper()
	
  if risposta40 == "A":
    print("Sei riuscito ad entare nel sottomarino senza attirare l'attenzione")
    print("e, armato di una pistola silenziata calibro 9, riesci ad arrivare a una scala senza farti scoprire")
    print()
    print("Secondo le tue informazioni i piani militari si trovano in una cassaforte nella \n cabina del capitano del sommergibile, che potrebbe trovarsi al piano inferiore o superiore")
    print("Dove decidi di andare?")
    print("A. Al piano superiore con le scale")
    print("B. Al piano inferiore cone le scale")
    print("C. Al piano superiore con l'ascensore perchè sei pigro")
    print("D. Al piano inferiore con l'ascensore, sempre perchè sei pigro")
    risposta41 = input().upper()

    if risposta41 == "A" or risposta41 == "C":
      print("Arrivato al piano superiore, ti accorgi di esserti sbagliato e di essere arrivato nei pressi dell'armeria")
      print("Non sapendo cosa aspettarti una volta arrivato nella cabina del capitano, decidi di \n dirigerti all'armeria per armarti")
      print()
      print("A guardia dell'ingresso si trova un soldato della Guardia Rossa Sovietica armato di Kalashnikov")
      print()
      print("Come vuoi eliminarlo?")
      print()
      print("A. Sparandogli")
      print("B. Avvicinandoti di soppiatto e accoltellandolo")
      risposta42 = input().upper()

      if risposta42 == "A":
        print("Il soldato, meglio addestrato di te nell'arte delle armi, \n riesce a colpirti ancor prima che tu riesca a togliere la sicura alla pistola ")
        print()
        print("L'agente " + nome + " è deceduto in azione mentre serviva la patria con coraggio")
	    	
        if risposta42 == "B":
          print("Riesci a sorprendere il soldato nemico e, una volta nascosto il cadavere, accedi all'armeria")
          print()
          print("Alla vista di tutte quelle armi ti brillano gli occhi e, preso da un'euforia incontrollabile,")
          print("ti carichi addosso tutte le armi che il tuo corpo riesce a trasportare")
          print()
          input()
          print("poi cadi")
          input()
          print("poi di rialzi")
          print("Dopo diverse cadute, capisci che forse tutte quelle armi sono un po' pesanti")
          print("così, a malincuore, decidi di lasciarne giù la metà")
          print("A. Vai al centro di comando ")    		
          risposta43 = input().upper()

          if risposta41 == "B" or risposta41 == "D" or risposta43 == "A":
            print("Arrivi al centro di comando, entri e ti trovi davanti gli ufficiali col capitano")
            print()
            print("A. Prendi in ostaggio un ufficiale e ti fai dire dal capitano dove si trova la cassaforte")
            print("B. Comici a sparare in aria per spaventare il capitano e farti rivelare dov'è la cassaforte")
            print("C. Tenendo tutti sotto tiro, metti a soqquadro la stanza in cerca della cassaforte")
            risposta43 = input().upper()

            if risposta43 == "A" or risposta43 == "B" or risposta43 == "C" and risposta42 == "B":	    		
              print("Finalmente trovi la cassaforte, che però è protetta da una combinazione a 6 numeri")
              print("Fiducioso delle tue abilità oratorie, convinci 'gentilmente' il capitano a darti il codice e,")
              print("dopo un piccolo litigio con gli ufficiali, risolto a colpi di mitragliatrice, trovi i piani!!! ")
	    	
            if risposta43 == "A" or risposta43 == "B" or risposta43 == "C":
              print("Finalmente trovi la cassaforte, che però è protetta da una combinazione a 6 numeri")
              print("Fiducioso delle tue abilità oratorie, coninci 'gentilmente' il capitano a darti il codice e,")
              print("dopo un piccolo litigio con gli ufficiali, risolto a sbrangate in testa, trovi i piani!!! ")               

  if risposta40 == "B":
    print("muori")  
					  
print()
print()
print()
print()
print("agente" + nome + ", la missione e' terminata")
input()					