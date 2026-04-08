import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ARecordResponse",
    "AaaaRecordResponse",
    "CaaRecordResponse",
    "CnameRecordResponse",
    "DelegationSignerInfoResponse",
    "DigestResponse",
    "DnsResourceReferenceResponse",
    "DsRecordResponse",
    "MxRecordResponse",
    "NaptrRecordResponse",
    "NsRecordResponse",
    "PtrRecordResponse",
    "SigningKeyResponse",
    "SoaRecordResponse",
    "SrvRecordResponse",
    "SubResourceResponse",
    "SystemDataResponse",
    "TlsaRecordResponse",
    "TxtRecordResponse",
]

@pulumi.output_type
class ARecordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ipv4_address: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AaaaRecordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ipv6_address: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaaRecordResponse(dict):
    def __init__(
        __self__,
        *,
        flags: Optional[_builtins.int] = ...,
        tag: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CnameRecordResponse(dict):
    def __init__(__self__, *, cname: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DelegationSignerInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        digest_algorithm_type: _builtins.int,
        digest_value: _builtins.str,
        record: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="digestAlgorithmType")
    def digest_algorithm_type(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="digestValue")
    def digest_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def record(self) -> _builtins.str: ...

@pulumi.output_type
class DigestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm_type: Optional[_builtins.int] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="algorithmType")
    def algorithm_type(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DnsResourceReferenceResponse(dict):
    def __init__(
        __self__,
        *,
        dns_resources: Optional[Sequence[outputs.SubResourceResponse]] = ...,
        target_resource: Optional[outputs.SubResourceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsResources")
    def dns_resources(self) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> Optional[outputs.SubResourceResponse]: ...

@pulumi.output_type
class DsRecordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: Optional[_builtins.int] = ...,
        digest: Optional[outputs.DigestResponse] = ...,
        key_tag: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[outputs.DigestResponse]: ...
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MxRecordResponse(dict):
    def __init__(
        __self__,
        *,
        exchange: Optional[_builtins.str] = ...,
        preference: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NaptrRecordResponse(dict):
    def __init__(
        __self__,
        *,
        flags: Optional[_builtins.str] = ...,
        order: Optional[_builtins.int] = ...,
        preference: Optional[_builtins.int] = ...,
        regexp: Optional[_builtins.str] = ...,
        replacement: Optional[_builtins.str] = ...,
        services: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def regexp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def replacement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NsRecordResponse(dict):
    def __init__(__self__, *, nsdname: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def nsdname(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PtrRecordResponse(dict):
    def __init__(__self__, *, ptrdname: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ptrdname(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SigningKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delegation_signer_info: Sequence[outputs.DelegationSignerInfoResponse],
        flags: _builtins.int,
        key_tag: _builtins.int,
        protocol: _builtins.int,
        public_key: _builtins.str,
        security_algorithm_type: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delegationSignerInfo")
    def delegation_signer_info(
        self,
    ) -> Sequence[outputs.DelegationSignerInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityAlgorithmType")
    def security_algorithm_type(self) -> _builtins.int: ...

@pulumi.output_type
class SoaRecordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email: Optional[_builtins.str] = ...,
        expire_time: Optional[_builtins.float] = ...,
        host: Optional[_builtins.str] = ...,
        minimum_ttl: Optional[_builtins.float] = ...,
        refresh_time: Optional[_builtins.float] = ...,
        retry_time: Optional[_builtins.float] = ...,
        serial_number: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="refreshTime")
    def refresh_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="retryTime")
    def retry_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class SrvRecordResponse(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        priority: Optional[_builtins.int] = ...,
        target: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SubResourceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TlsaRecordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_association_data: Optional[_builtins.str] = ...,
        matching_type: Optional[_builtins.int] = ...,
        selector: Optional[_builtins.int] = ...,
        usage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certAssociationData")
    def cert_association_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def usage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TxtRecordResponse(dict):
    def __init__(
        __self__, *, value: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]: ...
