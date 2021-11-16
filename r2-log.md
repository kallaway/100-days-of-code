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
