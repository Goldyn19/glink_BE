import os

# Loop to create folders
for i in range(1, 61):
    folder_name = f"C:/Users/Golden/Videos/enjoy life {i}"
    os.makedirs(folder_name, exist_ok=True)

print("Folders created successfully!")