import os

# The path to your OneDrive main folder (adapt accordingly)
onedrive_path = "C://Users//I585524//OneDrive - SAP SE//Recordings"

# The path to your Teams recordings (update this as needed)
recording_path = "Recordings//"

# Full path to the folder with recordings
#folder_path = os.path.join(onedrive_path, recording_path)

# Get list of all files in the folder
files = os.listdir(onedrive_path)

# Filter only video files (with extension .mp4 in this example)
video_files = [file for file in files if file.endswith('.mp4')]

# Find the latest video file by comparing last modification times
latest_video_file = max(video_files, key=lambda x: os.path.getmtime(os.path.join(onedrive_path, x)))

# Full path to the latest video
latest_video_path = os.path.join(onedrive_path, latest_video_file)

# Get the size of the file
file_size = os.path.getsize(latest_video_path)

# Now you can open and read the latest video file like a local file
with open(latest_video_path, 'rb') as video_file:
    video_data = video_file.read()

# Do something with video
# Print the name and size of the file
print("Video name: ", latest_video_file)
print("Video size: ", file_size, "bytes")