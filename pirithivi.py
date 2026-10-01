import qrcode
pr = "https://www.instagram.com"
qr = qrcode.make(pr)
qr.save("website_qr.png")
print("qrcode generated")
qrcode generated
