
players = {
  'name':["Pat","Lowri","Carys","Phil"],
  'Birth Year': [1932,1969,1971,1974],
  'Location': ["MGN","Salop Street", "Harthill", "Coach House"]
}
Cluedo_attributes= { 
  'Characters':["Marvellous Mazel","Lovely Loz","Capable Carys","Professor Phil", "DCS Tim", "Jean Benson","Jolly June","Mysterious Michael", "Gwynne the Grope", "Tottering Ted","Ben Rees","Doctor John"],

  'Modus Operandi':["Copy of the Mabinogi","Harp String","Biting Wit","Carving Knife","Truncheon","Christmas Twig","Sand Wedge","Baseball Bat","Poisoned Shiraz","Death by Dangerous Driving","Dog Collar","iPad"],
  
  'Venue':["MGN","Salop Street","Harthill","The Coach House","Calderstones Park","The Golf Club","Philharmonic Hall","Capel","Court","Allerton Road Tescos","Deli Fonsecca","The Gardens"]
}

#print(Cluedo_attributes.items())

for i in Cluedo_attributes.keys():
  print(i,":")
  print("-----")
  for k,v in enumerate(Cluedo_attributes[i]):
    print (k,v)
#    for j in Cluedo_attributes.values():
 #     print(j)
    
  #print (i)    
  #print(i)
  #Cluedo_attributes.keys(), ": ", 