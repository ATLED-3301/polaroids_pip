import cv2 
import time
import numpy as np

def crop_image(filename, pixel_value=255):
    gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    crop_rows = gray[~np.all(gray == pixel_value, axis=1), :]
    cropped_image = crop_rows[:, ~np.all(crop_rows == pixel_value, axis=0)]
    return cropped_image

def insert_center(bg,img):
    bg_shape = bg.shape
    img_shape = img.shape
    ww = bg_shape[0]
    w = img_shape[0]
    hh = bg_shape[1]
    h = img_shape[1]
    center_x_bg = np.floor_divide( ww , 2 )
    center_y_bg =  np.floor_divide( hh , 2 )
    center_x_img =  np.floor_divide( w , 2 )
    center_y_img =  np.floor_divide( h , 2 )
    delta_x_minus = center_x_bg - center_x_img
    delta_x_plus= center_x_bg + center_x_img
    delta_y_minus = center_y_bg - center_y_img
    delta_y_plus= center_y_bg + center_y_img
    bg[delta_x_minus : delta_x_plus , delta_y_minus : delta_y_plus , :] = img[0:w,0:h,:]
    

def crop_border(img,border_x,border_y):
    img_shape = img.shape
    w = img_shape[0]
    h = img_shape[1]
    center_x_img =  np.floor_divide( w , 2 )
    center_y_img =  np.floor_divide( h , 2 )
    img = img[ border_x : w + border_x  , border_y : w - border_y , :]
    return img

if __name__ == "__main__" :
    path = input("insert full polaroid scan path :\n>>> ")
    imgor = cv2.imread(path)
    img_shape = imgor.shape
    h = img_shape[0]
    w = imgor.shape[1]
    img = crop_border(imgor,5,5)
    img_res = cv2.resize(img, (1054 ,1280) , interpolation= cv2.INTER_LINEAR)
    img_shape = img_res.shape
    hr = img_shape[0]
    wr = img_shape[1]


    cv2.waitKey(0)

    y = 120
    h = 870
    x = 120
    w = 870
    croppedwhite = img_res[y+10:y+h-10, x+10:x+w-10]


    cv2.imshow('graycsale imagde',croppedwhite)
    cv2.waitKey(0)

    blur_image = cv2.GaussianBlur(croppedwhite, (3,3), 0)
    blur_resized_up = cv2.resize(blur_image, (1600, 1600) , interpolation= cv2.INTER_LINEAR)
    bg_shape = blur_resized_up.shape
    hh = bg_shape[0]
    ww = bg_shape[1] 
    center_x = ww/2
    center_y = hh/2
    blur_resized_up = np.asarray(blur_resized_up)
    img_shape = np.asarray(img_shape)
    hr_m = np.floor(hr/2)
    wr_m = np.floor(wr/2)
    final = insert_center(blur_resized_up,img_res)
    final = blur_resized_up
    name = input("insert image name :\n>>> ")
    cv2.imwrite(name+".jpg", final)
    exit(0)






