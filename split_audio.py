import subprocess
import pkg_resources
import sys
from tqdm import tqdm
import os
import json

# Checks for missing Python packages and installs them
def install_missing_packages():
    required = {'tqdm'}  # Set of required packages
    installed = {pkg.key for pkg in pkg_resources.working_set}  # Set of currently installed packages
    missing = required - installed  # Determine missing packages

    if missing:
        print("Missing dependencies are being installed...")
        python = sys.executable
        # Install missing packages using pip
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        print("Installation of missing Python packages complete.")

# Checks if FFmpeg is correctly installed and accessible
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("FFmpeg is installed and ready.")
    except subprocess.CalledProcessError:
        print("FFmpeg is not installed correctly.")
    except FileNotFoundError:
        print("FFmpeg is not available on your system.")
        print("Please install FFmpeg from https://ffmpeg.org/download.html")

# Loads the configuration from a JSON file
def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {
            "target_size_mb": 9.5,
            "prompt_for_target_size": True,
            "prompt_for_action": True,
            "supported_audio_file_types": [
                ".mp3", ".wav", ".aac", ".ogg", ".m4a", ".flac"
            ],
            "supported_video_file_types": [
                ".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv"
            ]
        }

# Lists files in a directory that match the supported file types
def list_files(directory, file_types):
    files = [f for f in os.listdir(directory) if any(f.endswith(ext) for ext in file_types)]
    if not files:
        print("No files of the selected type found in the directory.")
        return None
    print("\nFiles found:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    return files

# Converts a video file to an audio file using FFmpeg
def convert_to_audio(video_path, output_folder):
    audio_output = os.path.join(output_folder, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")
    cmd = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'libmp3lame', '-y', audio_output]
    subprocess.run(cmd, check=True)
    print(f"Converted video to audio at: {audio_output}")
    return audio_output

# Splits media into segments of a specified size using FFmpeg
def split_media(file_path, target_size_mb, output_parent_folder):
    output_folder = os.path.join(output_parent_folder, os.path.splitext(os.path.basename(file_path))[0] + "_splits")
    os.makedirs(output_folder, exist_ok=True)
    media_type = 'audio' if file_path.endswith(('.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac')) else 'video'
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    duration_seconds = float(result.stdout.strip())
    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    segment_duration = (duration_seconds * target_size_mb) / file_size_mb
    num_segments = int(duration_seconds // segment_duration + (duration_seconds % segment_duration > 0))

    print(f"Total {media_type} duration: {duration_seconds} seconds")
    print(f"Total {media_type} size: {file_size_mb} MB")
    print(f"Calculated segment duration: {segment_duration} seconds")
    print(f"Expected number of segments: {num_segments}")

    start = 0
    for segment_index in tqdm(range(1, num_segments + 1), desc=f"Splitting {media_type}"):
        segment_file = os.path.join(output_folder, f"segment_{segment_index}{os.path.splitext(file_path)[1]}")
        cmd = [
            'ffmpeg', '-i', file_path, '-acodec', 'copy', '-vcodec', 'copy', '-ss', str(start),
            '-t', str(segment_duration), '-y', segment_file
        ]
        subprocess.run(cmd, check=True)
        start += segment_duration

    print("All segments have been created.")
    return output_folder

# Main function to run the program
def main():
    install_missing_packages()
    check_ffmpeg()

    config = load_config()
    while True:
        print("Select the directory to search for media files:")
        print("1. Current directory")
        print("2. Enter a custom directory")
        choice = input("Enter your choice (1 or 2): ")

        directory = os.getcwd() if choice == '1' else input("Enter the full path to your directory: ") if choice == '2' else None
        if not directory:
            print("Invalid choice.")
            continue

        print("Select the type of file to handle:")
        print("1. Audio")
        print("2. Video")
        file_type_choice = input("Enter your choice (1 for Audio, 2 for Video): ")

        file_types = config["supported_audio_file_types"] if file_type_choice == '1' else config["supported_video_file_types"] if file_type_choice == '2' else None
        if not file_types:
            print("Invalid file type choice.")
            continue

        files = list_files(directory, file_types)
        if not files:
            continue

        file_choice = int(input("Enter the number of the file you want to handle: ")) - 1
        if not (0 <= file_choice < len(files)):
            print("Invalid selection.")
            continue

        file_path = os.path.join(directory, files[file_choice])

        if file_type_choice == '2':  # Video file processing
            convert_choice = input("Convert this video to audio before splitting? (Y/N): ")
            if convert_choice.lower() == 'y':
                file_path = convert_to_audio(file_path, directory)
                if not file_path:
                    continue

        # Directly proceed to splitting for audio files
        if file_type_choice == '1' or (file_type_choice == '2' and convert_choice.lower() == 'y'):
            if config["prompt_for_target_size"]:
                use_default = input(f"Use default target size {config['target_size_mb']} MB? (Y/N): ")
                target_size_mb = config["target_size_mb"] if use_default.lower() == 'y' else float(input("Enter custom target file size in MB: "))
            else:
                target_size_mb = config["target_size_mb"]
            output_folder = split_media(file_path, target_size_mb, "Media_Splits")

        if config["prompt_for_action"]:
            again = input("Do you want to handle another file? (Y/N): ")
            if again.lower() == 'n':
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()
