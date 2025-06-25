import requests
import json

AZURE_METADATA_URL = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"

def get_instance_metadata(key: str = None) -> dict:
    headers = {'Metadata': 'true'}
    response = requests.get(AZURE_METADATA_URL, headers=headers)
    response.raise_for_status()
    metadata = response.json()

    if key:
        keys = key.split(".")
        for k in keys:
            metadata = metadata.get(k)
            if metadata is None:
                raise KeyError(f"Key '{key}' not found in metadata")
    return metadata

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Query Azure VM Metadata")
    parser.add_argument("--key", type=str, help="Specific metadata key to retrieve (e.g., 'compute.name')")
    args = parser.parse_args()

    try:
        metadata = get_instance_metadata(args.key)
        print(json.dumps(metadata, indent=2))
    except Exception as e:
        print(f"Error: {e}")
