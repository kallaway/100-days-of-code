# #100DaysOfThesis Log - Round 2 - Conor O'Mara

The log of my #100DaysOfCode challenge. Started on November 15th 2021 (running to Feb 23rd 2021).

## Log

### R2D1 (15/11/21)
Started literature review on thesis. Started with Tensorflowlite guide on pose estimation that uses MoveNet and PoseNet. Covered the mAP metric for evaluation of object detection models. Came across the [COCO dataset](https://cocodataset.org/#home) and its API.

### R1D2 (16/11/21)
MoveNet uses MobileNetV2 as the image feature extractor. Began the [MobileNetV2 paper](https://arxiv.org/abs/1801.04381) for this covering;
 - Paper implements a lighter computational model with small accuracy tradeoff for deep neural networks used in computer vision.
 - Depthwise separable convolution (split colnvolution operator into 2 separate factorized layers)
 - Linear bottlenecks (the d-channel pixels (h x w) of the image lie on a smaller dimensional manifold and transforming space to this will to save computation (less dimensions to multiply) while overcoming information loss that is problematic with RELU operator somehow... :anguished: )

 ### R1D3 (17/11/21)
Tony's lectures on DNN. Covered the [receptive field of CNNs](https://distill.pub/2019/computing-receptive-fields/) of neurons and how this increases with deeper layers (determined by preceeding convolution and poolying layers).
Covered multiple kernels and understood how to follow the volume diagrams used in papers. Input image (m x n x c) with N kernels (k x k x c) will produce an output feature map of (m' x n' x N) where m' and n' depend in input size m x n, stride, padding, etc.


Covered model architectures of:
- [AlexNet](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) and a [closer look](https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/tutorials/tut6_slides.pdf) at it
- [VGG](https://arxiv.org/abs/1409.1556)
- GoogLeNet (of which there was also a [theoretical paper](https://arxiv.org/pdf/1310.6343.pdf) proving some bounds and the existence of a probability distribution of data represented by some Sparse network ???)


 ### R1D4 (18/11/21)
 Another lecture on GoogLeNet's architecture. Main features covered were:
 - [Inception architecture](https://arxiv.org/pdf/1312.4400.pdf) (network in a network - parallel network units too. Introduces 1x1 bottlenecks convolutions that reduce amount of multiplication)
 - [GoogLeNet paper](https://arxiv.org/pdf/1409.4842.pdf)
 - [Hebbian's principle](https://en.wikipedia.org/wiki/Hebbian_theory) (mentioned in the GoogLeNet paper)

 Moved onto [ResNet architecture](https://arxiv.org/pdf/1512.03385.pdf), residual networks, which made training more layers easier. [Veit paper](https://arxiv.org/pdf/1605.06431.pdf) suggests this is because we are making shallower networks which avoids vanishing gradient and helps convergence.
 ResNet paper also used [batch normalization](https://arxiv.org/pdf/1502.03167.pdf)

 ### R1D5 (19/11/21)
 More work on DNN architectures. Covered more on batch normalization. [Understanding BN fully remains an open question](https://papers.nips.cc/paper/2018/file/36072923bfc3cf47745d704feb489480-Paper.pdf). It normalizes all activations that enables faster convergence. BN removes the case where large gradient updates can result in diverging loss and activations growing uncrontrollably with network depth, leading to a limit on the size of the learning rates that can be used. BN enables training with larger learning rates.

[Squeeze-Excite network](https://arxiv.org/pdf/1709.01507.pdf) (and blocks) can be inserted into ResNet blocks between the lasdt convolution layer in the main path before the shortcut addition. There are 2 path in a SE block where on one path with an input (HxWxC) goes Global average pooling (1x1xC) -> FC -> ReLU -> FC -> Sigmoid (output of [0,1] for each channel c). This is used as a scale factor on the input. Leads to performance increase of 10% on ImageNet.

 ### R1D6 (20/11/21)
 [DenseNet](https://arxiv.org/pdf/1608.06993.pdf) covered which is comparable to ResNet but with more connectivity due to the concatenation (instead of summation) the output feature maps are concatenated. Up to 90% less params than ResNet and also has the short paths and therefore avoids exploding/vanishing gradient.

Also worth noting that in DenseNet the arrangement is: BN -> ReLu -> Conv (different to ResNet). This was suggested in the paper [Identity mapping in deep res nets (Zhang 2016)](https://arxiv.org/pdf/1603.05027.pdf).

[This paper](https://arxiv.org/pdf/1810.00736.pdf) covered an overall summary of the different architectures of the model zoo. Models such as ResNet, Xception, DenseNet have reduced the no. of params by reducing the number of FC layers and using global average pooling, however they have a large number of convolution layers so there is high computational complexity.

 ### R1D7 (21/11/21)
Looking at gradient descent. The loss function $J(\theta)$ for image classification is `Categorical cross entropy` (Shannon entropy).
$$ J(\theta) = - \Sigma_{j}^{C} y_{true, j} log(y_{pred, j})$$

where the ground truth $y_{true, j}$ will be a one-hot encoded vector $y_{true} = [0,0,0,1,0,0]$

Mini-batch gradient descent, with [momentum](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.57.5612&rep=rep1&type=pdf).

Ways to [prevent overfitting](https://www.jeremyjordan.me/deep-neural-networks-preventing-overfitting/) in NN and methods to prevent it such as: Early stopping, regularization, dropout.

Touched on the [exploding gradient problem](https://arxiv.org/pdf/1712.05577.pdf) this very in-depth paper looks to cover it.

Also looking at this paper and seeing the mention of the [SELU](https://pytorch.org/docs/stable/generated/torch.nn.SELU.html) activation function lead me to a Pytorch documentation page which links a paper of [Self-Normalizing Neural networks](https://arxiv.org/abs/1706.02515).

 ### R1D8 (22/11/21)
The exploding/vanishing gradient problem occurs when the error is backpropagated through the NN and increases exponentially from layer to layer. The gradient wrt early network parameters (early layers) gets exponentially larger from layer to layer, making it hard to train. There is also the same case with exponentially decreases. A couple ways to tackle this are: [Glorot initialisation](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf), Batch normalization and architectures ( like ResNet and DenseNet).

Learning rates can have different policies. In general it makes sense to decrease LR once accuracy has plateaued and decrease LR by a factor of 10.

[Cyclical learning rates](https://arxiv.org/pdf/1506.01186.pdf) have been successful at getting higher accuracy in shorter training times. [Warmup](https://arxiv.org/pdf/1608.03983.pdf) can also be used, which is a method of using a less aggressive learning rate at the start of training.

Adaptive Gradient Descent algorithms can be used instead of SGD which use optimisation algorithms for each parameter (and each parameter has its own learning rate).

[Ruder](https://arxiv.org/pdf/1609.04747.pdf) provides a good overview of all gradient descent optimization algorithms.