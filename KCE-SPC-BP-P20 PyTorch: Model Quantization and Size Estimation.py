import torch, torch.nn as nn, os
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# Data & model
val = datasets.ImageFolder("data/val", transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])]))
loader = DataLoader(val,16)
m = models.resnet18(); m.fc = nn.Linear(m.fc.in_features,len(val.classes))
m.load_state_dict(torch.load("transfer_model.pth",map_location="cpu")); m.eval()

# Helper
def test(mod,name):
    acc = sum((mod(x).argmax(1)==y).sum().item() for x,y in loader)/len(val)
    torch.save(mod.state_dict(),f"{name}.pth")
    print(name,": acc=",round(acc,3)," size=",round(os.path.getsize(f"{name}.pth")/1e6,2),"MB")

# Run
test(m,"baseline")
test(torch.quantization.quantize_dynamic(m,{nn.Linear},dtype=torch.qint8),"dynamic")
m.qconfig=torch.quantization.get_default_qconfig("fbgemm")
test(torch.quantization.convert(torch.quantization.prepare(m)),"static")
