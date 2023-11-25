from plyer import notification
from databases.db_connector import SQLiteConnector

class Notification:
    def show_notification(self,category):
        try:
            db_connector = SQLiteConnector("KeyHub.db")
            table_name = "CustomizeKeys"
            data = db_connector.fetch_data(f"SELECT description,shortcut_key FROM {table_name} where category='{category}';")
            if data:

                message = "\n".join(str(record) for record in data)
                notification.notify(
                    title=f"All {category} Customize ShortCut-Key",
                    message=message,
                    timeout=10
                )
            else:
                notification.notify(
                    title=f"All {category} Customize ShortCut-Key",
                    message="No Shortcut Key Customized yet",
                    timeout=10
                )
        finally:
            if db_connector:    db_connector.close_connection()
