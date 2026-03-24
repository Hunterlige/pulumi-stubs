import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionSslCertificateResult",
    "AwaitableGetRegionSslCertificateResult",
    "get_region_ssl_certificate",
    "get_region_ssl_certificate_output",
]

@pulumi.output_type
class GetRegionSslCertificateResult:
    def __init__(
        __self__,
        certificate=...,
        certificate_id=...,
        creation_timestamp=...,
        description=...,
        expire_time=...,
        id=...,
        name=...,
        name_prefix=...,
        private_key=...,
        private_key_wo=...,
        private_key_wo_version=...,
        project=...,
        region=...,
        self_link=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKeyWo")
    def private_key_wo(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKeyWoVersion")
    def private_key_wo_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...

class AwaitableGetRegionSslCertificateResult(GetRegionSslCertificateResult):
    def __await__(self): ...

def get_region_ssl_certificate(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionSslCertificateResult: ...
def get_region_ssl_certificate_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionSslCertificateResult]: ...
