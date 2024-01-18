# DNS Monitoring Script

This script monitors changes to the DNS record of a specified domain and record type. It uses asyncio for asynchronous execution and rich for enhanced console output.

## Requirements

- Python 3.7 or higher
- Install dependencies using: `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/RadoGold57/dnsrecord.git

2. Navigate to the project directory:
````
    cd dnsrecord
````

3. Install dependencies:
````
   pip install -r requirements.txt
````
4. Run the script:
````
    python dns_monitor.py -d example.com -r A -t 10
````
![Screenshot from 2024-01-17 19-26-06](https://github.com/RadoGold57/dnsrecord/assets/64227801/76327b47-b1c5-4518-bdf1-6b5292642258)

## Configuration

    Modify the requirements.txt file to adjust library versions if needed.

## Contributing

If you encounter issues or have suggestions, feel free to open an issue or create a pull request.

## License

This script is licensed under the MIT License.
