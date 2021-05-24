# %%
import os

from webdav3.client import Client

options = {
 'webdav_hostname': os.getenv("DAV_HOST", "https://simpan.ugm.ac.id/remote.php/webdav"),
 'webdav_login'   : os.getenv("DAV_USER", "your username"),
 'webdav_password': os.getenv("DAV_PASSWORD", "your password")
}

client = Client(options)
# %%
# Try to upload file
remote_dir = "/example"
remote_path = "/example/a.txt"
local_path = "temp.txt"

# generate file
with open(local_path, "w") as f :
  f.writelines("Hello from local storage")

# Upload File
print("Upload File:", "\n" + "-"*10)
print("Is file exist on remote\t:", client.check(remote_path))
client.execute_request("mkdir", remote_dir) #make directory
print("Uploading...")
client.upload_file(
  local_path=local_path,
  remote_path=remote_path
)
print("Upload done.")
print("Is file exist on remote\t:", client.check(remote_path))


print()
print("Download File:", "\n" + "-"*10)
# Download file
local_download_path = "downloaded.txt"
print("Downloding...")
client.download(
  remote_path=remote_path,
  local_path=local_download_path
)
print("Download done.")

# Read downloaded file
print("Read downloaded file:")
with open(local_download_path, "r") as f:
  data = f.read()
  print(data)


print("\n Cleanup.")
# Remove file on remote
client.clean(remote_path)
client.clean(remote_dir)

# Remove generated and downloaded file
os.unlink(local_path)
os.unlink(local_download_path)

