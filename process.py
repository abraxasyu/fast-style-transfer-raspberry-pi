#import py_compile
#py_compile.compile('evaluate.py')


import evaluate

evaluate.ffwd([r'C:\Users\Sean Yu\Box\Sync\Projects\Style Transfer\testset\in\gala3_512.jpg'],
     [r'C:\Users\Sean Yu\Box\Sync\Projects\Style Transfer\testset\out\test.jpg'],
     r'C:\Users\Sean Yu\Box\Sync\Projects\Style Transfer\fast-style-transfer\style\la_muse.ckpt', device_t='/gpu:0', batch_size=4)

















