;; Auto-generated. Do not edit!


(when (boundp 'data_acquisition::Geolocation)
  (if (not (find-package "DATA_ACQUISITION"))
    (make-package "DATA_ACQUISITION"))
  (shadow 'Geolocation (find-package "DATA_ACQUISITION")))
(unless (find-package "DATA_ACQUISITION::GEOLOCATION")
  (make-package "DATA_ACQUISITION::GEOLOCATION"))

(in-package "ROS")
;;//! \htmlinclude Geolocation.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass data_acquisition::Geolocation
  :super ros::object
  :slots (_header _latitude _longitude ))

(defmethod data_acquisition::Geolocation
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get data_acquisition::Geolocation :md5sum-) "e383d714141551d92fd5b87614818b1c")
(setf (get data_acquisition::Geolocation :datatype-) "data_acquisition/Geolocation")
(setf (get data_acquisition::Geolocation :definition-)
      "Header header
float64 latitude
float64 longitude
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :data_acquisition/Geolocation "e383d714141551d92fd5b87614818b1c")


