import qrcode
i=4
print (len(str(i)))


for i in range (38):
    #usando pillow para generar la imagen
    if len(str(i))==1:
        j=f"0{str(i+1)}"
    else:
        j=i+1
    img = qrcode.make(f"22200{j}")
    f = open(f"22200{j}.png", "wb")
    img.save(f)
    f.close()
    pass