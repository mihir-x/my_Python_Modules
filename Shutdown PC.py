import os, platform

time = input("Shutdown after how many seconds ")
os.system(f"shutdown /s /t {time}")
print('Windows is shutting down after {time} seconds')
