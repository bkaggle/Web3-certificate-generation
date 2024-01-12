from openai import OpenAI
from decouple import config
import cv2

# Set your OpenAI API key from environment variable
openai_api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Use DALL-E to generate an image based on a prompt
prompt = 'Generate a certificate background with colors and patterns suitable for 10 Academy certificates.'
response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)


# Get the generated image URL from the response
image_url = response.data[0].url

# You can download the image using a library like requests or urllib
# For example, using requests:
import requests

image_response = requests.get(image_url)
with open('../images/generated_certificate_background.jpg', 'wb') as f:
    f.write(image_response.content)

# Load the generated image using CV2
base_background_img = cv2.imread('../images/generated_certificate_background.jpg')

# Placeholder coordinates for the Full Name text
x_full_name = 100
y_full_name = 100

# Placeholder coordinates for the Logo
x_logo = 50
y_logo = 50
logo = cv2.imread('../images/logo.png')

# Placeholder coordinates for the Date text
x_date = 200
y_date = 150

# Function to overlay text on the certificate
def overlay_text(image, text, position, font_size, color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, position, font, font_size, color, 2, cv2.LINE_AA)

# Insert Full Name, Logo, and Date on the certificate
overlay_text(base_background_img, "Naol Lamesa", (x_full_name, y_full_name), 1.0, (255, 255, 255))
base_background_img[y_logo:y_logo + logo.shape[0], x_logo:x_logo + logo.shape[1]] = logo
overlay_text(base_background_img, "January 9, 2024", (x_date, y_date), 1.0, (255, 255, 255))

# Save the final certificate image
output_path = '../images/certificate.png'
cv2.imwrite(output_path, base_background_img)

# Display the final certificate image
cv2.imshow('Certificate', base_background_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
