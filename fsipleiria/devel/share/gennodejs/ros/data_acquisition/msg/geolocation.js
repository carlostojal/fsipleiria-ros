// Auto-generated. Do not edit!

// (in-package data_acquisition.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class geolocation {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.latitute = null;
      this.longitute = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('latitute')) {
        this.latitute = initObj.latitute
      }
      else {
        this.latitute = 0.0;
      }
      if (initObj.hasOwnProperty('longitute')) {
        this.longitute = initObj.longitute
      }
      else {
        this.longitute = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type geolocation
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [latitute]
    bufferOffset = _serializer.float64(obj.latitute, buffer, bufferOffset);
    // Serialize message field [longitute]
    bufferOffset = _serializer.float64(obj.longitute, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type geolocation
    let len;
    let data = new geolocation(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [latitute]
    data.latitute = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [longitute]
    data.longitute = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'data_acquisition/geolocation';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '68b28efb81f156a5687c93ca2b4a86b3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new geolocation(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.latitute !== undefined) {
      resolved.latitute = msg.latitute;
    }
    else {
      resolved.latitute = 0.0
    }

    if (msg.longitute !== undefined) {
      resolved.longitute = msg.longitute;
    }
    else {
      resolved.longitute = 0.0
    }

    return resolved;
    }
};

module.exports = geolocation;
