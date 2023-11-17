# Raspberry Pi Camera Detect Objects and Upload Results

Periodically detect objects in Raspberry Pi camera image and upload JSON results to Firebase Firestore.
  
### Use Cases
- check parking lot occupancy and update Firestore for Firebase website to show parking availability
- notify when people are detected
- count cars or people over time with Firestore timeseries queries


### Usage

```sh
libcamera-still -r -t 1 -o input/picture.jpg
python detect.py -i input/picture.jpg -m yolov8n.pt -o output/results.json -oi output/results.jpg
python firestoreupload.py --credentials=credentials.json --file=output/results.json --collection=DetectedObjects
```

### Dependencies

- Raspberry Pi, Camera, Distro: Bullseye 11
- https://github.com/ultralytics/ultralytics

### Update Raspberry Pi and Install Dependencies

```sh
ssh $USER@pi.local

sudo apt -y update
sudo apt -y full-upgrade

# "detect.py" dependencies
sudo apt -y install python3-pip
sudo pip install ultralytics
# for ImportError: libGL.so.1: cannot open shared object file: No such file or directory:
sudo pip install opencv-python-headless
# debian requires sep build for libcamera-apps https://www.raspberrypi.com/documentation/computers/camera_software.html#building-libcamera-apps

# "firestoreupload.py" dependencies
pip install firebase-admin

# add samba share (optional) 
sudo apt -y install samba samba-common-bin
sudo mkdir -m 1777 /shared
sudo cat <<EOF >> /etc/samba/smb.conf
[pishare]
path = /shared
writeable = yes
browseable = yes
create mask = 0777
directory mask = 0777
public = no
EOF
sudo smbpasswd -a $USER
# windows: \\PI\pishare
```

### Check Install

```sh
python -c "from ultralytics import YOLO; print(YOLO('yolov8m.pt'))"
python -c "import cv2; print(cv2.__version__)"
```

### Todo

- add cronjob or loop to periodically update
- add web example