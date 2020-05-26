from PIL import Image
from pylab import *

im = array(Image.open('images/bird.jpg').convert('L'))

gray()

negative_im = 255 - im
contrast_im = 255.0 * (im / 255.0)**2

subplot(1, 3, 1)
imshow(im)
title('Original')

subplot(1, 3, 2)
imshow(negative_im)
title('Negative')

subplot(1, 3, 3)
imshow(contrast_im)
title('High contrast')

show()
