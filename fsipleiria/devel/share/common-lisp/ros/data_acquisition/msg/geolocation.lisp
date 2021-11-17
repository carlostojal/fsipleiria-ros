; Auto-generated. Do not edit!


(cl:in-package data_acquisition-msg)


;//! \htmlinclude geolocation.msg.html

(cl:defclass <geolocation> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (latitute
    :reader latitute
    :initarg :latitute
    :type cl:float
    :initform 0.0)
   (longitute
    :reader longitute
    :initarg :longitute
    :type cl:float
    :initform 0.0))
)

(cl:defclass geolocation (<geolocation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <geolocation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'geolocation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name data_acquisition-msg:<geolocation> is deprecated: use data_acquisition-msg:geolocation instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <geolocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader data_acquisition-msg:header-val is deprecated.  Use data_acquisition-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'latitute-val :lambda-list '(m))
(cl:defmethod latitute-val ((m <geolocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader data_acquisition-msg:latitute-val is deprecated.  Use data_acquisition-msg:latitute instead.")
  (latitute m))

(cl:ensure-generic-function 'longitute-val :lambda-list '(m))
(cl:defmethod longitute-val ((m <geolocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader data_acquisition-msg:longitute-val is deprecated.  Use data_acquisition-msg:longitute instead.")
  (longitute m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <geolocation>) ostream)
  "Serializes a message object of type '<geolocation>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'latitute))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'longitute))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <geolocation>) istream)
  "Deserializes a message object of type '<geolocation>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitute) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitute) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<geolocation>)))
  "Returns string type for a message object of type '<geolocation>"
  "data_acquisition/geolocation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'geolocation)))
  "Returns string type for a message object of type 'geolocation"
  "data_acquisition/geolocation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<geolocation>)))
  "Returns md5sum for a message object of type '<geolocation>"
  "68b28efb81f156a5687c93ca2b4a86b3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'geolocation)))
  "Returns md5sum for a message object of type 'geolocation"
  "68b28efb81f156a5687c93ca2b4a86b3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<geolocation>)))
  "Returns full string definition for message of type '<geolocation>"
  (cl:format cl:nil "Header header~%float64 latitute~%float64 longitute~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'geolocation)))
  "Returns full string definition for message of type 'geolocation"
  (cl:format cl:nil "Header header~%float64 latitute~%float64 longitute~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <geolocation>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <geolocation>))
  "Converts a ROS message object to a list"
  (cl:list 'geolocation
    (cl:cons ':header (header msg))
    (cl:cons ':latitute (latitute msg))
    (cl:cons ':longitute (longitute msg))
))
