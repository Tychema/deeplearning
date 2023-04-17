import torch
from torch.utils.data import Dataset,DataLoader
if __name__ == '__main__':
    print(dir(torch))

class MyDataSet(Dataset):
    #read data and preprocess
    def __init__(self,file):
        self.data="data"

    #return one sample of dataset at a time
    def __getitem__(self, index):
        return self.data[index]

    #return the size of dataset
    def __len__(self):
        return len(self.data)