//
// Autogenerated by Thrift Compiler (0.9.1)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//
var Thrift = require('thrift').Thrift;

var ttypes = require('./skype_types');
//HELPER FUNCTIONS AND STRUCTURES

Skype_get_chats_args = function(args) {
  this.auth = null;
  if (args) {
    if (args.auth !== undefined) {
      this.auth = args.auth;
    }
  }
};
Skype_get_chats_args.prototype = {};
Skype_get_chats_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.auth = new ttypes.Authentication();
        this.auth.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_chats_args.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_chats_args');
  if (this.auth !== null && this.auth !== undefined) {
    output.writeFieldBegin('auth', Thrift.Type.STRUCT, 1);
    this.auth.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Skype_get_chats_result = function(args) {
  this.success = null;
  this.ae = null;
  if (args instanceof ttypes.AuthenticationException) {
    this.ae = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.ae !== undefined) {
      this.ae = args.ae;
    }
  }
};
Skype_get_chats_result.prototype = {};
Skype_get_chats_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size0 = 0;
        var _rtmp34;
        this.success = [];
        var _etype3 = 0;
        _rtmp34 = input.readListBegin();
        _etype3 = _rtmp34.etype;
        _size0 = _rtmp34.size;
        for (var _i5 = 0; _i5 < _size0; ++_i5)
        {
          var elem6 = null;
          elem6 = new ttypes.Chat();
          elem6.read(input);
          this.success.push(elem6);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.ae = new ttypes.AuthenticationException();
        this.ae.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_chats_result.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_chats_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.STRUCT, this.success.length);
    for (var iter7 in this.success)
    {
      if (this.success.hasOwnProperty(iter7))
      {
        iter7 = this.success[iter7];
        iter7.write(output);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.ae !== null && this.ae !== undefined) {
    output.writeFieldBegin('ae', Thrift.Type.STRUCT, 1);
    this.ae.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Skype_get_chat_args = function(args) {
  this.auth = null;
  this.name = null;
  if (args) {
    if (args.auth !== undefined) {
      this.auth = args.auth;
    }
    if (args.name !== undefined) {
      this.name = args.name;
    }
  }
};
Skype_get_chat_args.prototype = {};
Skype_get_chat_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.auth = new ttypes.Authentication();
        this.auth.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRING) {
        this.name = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_chat_args.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_chat_args');
  if (this.auth !== null && this.auth !== undefined) {
    output.writeFieldBegin('auth', Thrift.Type.STRUCT, 1);
    this.auth.write(output);
    output.writeFieldEnd();
  }
  if (this.name !== null && this.name !== undefined) {
    output.writeFieldBegin('name', Thrift.Type.STRING, 2);
    output.writeString(this.name);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Skype_get_chat_result = function(args) {
  this.success = null;
  this.ae = null;
  if (args instanceof ttypes.AuthenticationException) {
    this.ae = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.ae !== undefined) {
      this.ae = args.ae;
    }
  }
};
Skype_get_chat_result.prototype = {};
Skype_get_chat_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.STRUCT) {
        this.success = new ttypes.Chat();
        this.success.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.ae = new ttypes.AuthenticationException();
        this.ae.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_chat_result.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_chat_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRUCT, 0);
    this.success.write(output);
    output.writeFieldEnd();
  }
  if (this.ae !== null && this.ae !== undefined) {
    output.writeFieldBegin('ae', Thrift.Type.STRUCT, 1);
    this.ae.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Skype_get_user_args = function(args) {
  this.auth = null;
  this.handle = null;
  if (args) {
    if (args.auth !== undefined) {
      this.auth = args.auth;
    }
    if (args.handle !== undefined) {
      this.handle = args.handle;
    }
  }
};
Skype_get_user_args.prototype = {};
Skype_get_user_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.auth = new ttypes.Authentication();
        this.auth.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRING) {
        this.handle = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_user_args.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_user_args');
  if (this.auth !== null && this.auth !== undefined) {
    output.writeFieldBegin('auth', Thrift.Type.STRUCT, 1);
    this.auth.write(output);
    output.writeFieldEnd();
  }
  if (this.handle !== null && this.handle !== undefined) {
    output.writeFieldBegin('handle', Thrift.Type.STRING, 2);
    output.writeString(this.handle);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

Skype_get_user_result = function(args) {
  this.success = null;
  this.ae = null;
  if (args instanceof ttypes.AuthenticationException) {
    this.ae = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.ae !== undefined) {
      this.ae = args.ae;
    }
  }
};
Skype_get_user_result.prototype = {};
Skype_get_user_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.STRUCT) {
        this.success = new ttypes.User();
        this.success.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.ae = new ttypes.AuthenticationException();
        this.ae.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

Skype_get_user_result.prototype.write = function(output) {
  output.writeStructBegin('Skype_get_user_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRUCT, 0);
    this.success.write(output);
    output.writeFieldEnd();
  }
  if (this.ae !== null && this.ae !== undefined) {
    output.writeFieldBegin('ae', Thrift.Type.STRUCT, 1);
    this.ae.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

SkypeClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this.seqid = 0;
    this._reqs = {};
};
SkypeClient.prototype = {};
SkypeClient.prototype.get_chats = function(auth, callback) {
  this.seqid += 1;
  this._reqs[this.seqid] = callback;
  this.send_get_chats(auth);
};

SkypeClient.prototype.send_get_chats = function(auth) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('get_chats', Thrift.MessageType.CALL, this.seqid);
  var args = new Skype_get_chats_args();
  args.auth = auth;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

SkypeClient.prototype.recv_get_chats = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new Skype_get_chats_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.ae) {
    return callback(result.ae);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('get_chats failed: unknown result');
};
SkypeClient.prototype.get_chat = function(auth, name, callback) {
  this.seqid += 1;
  this._reqs[this.seqid] = callback;
  this.send_get_chat(auth, name);
};

SkypeClient.prototype.send_get_chat = function(auth, name) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('get_chat', Thrift.MessageType.CALL, this.seqid);
  var args = new Skype_get_chat_args();
  args.auth = auth;
  args.name = name;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

SkypeClient.prototype.recv_get_chat = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new Skype_get_chat_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.ae) {
    return callback(result.ae);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('get_chat failed: unknown result');
};
SkypeClient.prototype.get_user = function(auth, handle, callback) {
  this.seqid += 1;
  this._reqs[this.seqid] = callback;
  this.send_get_user(auth, handle);
};

SkypeClient.prototype.send_get_user = function(auth, handle) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('get_user', Thrift.MessageType.CALL, this.seqid);
  var args = new Skype_get_user_args();
  args.auth = auth;
  args.handle = handle;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

SkypeClient.prototype.recv_get_user = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new Skype_get_user_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.ae) {
    return callback(result.ae);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('get_user failed: unknown result');
};
SkypeProcessor = exports.Processor = function(handler) {
  this._handler = handler
}
SkypeProcessor.prototype.process = function(input, output) {
  var r = input.readMessageBegin();
  if (this['process_' + r.fname]) {
    return this['process_' + r.fname].call(this, r.rseqid, input, output);
  } else {
    input.skip(Thrift.Type.STRUCT);
    input.readMessageEnd();
    var x = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN_METHOD, 'Unknown function ' + r.fname);
    output.writeMessageBegin(r.fname, Thrift.MessageType.Exception, r.rseqid);
    x.write(output);
    output.writeMessageEnd();
    output.flush();
  }
}

SkypeProcessor.prototype.process_get_chats = function(seqid, input, output) {
  var args = new Skype_get_chats_args();
  args.read(input);
  input.readMessageEnd();
  this._handler.get_chats(args.auth, function (err, result) {
    var result = new Skype_get_chats_result((err != null ? err : {success: result}));
    output.writeMessageBegin("get_chats", Thrift.MessageType.REPLY, seqid);
    result.write(output);
    output.writeMessageEnd();
    output.flush();
  })
}

SkypeProcessor.prototype.process_get_chat = function(seqid, input, output) {
  var args = new Skype_get_chat_args();
  args.read(input);
  input.readMessageEnd();
  this._handler.get_chat(args.auth, args.name, function (err, result) {
    var result = new Skype_get_chat_result((err != null ? err : {success: result}));
    output.writeMessageBegin("get_chat", Thrift.MessageType.REPLY, seqid);
    result.write(output);
    output.writeMessageEnd();
    output.flush();
  })
}

SkypeProcessor.prototype.process_get_user = function(seqid, input, output) {
  var args = new Skype_get_user_args();
  args.read(input);
  input.readMessageEnd();
  this._handler.get_user(args.auth, args.handle, function (err, result) {
    var result = new Skype_get_user_result((err != null ? err : {success: result}));
    output.writeMessageBegin("get_user", Thrift.MessageType.REPLY, seqid);
    result.write(output);
    output.writeMessageEnd();
    output.flush();
  })
}

