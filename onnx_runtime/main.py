import cv2
import numpy as np
import preprocess_yolov4 as pre
import postprocess_yolov4 as post
from PIL import Image
input_size = 416
original_image = cv2.imread("kite.jpg")
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
original_image_size = original_image.shape[:2]
image_data = pre.image_preprocess(np.copy(original_image), [input_size, input_size])
image_data = image_data[np.newaxis, ...].astype(np.float32)
print("Preprocessed image shape:", image_data.shape) # shape of the preprocessed input
import onnxruntime as rt

sess = rt.InferenceSession("yolov4.onnx")

output_name = sess.get_outputs()[0].name
input_name = sess.get_inputs()[0].name

detections = sess.run([output_name], {input_name: image_data})[0]

print("Output shape:", detections.shape)

image = post.image_postprocess(original_image, input_size, detections)

image = Image.fromarray(image)
image.save("kite-with-objects.jpg")
