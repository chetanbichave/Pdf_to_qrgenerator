import qrcode
from PIL import Image

resumelnk = input("Enter Your Resume Link : ")
linkedinlnk = input("Enter Your Linkedin URL : ")
githublnk = input("Enter Your Github URL : ")

Logo1 = "logo.png"
linkedin = "Linkedin.png"
github = "github.png"



logolist = [Logo1,linkedin,github]
linksList = [resumelnk,linkedinlnk,githublnk]

for logo in logolist:

    logosindex = logolist.index(logo)
    print(logosindex)
    logos = Image.open(logo)
    basewidth = 20
    #logo = Image.open(Logo_link)

    wpercent = (basewidth / float(logos.size[0]))
    hsize = int((float(logos.size[1]) * float(wpercent)))
    logos = logos.resize((basewidth, hsize))

    QRcode = qrcode.QRCode(
        version=1,
        box_size=2,
        border=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    #for links in linksList:
    linksName = linksList[logosindex]
    print("Link is : ",linksName)
    QRcode.add_data(linksName)
    #print(QRcode.add_data(linksName))
    QRcode.make(fit=True)
    img = QRcode.make_image(
    fill_color="Grey", back_color="white").convert('RGB')

    # set size of QR code
    pos = ((img.size[0] - logos.size[0]) // 2,
            (img.size[1] - logos.size[1]) // 2)
    img.paste(logos, pos)

    print("Logo Name : = " ,logo)
    # save the QR code generated
    if logo == "logo.png":
        img.save("Resume.png")
    elif logo == "Linkedin.png":
        img.save("LinkedinQR.png")
    elif logo == "github.png":
        img.save("GithubQR.png")
    else :
        print("error")

    print('QR code generated!')

