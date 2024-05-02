# Audio-Splitter-for-ElevenLabs

This tool is designed to split audio and video files into segments under 10MB, making it easier to upload large amounts of data to ElevenLabs, which imposes a 10MB limit per file. It supports direct audio file handling and can convert video files to audio for easier manipulation.

## Prerequisites

- **Python**: Ensure Python 3.x is installed. [Download Python](https://www.python.org/downloads/) and make sure to select the "Add Python 3.x to PATH" option during installation.
- **FFmpeg**: [Download FFmpeg](https://ffmpeg.org/download.html). After downloading, extract the files and add the path to the FFmpeg 'bin' folder to your system's PATH environment variable.

## Adding to PATH

Editing your PATH variable allows your operating system to locate executables from the command line or terminal window.

### For Windows Users:

1. **Find the folders**:
   - Locate the `bin` folder within your Python installation directory (e.g., `C:\Python310\bin`).
   - Locate the `bin` folder within your FFmpeg installation.

2. **Edit system variables**:
   - Search for "Edit the system environment variables" in your Windows search bar and open it.

3. **Environment Variables**:
   - Click "Environment Variables".

4. **Edit PATH**:
   - Under "System variables", find the "Path" variable and click "Edit".

5. **Add new paths**:
   - Click "New" and paste the path to your Python's `bin` folder.
   - Click "New" again and paste the path to FFmpeg's `bin` folder. Ensure each path is on a separate line.

6. **Apply Changes**:
   - Click "OK" on all open windows. You might need to restart your computer for the changes to take effect.

## Setup

Download and unzip the repository to your preferred location.

### Windows Users

- Double-click the `run.bat` file to automatically install Python packages and start the application. This script handles checking for Python and FFmpeg, installs required dependencies, and runs the tool.

## Usage

Follow the on-screen prompts to select your files and configure the splitting parameters. The tool allows you to:
- Split audio files directly.
- Convert video files to audio and then split them.
- Specify the desired size for each segment to comply with platform limits.

## Contributing

Contributions to the tool are welcome. Please fork the repository, make your changes, and submit a pull request. You can also create issues for bugs or feature suggestions.
