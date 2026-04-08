import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerTrustCertificateResult",
    "AwaitableGetServerTrustCertificateResult",
    "get_server_trust_certificate",
    "get_server_trust_certificate_output",
]

@pulumi.output_type
class GetServerTrustCertificateResult:
    def __init__(
        __self__,
        azure_api_version=...,
        certificate_name=...,
        id=...,
        name=...,
        public_blob=...,
        thumbprint=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicBlob")
    def public_blob(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerTrustCertificateResult(GetServerTrustCertificateResult):
    def __await__(self): ...

def get_server_trust_certificate(
    certificate_name: Optional[_builtins.str] = ...,
    managed_instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerTrustCertificateResult: ...
def get_server_trust_certificate_output(
    certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerTrustCertificateResult]: ...
