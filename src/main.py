import youtube_dl.ydl as ydl


def main():
    url = input("Enter url: ")
    output_path = input("Enter output path (default = ~/Downloads): ")
    filename = input("Enter filename (default = video): ")

    if url == "":
        return print("No url entered!")

    if output_path == "" and filename == "":
        return print(f"{ydl.download(url)}")

    if output_path == "":
        return print(f"{ydl.download(url, filename=filename)}")
    
    if filename == "":
        return print(f"{ydl.download(url, output_path=output_path)}")
    
    return print(f"{ydl.download(url, output_path, filename)}")


if __name__ == "__main__":
    main()
