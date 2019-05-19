import argparse
from concurrent.futures import ThreadPoolExecutor
from impl import classify_image_remote

parser = argparse.ArgumentParser()
parser.add_argument('images', nargs='+', help='Image(s) to classify')
args = parser.parse_args()

with ThreadPoolExecutor(max_workers=128) as executor:
    for image in args.images:    
        executor.submit(lambda: classify_image_remote(image)).result()
