
email = str(input("Digite seu E-mail: "))

count = email.find("@")
maxLength = len(email)

print("http://" + email[count+1:maxLength])