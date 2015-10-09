from PIL import Image, ImageDraw, ImageFont
__author__ = 'DanielSong'

def add_num(img,number):



    #生成pad和数字
    if number >= 10000:
       strNumber = '...'  
    else:
       strNumber = '%d' %(number)
    
    draw = ImageDraw.Draw(img)
    #myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=50)
    myfont = ImageFont.truetype('C:/windows/fonts/framdit.ttf', size=40)
   
    width, height = img.size
    txtWidth,txtHeight = myfont.getsize(strNumber)
    #print ("txtHeight %d" %txtHeight)

    if len(strNumber) > 1:
       NumImageWidth = txtWidth + 20
    else:
       NumImageWidth = 40;
    p = Image.new('RGBA', (NumImageWidth,40),(255,255,255,0)) 
    NumberDraw = ImageDraw.Draw(p)
    fillcolor = "#ff0000"
    NumberDraw.ellipse((0,0,40,40),fill=fillcolor)
    NumberDraw.ellipse((NumImageWidth-40,0,NumImageWidth,40),fill=fillcolor)
    NumberDraw.rectangle((20,0,NumImageWidth-20,40),fill=fillcolor)
    txtPosX = (NumImageWidth-txtWidth)/2
    if len(strNumber) > 1:
       NumberDraw.text((txtPosX, -3), strNumber, font=myfont, fill="#FFFFFF")
    else:
       NumberDraw.text((8, -3), strNumber, font=myfont, fill="#FFFFFF")


    #生成pad和数字 完成

       
    #p.show()
    img.show()

    resultP = Image.new('RGBA', (width+20, height+20),(255,255,255,0))
    resultP.paste(img,(0,20,width,height+20));
    R,G,B,A = p.split()
    resultP.paste(p,(width+20-NumImageWidth,0,width+20,40),mask = A);
    
    resultP.show()
    resultP.save('result.jpg','jpeg')
    return 0

    #if txtWidth>40:
    #    DrawMode = 1
    #else :
    #    DrawMode = 0;
    #fillcolor = "#ff0000"

    #if DrawMode == 0:
    #   draw.ellipse((width-50/2,0,width+50/2,50),fill=255)
    #else :
    #   if DrawMode ==1:
    #      draw.ellipse((width-50/2,0,width+50/2,50),fill=255)
    
    
    #draw.arc((width-50,0,width,50),0,360,fill=255)
    

    #textdraw = ImageDraw.Draw(img)
    
    #print("txtWidth,txtHeight = %d"%(txtWidth),",%d"%(txtHeight))
    #draw.rectangle((width-txtWidth,0,width,50),fill=255)

    #fillcolor = "#FFFFFF"
    #draw.text((width-42, 7), '1011', font=myfont, fill="#FFFFFF")
    #draw.text((0,60),unicode('你好','utf-8'),(0,0,0),font=font) 
    #draw.text((width-txtWidth, 7), strNumber, font=myfont, fill="#FFFFFF")
    #img.save('result.jpg','jpeg')

    
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image,6)
    #image.show()
