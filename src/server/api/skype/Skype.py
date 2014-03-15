#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def get_chats(self, auth):
    """
    Parameters:
     - auth
    """
    pass

  def get_chat(self, auth, name):
    """
    Parameters:
     - auth
     - name
    """
    pass

  def get_user(self, auth, handle):
    """
    Parameters:
     - auth
     - handle
    """
    pass

  def send_message(self, auth, chatName, messageBody):
    """
    Parameters:
     - auth
     - chatName
     - messageBody
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def get_chats(self, auth):
    """
    Parameters:
     - auth
    """
    self.send_get_chats(auth)
    return self.recv_get_chats()

  def send_get_chats(self, auth):
    self._oprot.writeMessageBegin('get_chats', TMessageType.CALL, self._seqid)
    args = get_chats_args()
    args.auth = auth
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_chats(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_chats_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ae is not None:
      raise result.ae
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_chats failed: unknown result");

  def get_chat(self, auth, name):
    """
    Parameters:
     - auth
     - name
    """
    self.send_get_chat(auth, name)
    return self.recv_get_chat()

  def send_get_chat(self, auth, name):
    self._oprot.writeMessageBegin('get_chat', TMessageType.CALL, self._seqid)
    args = get_chat_args()
    args.auth = auth
    args.name = name
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_chat(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_chat_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ae is not None:
      raise result.ae
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_chat failed: unknown result");

  def get_user(self, auth, handle):
    """
    Parameters:
     - auth
     - handle
    """
    self.send_get_user(auth, handle)
    return self.recv_get_user()

  def send_get_user(self, auth, handle):
    self._oprot.writeMessageBegin('get_user', TMessageType.CALL, self._seqid)
    args = get_user_args()
    args.auth = auth
    args.handle = handle
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_user(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_user_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ae is not None:
      raise result.ae
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_user failed: unknown result");

  def send_message(self, auth, chatName, messageBody):
    """
    Parameters:
     - auth
     - chatName
     - messageBody
    """
    self.send_send_message(auth, chatName, messageBody)
    return self.recv_send_message()

  def send_send_message(self, auth, chatName, messageBody):
    self._oprot.writeMessageBegin('send_message', TMessageType.CALL, self._seqid)
    args = send_message_args()
    args.auth = auth
    args.chatName = chatName
    args.messageBody = messageBody
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_send_message(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = send_message_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ae is not None:
      raise result.ae
    raise TApplicationException(TApplicationException.MISSING_RESULT, "send_message failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["get_chats"] = Processor.process_get_chats
    self._processMap["get_chat"] = Processor.process_get_chat
    self._processMap["get_user"] = Processor.process_get_user
    self._processMap["send_message"] = Processor.process_send_message

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_get_chats(self, seqid, iprot, oprot):
    args = get_chats_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_chats_result()
    try:
      result.success = self._handler.get_chats(args.auth)
    except AuthenticationException, ae:
      result.ae = ae
    oprot.writeMessageBegin("get_chats", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_get_chat(self, seqid, iprot, oprot):
    args = get_chat_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_chat_result()
    try:
      result.success = self._handler.get_chat(args.auth, args.name)
    except AuthenticationException, ae:
      result.ae = ae
    oprot.writeMessageBegin("get_chat", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_get_user(self, seqid, iprot, oprot):
    args = get_user_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_user_result()
    try:
      result.success = self._handler.get_user(args.auth, args.handle)
    except AuthenticationException, ae:
      result.ae = ae
    oprot.writeMessageBegin("get_user", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_send_message(self, seqid, iprot, oprot):
    args = send_message_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = send_message_result()
    try:
      result.success = self._handler.send_message(args.auth, args.chatName, args.messageBody)
    except AuthenticationException, ae:
      result.ae = ae
    oprot.writeMessageBegin("send_message", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class get_chats_args:
  """
  Attributes:
   - auth
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (Authentication, Authentication.thrift_spec), None, ), # 1
  )

  def __init__(self, auth=None,):
    self.auth = auth

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = Authentication()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_chats_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.auth is None:
      raise TProtocol.TProtocolException(message='Required field auth is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_chats_result:
  """
  Attributes:
   - success
   - ae
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Chat, Chat.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'ae', (AuthenticationException, AuthenticationException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ae=None,):
    self.success = success
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype38, _size35) = iprot.readListBegin()
          for _i39 in xrange(_size35):
            _elem40 = Chat()
            _elem40.read(iprot)
            self.success.append(_elem40)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ae = AuthenticationException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_chats_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter41 in self.success:
        iter41.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_chat_args:
  """
  Attributes:
   - auth
   - name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (Authentication, Authentication.thrift_spec), None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
  )

  def __init__(self, auth=None, name=None,):
    self.auth = auth
    self.name = name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = Authentication()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_chat_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.auth is None:
      raise TProtocol.TProtocolException(message='Required field auth is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_chat_result:
  """
  Attributes:
   - success
   - ae
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Chat, Chat.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'ae', (AuthenticationException, AuthenticationException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ae=None,):
    self.success = success
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Chat()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ae = AuthenticationException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_chat_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_user_args:
  """
  Attributes:
   - auth
   - handle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (Authentication, Authentication.thrift_spec), None, ), # 1
    (2, TType.STRING, 'handle', None, None, ), # 2
  )

  def __init__(self, auth=None, handle=None,):
    self.auth = auth
    self.handle = handle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = Authentication()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.handle = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_user_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    if self.handle is not None:
      oprot.writeFieldBegin('handle', TType.STRING, 2)
      oprot.writeString(self.handle)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.auth is None:
      raise TProtocol.TProtocolException(message='Required field auth is unset!')
    if self.handle is None:
      raise TProtocol.TProtocolException(message='Required field handle is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_user_result:
  """
  Attributes:
   - success
   - ae
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (User, User.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'ae', (AuthenticationException, AuthenticationException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ae=None,):
    self.success = success
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = User()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ae = AuthenticationException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_user_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class send_message_args:
  """
  Attributes:
   - auth
   - chatName
   - messageBody
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (Authentication, Authentication.thrift_spec), None, ), # 1
    (2, TType.STRING, 'chatName', None, None, ), # 2
    (3, TType.STRING, 'messageBody', None, None, ), # 3
  )

  def __init__(self, auth=None, chatName=None, messageBody=None,):
    self.auth = auth
    self.chatName = chatName
    self.messageBody = messageBody

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = Authentication()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.chatName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.messageBody = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('send_message_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    if self.chatName is not None:
      oprot.writeFieldBegin('chatName', TType.STRING, 2)
      oprot.writeString(self.chatName)
      oprot.writeFieldEnd()
    if self.messageBody is not None:
      oprot.writeFieldBegin('messageBody', TType.STRING, 3)
      oprot.writeString(self.messageBody)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.auth is None:
      raise TProtocol.TProtocolException(message='Required field auth is unset!')
    if self.chatName is None:
      raise TProtocol.TProtocolException(message='Required field chatName is unset!')
    if self.messageBody is None:
      raise TProtocol.TProtocolException(message='Required field messageBody is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class send_message_result:
  """
  Attributes:
   - success
   - ae
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Message, Message.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'ae', (AuthenticationException, AuthenticationException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ae=None,):
    self.success = success
    self.ae = ae

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Message()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ae = AuthenticationException()
          self.ae.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('send_message_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.ae is not None:
      oprot.writeFieldBegin('ae', TType.STRUCT, 1)
      self.ae.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
