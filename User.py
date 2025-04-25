#python class to extract the mongo db locally and write the data csv format before deployment to aws

from pymongo import MongoClient
import csv

class UserDetailCSV:
    def __init__(self, db_name, collection_name, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_user_data(self):
        data = list(self.collection.find())
        for doc in data:
            doc.pop('_id', None)
        return data

    def export_to_csv(self, file_name="user_data.csv"):
        data = self.fetch_user_data()
        if data:

            fieldnames = data[0].keys()

            with open(file_name, mode="w", newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            print(f"Data exported to '{file_name}' successfully.")
        else:
            print("No data found to export.")

# Example usage
if __name__ == "__main__":
    exporter = UserDetailCSV("user_database", "users")
    exporter.export_to_csv("users_output.csv")