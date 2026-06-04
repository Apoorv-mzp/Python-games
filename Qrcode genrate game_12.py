import qrcode

url = input("PLease enter your URL:").strip()
file_keeper= "/Users/apoorvpandey/Desktop/Parctise of js and projects of js// qrcode.png"
qr= qrcode.QRCode()
qr.add_data(url)
img= qr.make_image()
img.save(file_keeper)
print('Qrcode is saved in',file_keeper)
