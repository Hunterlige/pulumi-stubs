

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ARecordArgs', 'ARecordArgsDict', 'AaaaRecordArgs', 'AaaaRecordArgsDict', 'CaaRecordArgs', 'CaaRecordArgsDict', 'CnameRecordArgs', 'CnameRecordArgsDict', 'DigestArgs', 'DigestArgsDict', 'DsRecordArgs', 'DsRecordArgsDict', 'MxRecordArgs', 'MxRecordArgsDict', 'NaptrRecordArgs', 'NaptrRecordArgsDict', 'NsRecordArgs', 'NsRecordArgsDict', 'PtrRecordArgs', 'PtrRecordArgsDict', 'SoaRecordArgs', 'SoaRecordArgsDict', 'SrvRecordArgs', 'SrvRecordArgsDict', 'SubResource', 'SubResourceDict', 'SubResourceArgs', 'SubResourceArgsDict', 'TlsaRecordArgs', 'TlsaRecordArgsDict', 'TxtRecordArgs', 'TxtRecordArgsDict']
class ARecordArgsDict(TypedDict):
    
    ipv4_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ARecordArgs:
    def __init__(__self__, *, ipv4_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AaaaRecordArgsDict(TypedDict):
    
    ipv6_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AaaaRecordArgs:
    def __init__(__self__, *, ipv6_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CaaRecordArgsDict(TypedDict):
    
    flags: NotRequired[pulumi.Input[_builtins.int]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CaaRecordArgs:
    def __init__(__self__, *, flags: Optional[pulumi.Input[_builtins.int]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @flags.setter
    def flags(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CnameRecordArgsDict(TypedDict):
    
    cname: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CnameRecordArgs:
    def __init__(__self__, *, cname: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cname.setter
    def cname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DigestArgsDict(TypedDict):
    
    algorithm_type: NotRequired[pulumi.Input[_builtins.int]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DigestArgs:
    def __init__(__self__, *, algorithm_type: Optional[pulumi.Input[_builtins.int]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="algorithmType")
    def algorithm_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @algorithm_type.setter
    def algorithm_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DsRecordArgsDict(TypedDict):
    
    algorithm: NotRequired[pulumi.Input[_builtins.int]]
    digest: NotRequired[pulumi.Input[DigestArgsDict]]
    key_tag: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DsRecordArgs:
    def __init__(__self__, *, algorithm: Optional[pulumi.Input[_builtins.int]] = ..., digest: Optional[pulumi.Input[DigestArgs]] = ..., key_tag: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[DigestArgs]]:
        
        ...
    
    @digest.setter
    def digest(self, value: Optional[pulumi.Input[DigestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_tag.setter
    def key_tag(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MxRecordArgsDict(TypedDict):
    
    exchange: NotRequired[pulumi.Input[_builtins.str]]
    preference: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MxRecordArgs:
    def __init__(__self__, *, exchange: Optional[pulumi.Input[_builtins.str]] = ..., preference: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exchange.setter
    def exchange(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @preference.setter
    def preference(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NaptrRecordArgsDict(TypedDict):
    
    flags: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    preference: NotRequired[pulumi.Input[_builtins.int]]
    regexp: NotRequired[pulumi.Input[_builtins.str]]
    replacement: NotRequired[pulumi.Input[_builtins.str]]
    services: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NaptrRecordArgs:
    def __init__(__self__, *, flags: Optional[pulumi.Input[_builtins.str]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., preference: Optional[pulumi.Input[_builtins.int]] = ..., regexp: Optional[pulumi.Input[_builtins.str]] = ..., replacement: Optional[pulumi.Input[_builtins.str]] = ..., services: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @flags.setter
    def flags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @preference.setter
    def preference(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regexp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @regexp.setter
    def regexp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replacement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replacement.setter
    def replacement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @services.setter
    def services(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NsRecordArgsDict(TypedDict):
    
    nsdname: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NsRecordArgs:
    def __init__(__self__, *, nsdname: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nsdname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nsdname.setter
    def nsdname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PtrRecordArgsDict(TypedDict):
    
    ptrdname: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PtrRecordArgs:
    def __init__(__self__, *, ptrdname: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ptrdname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ptrdname.setter
    def ptrdname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


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
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.float]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., minimum_ttl: Optional[pulumi.Input[_builtins.float]] = ..., refresh_time: Optional[pulumi.Input[_builtins.float]] = ..., retry_time: Optional[pulumi.Input[_builtins.float]] = ..., serial_number: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @minimum_ttl.setter
    def minimum_ttl(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTime")
    def refresh_time(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @refresh_time.setter
    def refresh_time(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryTime")
    def retry_time(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @retry_time.setter
    def retry_time(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SrvRecordArgsDict(TypedDict):
    
    port: NotRequired[pulumi.Input[_builtins.int]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SrvRecordArgs:
    def __init__(__self__, *, port: Optional[pulumi.Input[_builtins.int]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SubResourceDict(TypedDict):
    
    id: NotRequired[_builtins.str]


@pulumi.input_type
class SubResource:
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[_builtins.str]): # -> None:
        ...
    


class SubResourceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TlsaRecordArgsDict(TypedDict):
    
    cert_association_data: NotRequired[pulumi.Input[_builtins.str]]
    matching_type: NotRequired[pulumi.Input[_builtins.int]]
    selector: NotRequired[pulumi.Input[_builtins.int]]
    usage: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TlsaRecordArgs:
    def __init__(__self__, *, cert_association_data: Optional[pulumi.Input[_builtins.str]] = ..., matching_type: Optional[pulumi.Input[_builtins.int]] = ..., selector: Optional[pulumi.Input[_builtins.int]] = ..., usage: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certAssociationData")
    def cert_association_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cert_association_data.setter
    def cert_association_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @matching_type.setter
    def matching_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def usage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @usage.setter
    def usage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TxtRecordArgsDict(TypedDict):
    
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TxtRecordArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


