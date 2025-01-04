import qrcode
import yaml

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

input_data = config['input_data']
data = input_data['text']
output_path = input_data['output_path']
image_format = input_data['image_format'] # Image format is not directly used with this library

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(output_path)

print(f"QR code generated and saved as {output_path}")
