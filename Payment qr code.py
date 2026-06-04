import qrcode
Upi_id= (input('Please enter your UPI ID ->>'))
Phonee_URL= f'upi://pay?pa={Upi_id}&pn=Recipient%20name&mc=1234'
Paytm_URL= f'upi://pay?pa={Upi_id}&pn=Recipient%20name&mc=1234'
Google_pay_URL= f'upi://pay?pa={Upi_id}&pn=Recipient%20name&mc=1234'
Phonee_qr= qrcode.make(Phonee_URL)
Paytm_qr= qrcode.make(Paytm_URL)
Google_pay_qr= qrcode.make(Google_pay_URL)
Phonee_qr.save('Phone_pay_qr.png')
Google_pay_qr.save('Google_pay.png')
Paytm_qr.save('Paytm_pay.png')
Phonee_qr.show()
Google_pay_qr.show()
Paytm_qr.show()

