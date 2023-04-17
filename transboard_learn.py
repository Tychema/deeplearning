from torch.utils.tensorboard import SummaryWriter
import numpy as np
import cv2
if __name__ == '__main__':
    writer = SummaryWriter("logs")
    # writer.add_image()
    #tag:标题
    #scalar_value:数值
    #global_step:x轴的步长
    # for i in range(100):
    #     writer.add_scalar("y=2x",3*i,i)

    img_path='dataset/train/ants_image/0013035.jpg'
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    #dataformats="HWC" 图片参数的问题
    #img(宽度，高度，通道) 而参数默认传递的是(通道，高度，款段)所以要指定为“HWC”
    writer.add_image("test",img,1,dataformats="HWC")
    writer.close()
