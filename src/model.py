import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, inputSize, hiddenSize, numClasses):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(inputSize, hiddenSize)
        self.l2 = nn.Linear(hiddenSize, hiddenSize)
        self.l3 = nn.Linear(hiddenSize, hiddenSize)
        self.l4 = nn.Linear(hiddenSize, numClasses)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        out = self.relu(out)
        out = self.l4(out)

        return out