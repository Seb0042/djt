
import owncloud


oc = owncloud.Client('https://www.djtabasco.dance/nextcloud')
oc.login('djt', 'JQ2Do-fBf27-ejS7b-BZ2C9-iryTN')

#oc.get_file('Salsa/radio.txt', 'Salsa_radio.txt')
oc.get_file('Salsa/Mas Bajo/01-01- Emmenez-moi.mp3','test.mp3')
