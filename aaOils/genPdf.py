from reportlab.lib.pagesizes import A4, cm
from reportlab.platypus import SimpleDocTemplate,Image,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json
import urllib

with open("finalest.json","rb") as file:
    datas = json.load(file)

downloadNum = 0
for data in datas:
    if 'imgSrc' in data:
        print('Retrieving the {0}th image------{1}'.format(downloadNum,data['imgSrc'].split('/')[-1]))
        if downloadNum > -1:
            urllib.urlretrieve(data['imgSrc'],data['imgSrc'].split('/')[-1])
        downloadNum += 1
    else:
        print('%s doesn\'t have a image' % data['oilName'])
        data['imgSrc'] = ''
print("-------------------------------------------------------------All images are already downloaded!---------------------------------------")

doc = SimpleDocTemplate("test.pdf",pagesizes=A4)
width,height = A4
styles = getSampleStyleSheet()

elements = []

for data in datas:
    imgSrc = data['imgSrc']

    if imgSrc.split('/')[-1] != 'organic_lemon_raw_300x300.jpg':
        img = Image(imgSrc.split('/')[-1],4*cm,4*cm)
        elements.append(img)
    else:
        elements.append(Paragraph('<font color=red size=15>{0} is a invalid image!</font>'.format(imgSrc.split('/')[-1]),styles['BodyText']))

    for key,value in data.iteritems():
        if key == 'description':
            elements.append(Paragraph('<font color=blue size=15>%s:</font>'% key,styles['BodyText']))
            for info in value:
                elements.append(Paragraph("<font size=14>----- %s</font>" % info,styles['BodyText']))
        elif key == 'prices':
            priceStr = '<font color=blue size=15>%s:</font>'% key
            for volume,price in value.iteritems():
                priceStr += u'<font size=14>{0}---{1}</font>    '.format(volume,price)
            elements.append(Paragraph(priceStr,styles['BodyText']))
        else:
            elements.append(Paragraph(u"<font color=blue size=15>{0}:</font><font size=14> {1}</font>".format(key,value),styles['BodyText']))
    elements.append(Spacer(1,15))
    elements.append(Paragraph('------------------------------I am a little line--------------------------------',styles['BodyText']))
    elements.append(Spacer(1,15))
    print('%s has been push into list.'% data['oilName'])

doc.build(elements)

