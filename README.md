1) Run the notebook to get the new fine tuned yolov11 pytorch model.
2) run the onnx_conv.py to export the pytorch to onnx.
3) python -m onnxruntime.tools.convert_onnx_models_to_ort best_filtered.onnx --output_dir ./converted
Further run the above command to convert the onnx to ort.(here i renamed my model's name as best_filtered)
