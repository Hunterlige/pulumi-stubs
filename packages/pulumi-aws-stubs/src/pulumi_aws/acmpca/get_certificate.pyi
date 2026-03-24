import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCertificateResult",
    "AwaitableGetCertificateResult",
    "get_certificate",
    "get_certificate_output",
]

@pulumi.output_type
class GetCertificateResult:
    def __init__(
        __self__,
        arn=...,
        certificate=...,
        certificate_authority_arn=...,
        certificate_chain=...,
        id=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetCertificateResult(GetCertificateResult):
    def __await__(self): ...

def get_certificate(
    arn: Optional[_builtins.str] = ...,
    certificate_authority_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCertificateResult: ...
def get_certificate_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCertificateResult]: ...
