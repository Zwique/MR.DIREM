# MR.DIREM
<img src='https://miro.medium.com/v2/resize:fit:1400/1*_c2-NrOCPvlrSNzE2ZaX1g.jpeg' style='width:50%'/>
This Python script scans a web server for common directories specified in a file. It checks each directory path against a provided base URL to determine if the directory exists on the server. The script uses colored text to provide visual feedback about the status of each directory check, making it easier to identify which directories are present, forbidden, or not found.

## Features
- **Directory Checking:** Verifies the presence of directories on the specified URL.
- **Colored Output:** Uses colors to indicate different statuses:
  - **Green:** Directory found (HTTP 200 OK).
  - **Yellow:** Access forbidden (HTTP 403 Forbidden).
  - **Red:** Directory not found (HTTP 404 Not Found).
  - **Cyan:** Starting scan message.
  - **Magenta:** Completion message.
- **Missing Library Handling:** Checks for required libraries and installs them if necessary.
- **Fun ASCII Art:** Displays an ASCII cow with a message at the start.

## Requirements
### Python 3 Libraries: requests, colorama, cowsay

## Usage
```
python3 directory_scanner.py <base_url> <wordlists>
```

## Example
```
python3 directory_scanner.py http://example.com ~/path/directories.txt
```

## Notes
> [!IMPORTANT]
> Ensure the file specified in <wordlists> exists and contains one directory path per line.
> 
> The script will provide feedback for each directory, indicating whether it was found, access was forbidden, or it was not found.
