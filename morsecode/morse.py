from machine import Pin
import time
led = Pi(25, Pin.OUT)

def dot()
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
def dash()
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(0.5)
    
def morse(txt):
    '''Morse code encryption and decryption'''
    
    d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}
    translation = ''
    
    # Encrypt Morsecode
    if txt.startswith('.') or txt.startswith('−'):
        # Swap key/values in d:
        d_encrypt = dict([(v, k) for k, v in d.items()])
        # Morse code is separated by empty space chars
        txt = txt.split(' ')
        for x in txt:
            translation += d_encrypt.get(x)
        
    # Decrypt to Morsecode:
    else:
        txt = txt.upper()
        for x in txt:
            translation += d.get(x) + ' '
    return translation.strip()
#print(morse('python')) #encode a phrase
# .--. -.-- - .... --- -.
#print(morse('.--. -.-- - .... --- -.')) #decode a morse message
# PYTHON
#print(morse(morse('HEY'))) #decrypt a morse code
# HEY
text = input("Enter text to translate to morse code: ")


