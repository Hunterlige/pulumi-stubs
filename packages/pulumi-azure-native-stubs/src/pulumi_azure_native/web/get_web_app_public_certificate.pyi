import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppPublicCertificateResult",
    "AwaitableGetWebAppPublicCertificateResult",
    "get_web_app_public_certificate",
    "get_web_app_public_certificate_output",
]

@pulumi.output_type
class GetWebAppPublicCertificateResult:
    def __init__(
        __self__,
        azure_api_version=...,
        blob=...,
        id=...,
        kind=...,
        name=...,
        public_certificate_location=...,
        thumbprint=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def blob(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicCertificateLocation")
    def public_certificate_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAppPublicCertificateResult(GetWebAppPublicCertificateResult):
    def __await__(self): ...

def get_web_app_public_certificate(
    name: Optional[_builtins.str] = ...,
    public_certificate_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppPublicCertificateResult: ...
def get_web_app_public_certificate_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    public_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppPublicCertificateResult]: ...
