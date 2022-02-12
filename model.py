import torch.nn as nn

class Model(nn.Module):
    
    def __init__(self, input_features=40346, hidden1=256, hidden2=32, output_features=3):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(input_features, hidden1)
        self.fc2 = nn.Linear(hidden1, hidden2)
        self.relu = nn.LeakyReLU()
        self.out = nn.Linear(hidden2, output_features)

    def forward(self, x):

        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.out(x)
        
        return x