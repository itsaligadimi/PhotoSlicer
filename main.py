from PIL import Image
import glob

input_files_dir = '../images/test/*.jpg'
output_files_dir = '../dataset/test/'
kernel_w = 450
kernel_h = 200
stride_h = 100
stride_v = 50

files = glob.glob(input_files_dir)


for i in range(len(files)):
    img = Image.open(files[i])
    width = img.width
    height = img.height
    
    kernel_count_h = int((width - kernel_w) / stride_h) + 1
    kernel_count_v = int((height - kernel_h) / stride_v) + 1

    for j in range(kernel_count_v):
        top = j * stride_v
        bottom = top + kernel_h

        for k in range(kernel_count_h):
            left = k * stride_v
            right = left + kernel_w

            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save('{}{:03d}_{:03d}_{:03d}_{}'.format(output_files_dir, i, j, k, '.jpg'))
    print('{:03d} -> {} images'.format(i, kernel_count_h * kernel_count_v))


