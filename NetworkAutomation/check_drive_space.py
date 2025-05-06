import shutil

# Set a threshold in GB
THRESHOLD_GB = 60

def check_c_drive_space():
    total, used, free = shutil.disk_usage("C:\\")
    free_gb = free // (2**30)

    print("Disk usage for C:\\ drive:")
    print(f"  Total: {total // (2**30)} GB")
    print(f"  Used:  {used // (2**30)} GB")
    print(f"  Free:  {free_gb} GB")

    if free_gb < THRESHOLD_GB:
        print("WARNING: Free disk space on C: drive is below threshold!")
        # Optional: Add code here to send an email, write to a log file, or pop up a message box

if __name__ == "__main__":
    check_c_drive_space()
