# Audio-Splitter-for-ElevenLabs
This tool is designed to split audio files into segments under 10MB, making it easier to upload large amounts of data to ElevenLabs, which has a 10MB limit per file. It supports audio files directly and can convert video files to audio to ensure ease of access and manipulation.

### Prerequisites
- **Python**: Ensure Python 3.
x is installed. Download Python: https://www.python.org/downloads/ and make sure to select the "Add Python 3.x to PATH" option during installation.
- **FFmpeg**: Download FFmpeg:
https://ffmpeg.org/download.html. After downloading, extract the files and add the path to the FFmpeg 'bin' folder to your system's PATH environment variable.

Adding to PATH

Instructions on how to edit your PATH variable will differ slightly depending on your operating system. Here's a general guide for Windows users:

    Find the folders:
        Locate the bin folder within your Python installation directory (e.g., C:\Python310\bin)
        Locate the bin folder within your FFmpeg installation.
    Edit system variables: Search for "Edit the system environment variables" in your Windows search bar and open it.
    Click "Environment Variables"
    Edit PATH: Under "System variables", find the "Path" variable and click "Edit".
    Add new paths: Click "New" and paste the path to your Python's bin folder. Click "New" again and paste the path to FFmpeg's bin folder. Make sure each path is on a separate line.
    Click "OK" on all open windows. You might need to restart your computer for the changes to take effect.

### Setup
Download and unzip the repository to your preferred location.

### Windows Users
Double-click the `run.bat` file to automatically install Python packages and start the application.

## Usage
Follow the on-screen prompts to select your files and configure the splitting parameters. The tool supports direct audio file splitting and video to audio conversion.
