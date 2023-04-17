from torchvision.transforms import transforms
import cv2
if __name__ == '__main__':
    #通过transform.ToTensor去转换成一个Tensor
    #Tensor数据类型
    root_path="dataset/train/ants_image/0013035.jpg"
    img_path="dataset/train/ants_image/0013035.jpg"
    img=cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print(type(img))
    #ToTensor(PIL or numpy.ndarray)
    img_tensor=transforms.ToTensor().__call__(img)
    print(type(img_tensor))
    print(img_tensor)
    #output[channel] = (input[channel] - mean[channel]) / std[channel]
    trans_norm=transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
    img_norm=trans_norm.__call__(img_tensor)
