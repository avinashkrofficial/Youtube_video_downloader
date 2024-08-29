import yt_dlp

def download_specific_format(url, save_path, format_code):
    ydl_opts = {
        'format': format_code,  # Specify the format code here
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save path and filename template
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = input(print("Enter the link of youtube"))
save_path = "C:/Users/avipa/Downloads/Telegram Desktop"
format_code = '137+140'  # Example: best video (1080p) + best audio
download_specific_format(url, save_path, format_code)


