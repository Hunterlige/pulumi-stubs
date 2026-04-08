import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ARecordArgs",
    "ARecordArgsDict",
    "AaaaRecordArgs",
    "AaaaRecordArgsDict",
    "CnameRecordArgs",
    "CnameRecordArgsDict",
    "MxRecordArgs",
    "MxRecordArgsDict",
    "PtrRecordArgs",
    "PtrRecordArgsDict",
    "SoaRecordArgs",
    "SoaRecordArgsDict",
    "SrvRecordArgs",
    "SrvRecordArgsDict",
    "SubResourceArgs",
    "SubResourceArgsDict",
    "TxtRecordArgs",
    "TxtRecordArgsDict",
]

class ARecordArgsDict(TypedDict):
    ipv4_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ARecordArgs:
    def __init__(
        __self__, *, ipv4_address: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AaaaRecordArgsDict(TypedDict):
    ipv6_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AaaaRecordArgs:
    def __init__(
        __self__, *, ipv6_address: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CnameRecordArgsDict(TypedDict):
    cname: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CnameRecordArgs:
    def __init__(
        __self__, *, cname: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cname.setter
    def cname(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MxRecordArgsDict(TypedDict):
    exchange: NotRequired[pulumi.Input[_builtins.str]]
    preference: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MxRecordArgs:
    def __init__(
        __self__,
        *,
        exchange: Optional[pulumi.Input[_builtins.str]] = ...,
        preference: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exchange.setter
    def exchange(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @preference.setter
    def preference(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PtrRecordArgsDict(TypedDict):
    ptrdname: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PtrRecordArgs:
    def __init__(
        __self__, *, ptrdname: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ptrdname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ptrdname.setter
    def ptrdname(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SoaRecordArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    expire_time: NotRequired[pulumi.Input[_builtins.float]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    minimum_ttl: NotRequired[pulumi.Input[_builtins.float]]
    refresh_time: NotRequired[pulumi.Input[_builtins.float]]
    retry_time: NotRequired[pulumi.Input[_builtins.float]]
    serial_number: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class SoaRecordArgs:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.float]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_ttl: Optional[pulumi.Input[_builtins.float]] = ...,
        refresh_time: Optional[pulumi.Input[_builtins.float]] = ...,
        retry_time: Optional[pulumi.Input[_builtins.float]] = ...,
        serial_number: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @minimum_ttl.setter
    def minimum_ttl(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshTime")
    def refresh_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @refresh_time.setter
    def refresh_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="retryTime")
    def retry_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @retry_time.setter
    def retry_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class SrvRecordArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SrvRecordArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SubResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubResourceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TxtRecordArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TxtRecordArgs:
    def __init__(
        __self__,
        *,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @value.setter
    def value(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
