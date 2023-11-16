def get_status_download(status, total):
    percent = int((status / total) * 10)
    download = ""
    if percent in range(1, 11):
        download = "#" * percent

    return f"{download}   {percent * 10}%"


print(get_status_download(int(input()), int(input())))
