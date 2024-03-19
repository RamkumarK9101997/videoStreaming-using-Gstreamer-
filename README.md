# videoStreaming-using-Gstreamer-
1080P video streaming archieved with delay of 150ms  

FullHD video streaming via WFI with low latency of 150ms archieved in Nvidia Jetson platforms.
change camera index in the gstream_rtsp.py file then select which streaming pipeline to suitable for you usecase then
Just Run the gstream_rtsp.py python file on the Jetson Nano or other jetson devices it, it will stream the video in local network
you can access it via rtsp url like rtsp://127.0.0.1:8554/video in vlc or Gstreamer on client side(Best result)
