import subprocess

# Defining local file paths and hdfs directory
local_files = [
    "data/checkin_checkout_history_updated.csv",
    "data/gym_locations_data.csv",
    "data/subscription_plans.csv",
    "data/users_data.csv"
]

hdfs_dir = "/gym_data"

# Create HDFS directory
subprocess.run(["hdfs", "dfs", "-mkdir", "-p", hdfs_dir])

# Upload files to HDFS
for file in local_files:
    subprocess.run(["hdfs", "dfs", "-put", file, hdfs_dir])
    print(f"Uploaded {file} to HDFS at {hdfs_dir}")
