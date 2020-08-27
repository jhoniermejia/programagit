def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False

def test(): 
    num = int(input("introduzca un numero:"))
    resultado = NumeroPerfecto(num)
 
    if resultado is True:
         print(" Es un numero perfecto" )
    else:
         print( "NO es un numero perfecto")

         return 

if __name__ == '__main__':
     test()  