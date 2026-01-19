import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transformer = transforms.ToTensor()

data_train = datasets.MNIST(root='./data' , train = True ,  transform = transformer)
data_test = datasets.MNIST(root='./data' , train = False ,  transform = transformer)

train_loader = DataLoader(data_train , batch_size=  80 ,shuffle= True )
test_loader = DataLoader(data_test , batch_size=  80 ,shuffle= False )

class net(nn.Module) :
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28,128)
        self.fc2 = nn.Linear(128,128)
        self.fc3 = nn.Linear(128,10)
    def forward(self,x) :
        x = x.view(x.size(0),-1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
model = net()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters() , lr = 0.001)

epochs = 5 
for epoch in  range(epochs) :
    for images , labels in train_loader :
        optimizer.zero_grad()
        output = model(images)
        loss = criterion(output , labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
correct = 0
total = 0
with torch.no_grad() :
    for images , labels in test_loader :
        output = model(images)
        prediction = torch.argmax(output , dim = 1)
        total += labels.size(0)
        correct += (prediction == labels).sum().item()
print(f"Test Accuracy: {100 * correct / total:.2f}%")





