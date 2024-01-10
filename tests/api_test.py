import pytest
from unittest.mock import patch, MagicMock
import cv2
from backend.api import certificate

def test_generate_and_save_certificate():
    # Mock the OpenAI API response
    with patch('certificate.client.images.generate') as mock_generate:
        mock_response = MagicMock()
        mock_response.data = [{'url': 'mocked_image_url'}]
        mock_generate.return_value = mock_response

        # Mock the image download
        with patch('your_script_name.requests.get') as mock_requests_get:
            mock_requests_get.return_value.content = b'mocked_image_content'

            # Mock the cv2.imwrite function
            with patch('your_script_name.cv2.imwrite') as mock_imwrite:
                # Run the function to generate and save the certificate
                certificate()

                # Check if the cv2.imwrite function was called with the correct arguments
                mock_imwrite.assert_called_once_with('../images/certificate.png', cv2.imdecode(mock_requests_get.return_value.content, 1))
