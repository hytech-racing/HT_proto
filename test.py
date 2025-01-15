import argparse
import json

# Load the json data and print it out
parser = argparse.ArgumentParser()
parser.add_argument('json_data', type=str)
args = parser.parse_args()

data = json.loads(args.json_data)

print(data)

