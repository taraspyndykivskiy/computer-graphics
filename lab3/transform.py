from PIL import Image
import math

def rot_x(angle,ptx,pty):
    return math.cos(angle)*ptx + math.sin(angle)*pty

def rot_y(angle,ptx,pty):
    return -math.sin(angle)*ptx + math.cos(angle)*pty

angle = math.radians(50)

im = Image.open('image.png')

(x,y) = im.size

xextremes = [rot_x(angle,0,0),rot_x(angle,0,y-1),rot_x(angle,x-1,0),rot_x(angle,x-1,y-1)]
yextremes = [rot_y(angle,0,0),rot_y(angle,0,y-1),rot_y(angle,x-1,0),rot_y(angle,x-1,y-1)]
mnx = min(xextremes)
mxx = max(xextremes)
mny = min(yextremes)
mxy = max(yextremes)

blue = RGBTransform().mix_with((0, 0, 255),factor=.30).applied_to(lena)

im = im.transform((int(round(mxx-mnx)),int(round((mxy-mny)))),Image.AFFINE,(math.cos(angle),math.sin(angle),-mnx,-math.sin(angle),math.cos(angle),-mny),resample=Image.BILINEAR)
im.save('transformation.png')