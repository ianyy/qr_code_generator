# QR Code Generator

This project contains a Python script (`generate_qr.py`) that generates QR codes based on the configuration provided in the `config.yaml` file.

## Usage

1. **Configuration:** Create a `config.yaml` file with the following structure:

   ```yaml
   input_data:
     text: "Your text or URL to encode"
     output_path: "desired_output_filename.png"
   ```

2. **Dependencies:** Ensure you have the following Python libraries installed:
   - `qrcode`: For generating QR codes.
   - `pyyaml`: For reading YAML configuration files.

   You can install these using pip:
   ```bash
   pip install qrcode pyyaml
   ```

3. **Run the script:** Execute the `generate_qr.py` script:

   ```bash
   python generate_qr.py
   ```

   This will generate a QR code image based on the settings in `config.yaml`.

## Example

With the following `config.yaml`:

```yaml
input_data:
  text: "https://www.example.com"
  output_path: "example_qr.png"
