import json
import requests
import os
import argparse
from dotenv import load_dotenv


load_dotenv(".env")
url = os.getenv("API_TRANSCRIPT_URL")

def _parse_args():
    parser = argparse.ArgumentParser(description='Audio translator')
    parser.add_argument('-f', '--filenames', nargs='+', default=[])
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()

    files = [('files', open(f, 'rb')) for f in args.filenames]
    response = requests.post(url, files=files)
    json_response = json.dumps(response.json(), indent=4, ensure_ascii=False)

    print(json_response)
