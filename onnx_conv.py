from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("best_filtered.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'best_filtered.onnx'

# Load the exported ONNX model
onnx_model = YOLO("best_filtered.onnx")

# Run inference
results = onnx_model("hum_det2.jpg")




