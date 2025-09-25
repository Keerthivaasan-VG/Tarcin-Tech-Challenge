import torch, torch.nn as nn, torch.optim as optim
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader
from PIL import Image

# Data
transform = transforms.Compose([transforms.Resize((224,224)), transforms.RandomHorizontalFlip(), transforms.ToTensor(), transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])
data = {x: datasets.ImageFolder(f"data/{x}", transform=transform) for x in ['train','val']}
loaders = {x: DataLoader(data[x], batch_size=16, shuffle=True) for x in ['train','val']}
sizes = {x: len(data[x]) for x in ['train','val']}
classes = data['train'].classes

# Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True)
for p in model.parameters(): p.requires_grad=False
model.fc = nn.Linear(model.fc.in_features,len(classes)); model = model.to(device)
criterion = nn.CrossEntropyLoss(); optimizer = optim.Adam(model.fc.parameters(), lr=0.001)

# Training
for epoch in range(5):
    print(f"Epoch {epoch+1}/5")
    for phase in ['train','val']:
        model.train() if phase=='train' else model.eval()
        loss_sum=corrects=0
        for x,y in loaders[phase]:
            x,y=x.to(device),y.to(device); optimizer.zero_grad()
            with torch.set_grad_enabled(phase=='train'):
                out=model(x); _,preds=torch.max(out,1); loss=criterion(out,y)
                if phase=='train': loss.backward(); optimizer.step()
            loss_sum+=loss.item()*x.size(0); corrects+=torch.sum(preds==y.data)
        print(f"{phase} Loss:{loss_sum/sizes[phase]:.4f} Acc:{corrects.double()/sizes[phase]:.4f}")

# Save model
torch.save(model.state_dict(),"transfer_model.pth")

# Predict new image
img = Image.open("test_image.jpg")
tensor = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor(), transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])(img).unsqueeze(0).to(device)
model.load_state_dict(torch.load("transfer_model.pth")); model.eval()
with torch.no_grad(): out=model(tensor); _,pred=torch.max(out,1); print("Predicted class:",classes[pred.item()])
