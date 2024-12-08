'''import secrets 
import string 
def create_password(p_length=12):
    letters=string.ascii_letters 
    digits=string.digits 
    spc_chars=string.punctuation
    alphabet=letters+digits+spc_chars 
    password=""
    p_strong=False 
    while not p_strong:
        password=''
        for i in range(p_length):
            password+=''.join(secrets.choice(alphabet))
        if (any(char in spc_chars for char in password) and sum(char in digits for char in password)>=2):
            p_strong=True 
    return password 

if __name__ == '__main()__':
    print(create_password())'''


import qrcode 
source="https://www.google.com/"
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=10,
                 border=4,
                 )
qr.add_data(source)
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("qrcode.png")
print("QR Code generated and saved as 'qrcode.png'")







