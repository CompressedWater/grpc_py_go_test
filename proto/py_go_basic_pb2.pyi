from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name", "cur_date")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUR_DATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    cur_date: str
    def __init__(self, name: _Optional[str] = ..., cur_date: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message", "cur_date")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CUR_DATE_FIELD_NUMBER: _ClassVar[int]
    message: str
    cur_date: str
    def __init__(self, message: _Optional[str] = ..., cur_date: _Optional[str] = ...) -> None: ...
