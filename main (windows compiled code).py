import sys
import os
from pytube import YouTube

def clear_terminal():
    # Clear terminal
    os.system('cls')

def get_executable_directory():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, use the executable directory
        return os.path.dirname(sys.executable)
    else:
        # If the application is run as a script, use the script's directory
        return os.path.dirname(os.path.abspath(__file__))

def check_if_downloads_directory_exists():
    # Tell the user what is happening
    print(f"Checking if downloads folder exists...")

    # Specify the path of the "downloads" directory
    directory_path = os.path.join(get_executable_directory(), "downloads")

    # Check if the "downloads" directory exists
    exists = os.path.exists(directory_path)

    # Tell the user that the folder check has been done
    print(f"Done!")
    return exists

def tell_user_downloads_directory_status(x):
    # Specify status from the given input
    status = x

    # Check the status's value
    if status == True:
        # If the "downloads" folder exists tell the user that the app will continue like normal
        print(f"Downloads folder exists, continuing like normal!")
    elif status == False:
        # If the "downloads" folder doesn't exist tell the user that the app will make a new one
        print(f"Downloads folder doesn't exist, creating a new downloads folder...")
    else:
        # If the status cannot be identified close the application
        print(f"Downloads folder status can't be identified, closing application...")
        exit = input(f"\nPress Enter to continue... ")

def downloads_directory_action(x):
    # Specify status from the given input
    status = x
    if status == True:
        # If the "downloads" directory does exist do nothing
        pass
    elif status == False:
        # If the "downloads" directory doesn't exist create one
        # Specify the path of the "downloads" directory
        directory_path = os.path.join(get_executable_directory(), "downloads")

        # Create a directory called "downloads"
        os.mkdir(directory_path)

        # Tell the user that the directory named "downloads" was created
        print(f"Done!")

def get_youtube_video_url():
    # Get the youtube video's url that the user wishes to download
    url = input(f"Please enter the youtube video's URL that you wish to download.\n>> ")
    return url

def get_download_type():
    # Get the download type of the youtube video that the user wishes to download
    while True:
        # Get the download type
        download_type = input(f"\nPlease enter the type of download of the youtube video that you wish to perform.\n-video\n-audio\n-both\n>> ")

        # Verify that the option that the user chooses is one that exists
        if download_type == "video" or download_type == "audio" or download_type == "both":
            # if it does continue
            break
        else:
            # if not, ask the user again for the download type
            print(f"\nInvalid input, please try again!\n")
    return download_type

def download_video(x, y):
    # Specify the youtube url and download type from the given input
    url = x
    type = y

    if type == "video":    
        # Specify the video based upon the url
        video = YouTube(url)

        # Get the video's title
        video_title = video.title

        # Tell the user that the video will be downloaded in the best available quality
        print(f"Downloading '{video_title}' with video format at the best available quality...")

        # Specify the best available quality
        video = video.streams.get_highest_resolution()

        # Specify the download path
        directory_path = os.path.join(get_executable_directory(), "downloads")

        # Download the video in the best available quality
        video.download(directory_path)

        # Tell the user that the process is done
        print(f"Done!")

    elif type == "audio":
        # Specify the audio based upon the url
        audio = YouTube(url)

        # Get the video's title
        audio_title = audio.title

        # Tell the user that the audio will be downloaded in the best available quality
        print(f"Downloading '{audio_title}' with audio format at the best available quality...")

        # Specify the best available quality
        audio = audio.streams.filter(only_audio=True, file_extension='mp4').first()

        # Specify the download path
        directory_path = os.path.join(get_executable_directory(), "downloads")

        # Download the audio in the best available quality
        audio.download(directory_path, audio_title + ".mp3")

        # Tell the user that the process is done
        print(f"Done!")

    elif type == "both":
        # Specify the video based upon the url
        video = YouTube(url)

        # Get the video's title
        video_title = video.title

        # Tell the user that the video will be downloaded in the best available quality
        print(f"Downloading '{video_title}' with video format at the best available quality...")

        # Specify the best available quality
        video = video.streams.get_highest_resolution()

        # Specify the download path
        directory_path = os.path.join(get_executable_directory(), "downloads")

        # Download the video in the best available quality
        video.download(directory_path)

        # Tell the user that the process is done
        print(f"Done!")

        # Specify the audio based upon the url
        audio = YouTube(url)

        # Get the video's title
        audio_title = audio.title

        # Tell the user that the audio will be downloaded in the best available quality
        print(f"\nDownloading '{audio_title}' with audio format at the best available quality...")

        # Specify the best available quality
        audio = audio.streams.filter(only_audio=True, file_extension='mp4').first()

        # Specify the download path
        directory_path = os.path.join(get_executable_directory(), "downloads")

        # Download the audio in the best available quality
        audio.download(directory_path, audio_title + ".mp3")

        # Tell the user that the process is done
        print(f"Done!")

def close_app():
    exit = input(f"\nPress Enter to continue... ")

def main():
    clear_terminal()
    does_downloads_folder_exists = check_if_downloads_directory_exists()
    tell_user_downloads_directory_status(does_downloads_folder_exists)
    downloads_directory_action(does_downloads_folder_exists)
    clear_terminal()
    youtube_video_url = get_youtube_video_url()
    youtube_video_download_type = get_download_type()
    clear_terminal()
    download_video(youtube_video_url, youtube_video_download_type)
    close_app()

if __name__ == "__main__":
    main()
