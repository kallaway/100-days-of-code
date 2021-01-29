# Yolov4

This is the yolov 4 model from the following [NVIDIA tutorial](https://developer.nvidia.com/blog/announcing-onnx-runtime-for-jetson/#:~:text=ONNX%20Runtime%20optimizes%20models%20to,and%20control%20the%20inference%20sessions.).

I had to not include the yolov4.onxx file because it is 256MB.  It can be downloaded with the following command:

	wget https://github.com/onnx/models/blob/master/vision/object_detection_segmentation/yolov4/model/yolov4.onnx?raw=true -O yolov4.onnx
