Steps:
1)Upload the source dataset to kaggle input , and then run the human_filter.ipynb to get the filtered dataset. 
2)Upload the filtered dataset and run the filtered-hum-det.ipynb to get the new fine tuned yolov11 pytorch model(best_filtered.pt).
3) run the onnx_conv.py to export the pytorch to onnx.
4) python -m onnxruntime.tools.convert_onnx_models_to_ort best_filtered.onnx --output_dir ./converted
Further run the above command to convert the onnx to ort.(here i renamed my model's name as best_filtered)
