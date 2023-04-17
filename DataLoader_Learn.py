import torch
import cv2
from torch.utils.data import Dataset
import os


class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(root_dir, label_dir)
        self.img_name = os.listdir(self.path)

    def __getitem__(self, index):
        if index > self.__len__():
            print("索引越界")
            return "索引越界"
        img_path = os.path.join(self.root_dir, self.label_dir, self.img_name[index])
        # path: 该参数制定图片的路径，可以使用相对路径，也可以使用绝对路径；
        # flags: 指定以何种方式加载图片，有三个取值：
        # cv2.IMREAD_COLOR: 读取一副彩色图片，图片的透明度会被忽略，默认为该值，实际取值为1；
        # cv2.IMREAD_GRAYSCALE: 以灰度模式读取一张图片，实际取值为0
        # cv2.IMREAD_UNCHANGED: 加载一副彩色图像，透明度不会被忽略。
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        label = self.label_dir
        cv2.imshow("image", img)  # 显示图片
        cv2.waitKey(0)  # 等待按键
        return img, label

    def __len__(self):
        return len(self.img_name)


if __name__ == '__main__':
    root_dir = "dataset/val"
    ants_label_dir = "ants"
    bees_label_dir = "bees"
    ants_dataset = MyData(root_dir, ants_label_dir)
    bees_dataset = MyData(root_dir, bees_label_dir)
    print(str(ants_dataset.__len__())+" "+str(bees_dataset.__len__()))
