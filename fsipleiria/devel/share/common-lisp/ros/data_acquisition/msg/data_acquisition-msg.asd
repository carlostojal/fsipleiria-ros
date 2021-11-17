
(cl:in-package :asdf)

(defsystem "data_acquisition-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Geolocation" :depends-on ("_package_Geolocation"))
    (:file "_package_Geolocation" :depends-on ("_package"))
  ))