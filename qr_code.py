import qrcode as qr
img = qr.make(input("Give link to make in qr form:"))
img.save(input("Enter file name(with .png:)"))