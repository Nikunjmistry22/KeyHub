import logging
from databases.db_connector import SQLiteConnector
import subprocess
import keyboard
from notification import Notification

logging.basicConfig(filename='keyhub.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

db_connector = SQLiteConnector("KeyHub.db")
table_name = "CustomizeKeys"
query = f"SELECT * FROM {table_name} WHERE category in ('Chrome','Folder','File','Window','Default Keys');"


def open_chrome_with_urls(key_combination, urls):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    url_list = urls.split(',')

    subprocess.run([chrome_path, "--new-window", url_list[0].strip()])

    for url in url_list[1:]:
        subprocess.run([chrome_path, "--new-tab", url.strip()])

    logging.info(f"Opening Chrome with URLs using hotkey: {key_combination}")


def open_folder(key_combination, folder_path):
    subprocess.run(["start", " ", folder_path], shell=True)
    logging.info(f"Opening Folder's {folder_path} using hotkey: {key_combination}")


def open_file(key_combination, file_path):
    file_path = file_path.split(',')
    for file in file_path:
        subprocess.run(["start", " ", file], shell=True)

    logging.info(f"Opening File's {file_path} using hotkey: {key_combination}")


def open_window(key_combination, window_path):
    subprocess.Popen([window_path])
    logging.info(f"Opening Folder's {window_path} using hotkey: {key_combination}")


def register_hotkeys():
    try:
        notification = Notification()
        results = db_connector.fetch_data(query)
        keyboard.add_hotkey('Shift+C', notification.show_notification, args=('Chrome',))
        keyboard.add_hotkey('Shift+M', notification.show_notification, args=('File',))
        keyboard.add_hotkey('Shift+F', notification.show_notification, args=('Folder',))
        keyboard.add_hotkey('Shift+W', notification.show_notification, args=('Window',))

        if results:
            for result in results:
                key_combination = result[4]
                if result[2] == 'Chrome':
                    keyboard.add_hotkey(key_combination, open_chrome_with_urls, args=(key_combination, result[3]))
                elif result[2] == 'Folder':
                    keyboard.add_hotkey(key_combination, open_folder, args=(key_combination, result[3]))
                elif result[2] == 'File':
                    keyboard.add_hotkey(key_combination, open_file, args=(key_combination, result[3]))
                elif result[2] == 'Window':
                    keyboard.add_hotkey(key_combination, open_window, args=(key_combination, result[3]))
    except Exception as e:
        pass


register_hotkeys()

try:
    keyboard.wait('esc')
except KeyboardInterrupt:
    logging.info("KeyInterrupted")
finally:
    db_connector.close_connection()
