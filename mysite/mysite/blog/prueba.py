def validarUuario(username,password):
  y=raw_input("Ingrese un usuario")
  if y.isalnum() == True:
    if len(y)< 6:
      print "El nombre de usuario debe contener al menos 6 carácteres"
    elif len(y)> 12:
      print "El nombre de usuario no puede contener más de 12 carácteres"
    else:
      print "TRUE"
      
else:
  print ("El nombre de usuario puede contener solo letras y números)
  
#usuario()



def password():
  password=raw_input("Ingrese su password")
  espacio=False;
  mayuscula=False
  minuscula=False
  numero=False
  longitud=len(password)
  for ver in password:
    if ver.isspace() == True:
      espacio=True
    if ver.isupper() == True:
      mayuscula=True
    if ver.islower() == True:
      minuscula=True
    if ver.isdigit() == True:
      numero=True
    
if espacio == Flase and mayuscula == True and minuscula == True and numero == True and longitud >=8:
  print "Perfecto"

else:
  print "Password demasiado débil"
  
  #password()
