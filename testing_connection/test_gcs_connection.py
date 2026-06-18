from google.cloud import storage

keyfile_path = r"C:\Users\uwicl\Documents\04_ Documents 2026\04_Free nternship\Healthcare project\healthcare-data-project-499612-9deb30aec329.json"

client = storage.Client.from_service_account_json(keyfile_path)

print("Connected successfully!")

for bucket in client.list_buckets():
    print(bucket.name)