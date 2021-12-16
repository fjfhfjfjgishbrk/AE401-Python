import numpy as np

IMAGE_LAYERS = 3
IMAGE_SIZE = 9
CONV_L1_LAYERS = 15
CONV_L1_SIZE = 5

convL1 = []
biasL1 = []


class ConvKernalNormal:

    def __init__(self, layerCount, x, y):
        self.filters = np.random.randn(x, y, layerCount) / 9
        self.x = x
        self.y = y

    def iterRegion(self, input):
        x, y, c = input.shape
        region = np.array([])
        for i in range(x - self.x):
            for j in range(y - self.y):
                for layer in range(c):
                    np.append(region, input[i:(i + self.x), j:(j + self.y), layer])
                np.moveaxis(region, 0, -1)
                yield region, i, j

    def forward(self, input, bias):
        x, y, c = input.shape
        output = np.zeros((x - self.x, y - self.y))
        for region, i, j in self.iterRegion(input):
            output[i, j] += np.sum(region * self.filters)
            output[i, j] += bias[i, j]
        return output


class Bias:

    def __init__(self, layerCount, x, y):
        self.values = np.random.randn(layerCount, x, y) / 9
        self.x = x
        self.y = y


def main(image):
    outputL1 = conv_forward(image, convL1, biasL1)
    return


def init():
    for i in range(CONV_L1_LAYERS):
        convL1.append(ConvKernalNormal(IMAGE_LAYERS, CONV_L1_SIZE, CONV_L1_SIZE))
    global biasL1
    biasL1 = Bias(IMAGE_LAYERS, IMAGE_SIZE - CONV_L1_SIZE + 1, IMAGE_SIZE - CONV_L1_SIZE + 1)
    return


def relu(x):
    return x if x >= 0 else 0


def conv_forward(image, kernallist, bias):
    output = np.array([])
    for i in range(len(kernallist)):
        np.append(output, kernallist[i].forward(image, bias[i]))
    np.moveaxis(output, 0, -1)

    return output
