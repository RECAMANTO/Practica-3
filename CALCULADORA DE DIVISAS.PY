print("----- CONVERSOR DE DIVISAS -----")


while(True):

    eleccion = input("DOP A DOLAR(USD) [1] -- YEN A EURO [2] -- DOP A MXN [3]: \n" )   


    if(eleccion == "1"):
        print("----- DOP A DOLAR -----")
        #DOP A DOLAR
        def exchange_money(budget,exchange_rate):

            return budget * exchange_rate
    
        print(exchange_money(float(input("INGRESE CANTIDAD A CONVERTIR: ")),0.017))
                
        salir =input("DESEA SALIR?")
        if salir == "NO" or "no":
            continue
        else:
            break
        
    if(eleccion == "2"):
        #YEN A EURO
        def exchange_money(budget,exchange_rate):

            return budget * exchange_rate
            
            
    
        print(exchange_money(float(input("INGRESE CANTIDAD A CONVERTIR: ")),0.0062))

        salir =input("DESEA SALIR? ")
        if salir == "NO" or "no":
            continue
        else:
            break


    
        

    


