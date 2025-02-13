
While True:
    print("Youtube Manager | Choose an option :")
    print("1. List all of your youtube videos.")
    print("2. Add a youtube video.")
    print("3. Update a youtube video details.")
    print("4. Delete a youtube video.")
    print("5. exit the app.")
    choice = input("Enter your choice:")

    match choice:
        case 1:
            list_videos(video)