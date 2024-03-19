import gi
gi.require_version('Gst','1.0')
gi.require_version('GstVideo','1.0')
gi.require_version('GstRtspServer','1.0')
from gi.repository import GObject, Gst, GstVideo, GstRtspServer

Gst.init(None)


mainloop = GObject.MainLoop()
server = GstRtspServer.RTSPServer()
mounts = server.get_mount_points()

factory = GstRtspServer.RTSPMediaFactory()
# factory.set_launch('( v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! nvvidconv ! nvv4l2h264enc insert-sps-pps=1 idrinterval=15 insert-vui=1 ! rtph264pay name=pay0 )')
# factory.set_launch('( v4l2src device=/dev/video1 ! video/x-h264, width=640, height=480, framerate=30/1, format=H264 ! nvv4l2decoder ! nvvidconv ! nvv4l2h264enc insert-sps-pps=1 idrinterval=15 insert-vui=1 ! rtph264pay name=pay0 )')

# factory.set_launch('( v4l2src device=/dev/video0 ! image/jpeg,format=MJPG,width=640,height=480,framerate=30/1 ! rtpjpegpay name=pay0 )')
# factory.set_launch('( v4l2src device=/dev/video0 io-mode=2 ! image/jpeg,width=1920,height=1080, framerate=30/1 ! nvjpegdec ! video/x-raw ! nvvidconv ! video/x-raw(memory:NVMM) ! nvv4l2h264enc  maxperf-enable=1 bitrate=2000000 iframeinterval=40 preset-level=1 control-rate=1 insert-sps-pps=1 idrinterval=30 insert-vui=1 ! rtph264pay name=pay0 pt=96 )')

factory.set_launch('( v4l2src device=/dev/video0 ! image/jpeg, width=1920, height=1080, framerate=30/1, format=MJPG ! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw(memory:NVMM) ! omxh264enc target-bitrate=3000000 control-rate=variable ! rtph264pay name=pay0 pt=96 )')
# factory.set_launch('( v4l2src device=/dev/video1 ! video/x-raw, width=640, height=480, framerate=30/1 ! nvv4l2decoder ! nvvidconv ! video/x-raw(memory:NVMM) ! omxh264enc ! rtph264pay name=pay0 pt=96 )')

# command
# gst-launch-1.0 rtspsrc location="rtsp://192.168.31.109:8554/video" latency=100 ! rtph264depay ! h264parse ! nvv4l2decoder enable-max-performance=1 ! nvoverlaysink overlay-x=800 overlay-y=50 overlay-w=640 overlay-h=480 overlay=2




mounts.add_factory("/video", factory)
server.attach(None)

print("stream ready at rtsp://127.0.0.1:8554/video")
mainloop.run()
