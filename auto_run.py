import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    # on_created() - called when a file is created
    def on_created(self, event):
        # checking if the created event is a directory
        if event.is_directory:
            return
        # Getting the path of newly added file
        new_file_path = event.src_path
        # Runnig the Python script with the newly added file's path as an argument
        subprocess.run(["python", "chatgpt_automation.py", new_file_path])

def monitor_folder(folder_path):
    # Creating an object of the MyHandler class
    event_handler = MyHandler()
    # Creating an Observer to watch for file system events
    observer = Observer()
    # Setting up the observer to use the event handler for the specified folder
    observer.schedule(event_handler, path=folder_path, recursive=False)
    # Starting the observer
    observer.start()
    try:
        # Keeping the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stopping the observer when the script is interrupted
        observer.stop()
    # Wait for the observer to finish
    observer.join()

if __name__ == "__main__":
    # Folder path to monitor
    folder_to_monitor = "/Users/anirudhnuti/Documents/Architecting_With_Google_Kubernetes_Engine/Google_Cloud_Fundamentals_Core_Infrastructure/Transcripts"
    # Monitoring the folder
    monitor_folder(folder_to_monitor)
