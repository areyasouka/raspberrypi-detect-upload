# libcamera-still -r -t 1 -o input/picture.jpg
# python detect.py -i input/picture.jpg -m yolov8n.pt -o output/results.json -oi output/results.jpg

from ultralytics import YOLO
from PIL import Image
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Helper to run Ultralytics YOLO on images")
    parser.add_argument('--input', '-i', type=str, help='Input file path', required=True)
    parser.add_argument('--model', '-m', type=str, default='yolov8n.pt', help='Model to use')
    parser.add_argument('--output-json', '-o', type=str, default='results.json', help='Output file path')
    parser.add_argument('--output-image', '-oi', type=str, default='results.jpg', help='Model to use')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    model = YOLO(args.model)
    results = model(args.input) # results = model('https://ultralytics.com/images/bus.jpg')
    for r in results:
        if args.output_image:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            # im.show()  # show image
            im.save(args.output_image)  # save image
        if args.output_json:
            with open(args.output_json, 'w') as f:
                f.write(r.tojson())

if __name__ == '__main__':
    main()