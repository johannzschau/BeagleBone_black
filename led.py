#! / Usr / bin / python
# encoding: utf-8
import os, sys
import time
import os.path


class Port_I_O:
    
    CHEMIN_GPIO = '/sys/class/gpio'
 
    def __init__(self, gpio_id):    #Constructeur de la classe Port_I_O 
        self.gpio_id = gpio_id
        self.gpio_path = '/'.join([self.CHEMIN_GPIO, 'gpio' + str(self.gpio_id)])
        
        if not os.path.exists(self.gpio_path):
         F_tem = open('/'.join([self.CHEMIN_GPIO, 'export']),"w")
         F_tem.write(str(gpio_id))   
#   méthode pour déclarer la pin en sortie et lui donner une valeur
    def Output(self,_id,value): 
        F_tem = open('/'.join([self.CHEMIN_GPIO, 'gpio' + str(self.gpio_id), 'direction']),"w")
        F_tem.write("out")
        self.value=value
        self._id = _id
        F_tem = open('/'.join([self.CHEMIN_GPIO, 'gpio' + str(self._id), 'value']),"w")
        F_tem.write(str(value))
#   méthode pour déclarer la pin en entrée et lire sa valeur"""   
    def Intput(self,_id): 
        F_tem = open('/'.join([self.CHEMIN_GPIO, 'gpio' + str(self.gpio_id), 'direction']),"w")
        F_tem.write("in")
        self._id = _id
        F_tem = open('/'.join([self.CHEMIN_GPIO, 'gpio' + str(self._id), 'value']),"r")
        value = F_tem.read()
        return value.rstrip()
      
#   MAIN      
if __name__ == "__main__":
    chiffre = 0
    print('!!!!!!!!!!!!!!!!!\n programme V 1.4.5\n!!!!!!!!!!!!!!!!!')
    print('Numéro de la pin exemple 7')
    pin = input()
    gpio = Port_I_O(pin)
    print('Menu : 1)faire clignoter une GPIO , 2) lire une GPIO')
chiffre = input()
if chiffre == 1:
    while True:
     gpio.Output(pin,0)
     time.sleep(1)
     gpio.Output(pin,1)
     time.sleep(1)
elif chiffre == 2:
	 print('la valeur est :'+ gpio.Intput(pin))

	
	