import unittest
from unittest.mock import patch
from metadata_query.fetch_metadata import get_instance_metadata

mock_metadata = {
    "compute": {
        "name": "test-vm",
        "location": "eastus"
    },
    "network": {
        "interface": []
    }
}

class TestMetadataQuery(unittest.TestCase):

    @patch("metadata_query.fetch_metadata.requests.get")
    def test_fetch_full_metadata(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_metadata

        result = get_instance_metadata()
        self.assertEqual(result, mock_metadata)

    @patch("metadata_query.fetch_metadata.requests.get")
    def test_fetch_specific_key(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_metadata

        result = get_instance_metadata("compute.name")
        self.assertEqual(result, "test-vm")

    @patch("metadata_query.fetch_metadata.requests.get")
    def test_key_not_found(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_metadata

        with self.assertRaises(KeyError):
            get_instance_metadata("compute.invalidkey")

if __name__ == "__main__":
    unittest.main()
