import torch, torch.nn as nn, torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

z_dim, bs, lr, epochs = 100, 64, 0.0002, 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
loader = DataLoader(datasets.MNIST('./data', train=True, download=True,
                                   transform=transforms.Compose([transforms.Resize(28), transforms.ToTensor(), transforms.Normalize([0.5],[0.5])])),
                    batch_size=bs, shuffle=True)

G = nn.Sequential(nn.Linear(z_dim,128), nn.ReLU(True), nn.Linear(128,784), nn.Tanh()).to(device)
D = nn.Sequential(nn.Flatten(), nn.Linear(784,128), nn.LeakyReLU(0.2), nn.Linear(128,1), nn.Sigmoid()).to(device)
crit = nn.BCELoss(); optG, optD = optim.Adam(G.parameters(), lr=lr), optim.Adam(D.parameters(), lr=lr)

for e in range(epochs):
    for imgs,_ in loader:
        imgs = imgs.to(device); bs = imgs.size(0)
        real, fake = torch.ones(bs,1).to(device), torch.zeros(bs,1).to(device)
        z = torch.randn(bs,z_dim).to(device); f_imgs = G(z).view(-1,1,28,28)
        optD.zero_grad(); (crit(D(imgs),real)+crit(D(f_imgs.detach()),fake)).backward(); optD.step()
        z = torch.randn(bs,z_dim).to(device); optG.zero_grad(); crit(D(G(z).view(-1,1,28,28)),real).backward(); optG.step()

z = torch.randn(16,z_dim).to(device); f = G(z).view(-1,1,28,28).detach().cpu()
for i in range(16): plt.subplot(4,4,i+1); plt.imshow(f[i][0]*0.5+0.5,cmap='gray'); plt.axis('off')
plt.show()
