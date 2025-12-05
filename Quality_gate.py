import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=float, required=True)
args = parser.parse_args()

with open("metrics/accuracy.json", "r") as f:
    metrics = json.load(f)
accuracy = metrics["accuracy"]

if accuracy < args.threshold:
    raise ValueError(f"Model accuracy {accuracy:.2f} is below the threshold of {args.threshold:.2f}.")
else:
    print(f"Model passed the quality gate with accuracy {accuracy:.2f}.")
