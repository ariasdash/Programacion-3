def interfaz ( ):
    print( "Este programa utiliza la base de datos abierta sobre casos de COVID-19 en Colombia, permitiendo\n"
           "consultar hasta 1000 casos en un departamento específico. Los datos mostrados incluyen\n" 
           "el departamento, municipio, edad, tipo de contagio, estado del caso y país.\n" )
    departamento = input( "Ingrese el nombre del departamento que desea buscar: " ).upper()
    while True:
        try:
            num_casos = int( input( "Ingrese el número de casos que desea consultar (Máximo 1000): " ) )
            if num_casos > 1000:
                print( "El mayor número de casos permitidos es 1000, intentelo de nuevo\n" )
            else:
                break
        except ValueError:
            print( "Ingrese un número válido\n" )
    return departamento, num_casos
