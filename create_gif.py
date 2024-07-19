import imageio.v3 as iio

filenames = ['X-wing1.jpg', 'X-wing2.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('I_love_X-wings.gif', images, duration = 500, loop = 0)