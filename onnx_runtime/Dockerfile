FROM mcr.microsoft.com/azureml/onnxruntime:v.1.4.0-jetpack4.4-l4t-base-r32.4.3
WORKDIR .
RUN apt-get update && apt-get install -y python3-pip libprotobuf-dev protobuf-compiler python3-scipy
RUN python3 -m pip install onnx==1.6.0 easydict matplotlib
CMD ["/bin/bash"]
