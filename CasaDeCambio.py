print("Casa de Cambio")
usr = input("Ingrese Nombre de Usuario : ")
pwd = input("Ingrese su Contraseña     : ")

if ( usr!='admin' or pwd!='admin' ) :
    print("usuario/contraseña inválidos")
else :
    try:
        vendedor  = int(input("Ingrese Dolar Vendedor  : "))
    except :
        vendedor = 0
        
    try :    
        comprador = int(input("Ingrese Dolar Comprador : "))
    except :
        comprador = 0
    
    if ( comprador == 0 or vendedor == 0 ) :
        print("Los valores ingresados no son validos")
    elif ( comprador >= vendedor ) :
        print("Los valores fueron mal definidos ")
    else :
        
        cant_ventas = 0   # contador : 1, 2, 3...
        total_ventas = 0  # sumador : suma_dolares_vendidos
        
        cant_compras = 0   # contador : 1, 2, 3...
        total_compras = 0  # sumador : suma_dolares_vendidos

        while True :
            # opciones de menu
            print(f"1. COMPRAR DOLAR ({comprador})")
            print(f"2. VENDER  DOLAR ({vendedor})")
            print("3. SALIR ")
            # leo la opcion ingresada
            try :
                op = int(input("ingrese opcion : "))
            except :
                op = 0
            # evaluo la opcion ingresada
            if op == 1 :
                print("compra_dolares")
                # el cliente trae los dolares y se quiere llevar pesos
                try :
                    dolares = int(input("ingrese dolares : "))
                except :
                    dolares = 0
                
                if dolares > 0 :
                    cambio = dolares * comprador
                    print(f"resultado :{cambio} pesos")
                    cant_compras = cant_compras + 1 
                    total_compras = total_compras + dolares
                else :
                    print("error en la cantidad de dolares ingresada")

            elif op==2 :
                print("vender_dolares")
                # el cliente trae pesos y se quiere llevar dolares
                try :
                    dolares = int(input("ingrese dolares : "))
                except :
                    dolares = 0
                
                if dolares > 0 :
                    cambio = dolares * vendedor
                    print(f"debe pagar :{cambio} pesos")
                    cant_ventas = cant_ventas + 1 
                    total_ventas = total_ventas + dolares
                else :
                    print("error en la cantidad de dolares ingresada")
                    
            elif op==3:
                print("salir")
                break
    
            else :
                print("opcion no valida")
            #fin del if
        #fin del while
        
        print("cantidads de compras realizadas :", cant_compras)
        print("dolares comprados", total_compras, "=",total_compras*comprador,"pesos")
        print("cantidads de ventas realizadas :", cant_ventas)
        print("dolares vendidos", total_ventas,"=", total_ventas * vendedor, "pesos")
            
        
        