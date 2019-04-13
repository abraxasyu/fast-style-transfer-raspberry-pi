import evaluate
import os
import pygame
import time

os.system('sudo service motion stop')

pygame.init()

screen = pygame.display.set_mode((1040, 780))

styles = [r'./style/'+i+r'.ckpt' for i in ['la_muse','rain_princess','scream','udnie','wave','wreck']]

inpath=r'./in/'
outpath=r'./out/'

count=0

while(True):
    realinpath = inpath+str(count)+'.jpg'
    realoutpath = outpath+str(count)+'.jpg'
    curtime = time.time()
    os.system('fswebcam -r 640x480 -S 20  --no-banner --save '+realinpath)    
    evaluate.ffwd([realinpath],
     [realoutpath],
     styles[count%len(styles)], device_t='/gpu:0', batch_size=4)
    print('PROCESSING TOOK {:.1f} SECONDS'.format(time.time()-curtime))
    image = pygame.image.load(realoutpath)
    image = pygame.transform.scale(image, (1040, 780))
    retarea = screen.blit(image, (0, 0))
    pygame.display.update(retarea)
    count+=1



