import os
# pip install pytube
from pytube import YouTube

def clear_terminal():
    # Clear terminal
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def check_if_downloads_directory_exists():
    # Tell the user what is happening
    print(f"Chechking if downloads folder exists...")

    # Specify the path of the "downloads" dirctory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory_name = "downloads"
    directory_path = os.path.join(current_directory, directory_name)

    # Check if the "downlaods" directory exists
    exists = os.path.exists(directory_path)

    # Tell the user that the folder check has been done
    print(f"Done!")
    return exists

def tell_user_downloads_directory_status(x):
    # Specify status from the given input
    status = x

    # Check the status's value
    if status == True:
        # If the "downlaods" folder exists tell the user that the app will continne like normal
        print(f"Downloads folder exists, continuing like normal!")
    elif status == False:
        # If the "downloads" folder doesen't exists tell the user that the app will make a new one
        print(f"Downloads folder doesen't exist, creating a new downloads folder...")
    else:
        # If the status cannot be identified close the application
        print(f"Downloads folder status can't be identified, closing application...")
        exit = input(f"\nPress Enter to continue... ")

def downloads_directory_action(x):
    # Specify status from the given input
    status = x
    if status == True:
        # If the "downlaods" directory does exist do nothing
        pass
    elif status == False:
        # If the "downloads" directory doesen't exist create one
        # Specify the path of the "downloads" dirctory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        directory_name = "downloads"
        directory_path = os.path.join(current_directory, directory_name)

        # Create a directory called "downloads"
        os.mkdir(directory_path)

        # Tell the user that the direcotry named "downloads" was created
        print(f"Done!")

def get_youtube_video_url():
    # Get the youtube video's url that the user wishes to download
    url = input(f"Please enter the youtube video's URL that you wish to download.\n>> ")
    return url

def get_download_type():
    # Get the download type of the youtube video that the user wishes to download
    while True:
        # Get the downlaod type
        download_type = input(f"\nPlease enter the type of download of the youtube video that you wish to preform.\n-video\n-audio\n-both\n>> ")

        # Verify that the option that the user choose is one that exists
        if download_type == "video" or download_type == "audio" or download_type == "both":
            # if it does continne
            break
        else:
            # if not, ask the user again for the downlaod type
            print(f"\nnvalid input, please try again!\n")
    return download_type

def download_video(x,y):
    # Specify the youtube url and download type from the given input
    url = x
    type = y

    if type == "video":    
        # Specify the video based upon the url
        video = YouTube(url)

        # Get the video's title
        video_title = video.title

        # Tell the user that the video will be downloaded in the best avalible quality
        print(f"Downlaoding '{video_title}' with video format at the best avalible quality...")

        # Specify the best avalible quality
        video = video.streams.get_highest_resolution()

        # Specify the download path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        download_directory_name = "downloads"
        download_directory_path = os.path.join(current_directory, download_directory_name)

        # Download the video in the best avalible quality
        video.download(download_directory_path)

        # Tell the user that the procces is done
        print(f"Done!")

    elif type == "audio":
        # Specify the audio based upon the url
        audio = YouTube(url)

        # Get the video's title
        audio_title = audio.title

        # Tell the user that the audio will be downloaded in the best avalible quality
        print(f"Downlaoding '{audio_title}' with audio format at the best avalible quality...")

        # Specify the best avalible quality
        audio = audio.streams.filter(only_audio=True, file_extension='mp4').first()

        # Specify the download path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        download_directory_name = "downloads"
        download_directory_path = os.path.join(current_directory, download_directory_name)

        # Download the audio in the best avalible quality
        audio.download(download_directory_path, audio_title + ".mp3")

        # Tell the user that the procces is done
        print(f"Done!")

    elif type == "both":
        # Specify the video based upon the url
        video = YouTube(url)

        # Get the video's title
        video_title = video.title

        # Tell the user that the video will be downloaded in the best avalible quality
        print(f"Downlaoding '{video_title}' with video format at the best avalible quality...")

        # Specify the best avalible quality
        video = video.streams.get_highest_resolution()

        # Specify the download path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        download_directory_name = "downloads"
        download_directory_path = os.path.join(current_directory, download_directory_name)

        # Download the video in the best avalible quality
        video.download(download_directory_path)

        # Tell the user that the procces is done
        print(f"Done!")

        # Specify the audio based upon the url
        audio = YouTube(url)

        # Get the video's title
        audio_title = audio.title

        # Tell the user that the audio will be downloaded in the best avalible quality
        print(f"\nDownlaoding '{audio_title}' with audio format at the best avalible quality...")

        # Specify the best avalible quality
        audio = audio.streams.filter(only_audio=True, file_extension='mp4').first()

        # Specify the download path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        download_directory_name = "downloads"
        download_directory_path = os.path.join(current_directory, download_directory_name)

        # Download the audio in the best avalible quality
        audio.download(download_directory_path, audio_title + ".mp3")

        # Tell the user that the procces is done
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
    download_video(youtube_video_url,youtube_video_download_type)
    close_app()
    

if __name__ == "__main__":
    main()
