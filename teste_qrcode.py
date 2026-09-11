import qrcode

img = qrcode.make("NF 000001 - Cliente Maria Dias - Total R$ 7000,00")

img.save("qrcode_nf.png")

print("QR Code criado com sucesso!")
