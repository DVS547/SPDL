#!/usr/bin/env python3
# Testing out a file
# put in the same folder as object_detection.py
#
"""Dog detection 
 - Takes an input image and tries to detect person, dog, or cat.
 - If it detects a dog, detect whether it is being good or bad.
 - Saves images of dogs and labels them as being either good or bad with a time stamp.
"""
import argparse
import io
import sys
from PIL import Image
from PIL import ImageDraw

from aiy.vision.inference import ImageInference
from aiy.vision.models import object_detection

def crop_center(image):
    width, height = image.size
    size = min(width, height)
    x, y = (width - size) / 2, (height - size) / 2
    return image.crop((x, y, x + size, y + size)), (x, y)

def read_stdin():
    return io.BytesIO(sys.stdin.buffer.read())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', dest='input', required=True)
    parser.add_argument('--output', '-o', dest='output')
    args = parser.parse_args()

    with ImageInference(object_detection.model()) as inference:
        image = Image.open(read_stdin() if args.input == '-' else args.input)
        image_center, offset = crop_center(image)
        draw = ImageDraw.Draw(image)
        result = inference.run(image_center)
        for i, obj in enumerate(object_detection.get_objects(result, 0.3, offset)):
            print('Object #%d: %s' % (i, str(obj)))
            x, y, width, height = obj.bounding_box
# Manipulating object here
            try:
                if obj.kind == PERSON
                    print('I found a Person!')
       
            except KeyboardInterrupt:
                print('I did not find a person and there was a keyboard interrupt exception.')
            except:
                print('I did not find a person and there was some error with your code')
            if obj.kind == PERSON
                print('I found a person!')
#  end my code             
#            draw.rectangle((x, y, x + width, y + height), outline='red')
        if args.output:
            image.save(args.output)


if __name__ == '__main__':
    main()
