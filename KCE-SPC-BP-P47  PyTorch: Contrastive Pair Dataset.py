import torch, random
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

class ContrastiveDataset(Dataset):
    def __init__(self, base):
        self.base, self.labels = base, [y for _, y in base]
        self.cls_idx = {l: [i for i,y in enumerate(self.labels) if y==l] for l in set(self.labels)}
    def __len__(self): return len(self.base)
    def __getitem__(self, i):
        x1,y1 = self.base[i]
        if random.random()<0.5: x2,_=self.base[random.choice(self.cls_idx[y1])]; t=1
        else:
            y2=random.choice([l for l in self.cls_idx if l!=y1])
            x2,_=self.base[random.choice(self.cls_idx[y2])]; t=0
        return x1,x2,torch.tensor(t)

# Example with MNIST
mnist = datasets.MNIST("./data", train=True, download=True, transform=transforms.ToTensor())
loader = DataLoader(ContrastiveDataset(mnist), batch_size=2, shuffle=True)
print(next(iter(loader))[2])  # print pair labels
