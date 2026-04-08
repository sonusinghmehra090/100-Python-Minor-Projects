import qrcode
def qr_generate():
    link = input("enter your link to generate qr code : ")
    
    user = input("Do you want to customize your qr code [y/n] :").lower()
    if user =="n":
        img = qrcode.make(link)
        if img is not None:
            print("generating your qr code...")
            img.save("generated_qrcode_bysonumehra.png")
            print("Qr code generated successfully")

        else :
            print("Failed to generate Qr code")
        
    if user=="y":
        box_size = int(input("enter QR size eg.6,7,8.. :"))
        color = input("enter color of qr code : ")
        background_color = input("enter background color : ")

        qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=box_size,border=5)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color = color , back_color =background_color)
        print("Generating your QR code ...")
        img.save("generated_qrcode_bysonumehra.png")
        print("QR code generated successfully")
        
    
if __name__=="__main__":
    qr_generate()