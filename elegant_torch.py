from torch.utils.data import Dataset
import glob
import os
import torch
from skimage.io import imread
import torchvision.transforms as tf
from PIL import Image
import matplotlib.pyplot as plt


class CustomDataLoader(Dataset):
    def __init__(self, train_images, train_labels, image_suffix="jpg", target_size=(30, 30)):
        """

        :param train_images: Directory containing train_images
        :param train_labels: Directory containing train_labels
        :param image_suffix: Image suffix, for convenience
        :param target_size

        """

        self.train_images = train_images
        self.train_labels = train_labels
        self.image_suffix = image_suffix
        self.target_size = target_size

        # Include sanity checks

        # In this case, we only check that both train_images and train_labels directories exist
        # We also ensure that we get the correct image suffix, jpg and png here

        if not (all(os.path.isdir(directory) for directory in [train_images, train_labels])):
            raise NotADirectoryError("Please ensure that both train_images and train_labels are valid directories.")

        if not self.image_suffix in ["png", "jpg","jpeg"]:
            raise ValueError("Only supporting PNG and JPG files for now.")

        # glob for our file names
        # sorted because I prefer 1, 10, 11, ...
        # ideally should be able to glob both png and jpg, for simplicity glob only one type
        self.image_list = sorted(glob.glob(self.train_images + "/*" + self.image_suffix))
        self.labels_list = sorted(glob.glob(self.train_labels + "/*" + self.image_suffix))


        if len(self.image_list) != len(self.labels_list):
            raise ValueError("Images list and labels list should be the same length.")

    def __len__(self):
        """

        :return: length of the dataset

        """
        return len(self.image_list)

    def transform(self, image):
        # Basic, convert to PIL since torch tensors only work with PIL
        # Basic resizing
        to_pil = Image.fromarray(image)
        # resize_image
        resizer = tf.Resize(self.target_size)
        image = resizer(to_pil)
        return image

    def __getitem__(self, img_index):
        if torch.is_tensor(img_index):
            img_index = img_index.tolist()

        train_image = imread(self.image_list[img_index])
        train_label = imread(self.labels_list[img_index])

        return {"image":self.transform(train_image), "mask":self.transform(train_label)}


images_loader = CustomDataLoader("image_path",""
                                "image_path",
                                 target_size= (512, 512), image_suffix="png")
# Get one index of images
next(iter(images_loader))

# Manually
plt.imshow(images_loader[0]["image"])

import cv2
from skimage.filters import threshold_li
import numpy as np
img = imread("https://github.com/Nelson-Gon/nelson-gon.github.io/blob/master/images/dog-test.png?raw=true")
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
li_thresh = threshold_li(gray_img, initial_guess=np.quantile(gray_img,0.95))
thresholded_image = gray_img > li_thresh
thresholded_numpy = np.array(thresholded_image).astype("uint8")
plt.imshow(thresholded_numpy, cmap="gray")
plt.axis("off")

