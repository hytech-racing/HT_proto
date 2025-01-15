import argparse
import json

# Load the json data and print it out

# curl \
#   -X POST \
#   -H "Accept: application/vnd.github.v3+json" \
#   https://api.github.com/repos/octocat/hello-world/dispatches \
#   -d '{"event_type":"event_type", "client_payload": {"foo": "bar"}}'



parser = argparse.ArgumentParser()
parser.add_argument('json_data', type=str)
args = parser.parse_args()

data = json.loads(args.json_data)

print(data)

