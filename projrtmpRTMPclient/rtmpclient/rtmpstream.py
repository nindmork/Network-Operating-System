import subprocess
import cv2

rtmp_url = "rtmp://localhost:1935/live/cos3106"
path = "somtam.mp4"
cap = cv2.VideoCapture(path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

command = ['ffmpeg',
        '-y', 
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-re', 
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast', 
        '-f', 'flv',
         '-flvflags', 'no_duration_filesize',
        rtmp_url]
    
p = subprocess.Popen(command, stdin=subprocess.PIPE)   

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("frame read failed")
        break
    p.stdin.write(frame.tobytes())

