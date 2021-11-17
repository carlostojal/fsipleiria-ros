;; Auto-generated. Do not edit!


(when (boundp 'data_acquisition::geolocation)
  (if (not (find-package "DATA_ACQUISITION"))
    (make-package "DATA_ACQUISITION"))
  (shadow 'geolocation (find-package "DATA_ACQUISITION")))
(unless (find-package "DATA_ACQUISITION::GEOLOCATION")
  (make-package "DATA_ACQUISITION::GEOLOCATION"))

(in-package "ROS")
;;//! \htmlinclude geolocation.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass data_acquisition::geolocation
  :super ros::object
  :slots (_header _latitute _longitute ))

(defmethod data_acquisition::geolocation
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:latitute __latitute) 0.0)
    ((:longitute __longitute) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _latitute (float __latitute))
   (setq _longitute (float __longitute))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:latitute
   (&optional __latitute)
   (if __latitute (setq _latitute __latitute)) _latitute)
  (:longitute
   (&optional __longitute)
   (if __longitute (setq _longitute __longitute)) _longitute)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _latitute
    8
    ;; float64 _longitute
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _latitute
       (sys::poke _latitute (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitute
       (sys::poke _longitute (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _latitute
     (setq _latitute (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitute
     (setq _longitute (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get data_acquisition::geolocation :md5sum-) "68b28efb81f156a5687c93ca2b4a86b3")
(setf (get data_acquisition::geolocation :datatype-) "data_acquisition/geolocation")
(setf (get data_acquisition::geolocation :definition-)
      "Header header
float64 latitute
float64 longitute
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



(provide :data_acquisition/geolocation "68b28efb81f156a5687c93ca2b4a86b3")


