import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResponseHeadersPolicyResult",
    "AwaitableGetResponseHeadersPolicyResult",
    "get_response_headers_policy",
    "get_response_headers_policy_output",
]

@pulumi.output_type
class GetResponseHeadersPolicyResult:
    def __init__(
        __self__,
        arn=...,
        comment=...,
        cors_configs=...,
        custom_headers_configs=...,
        etag=...,
        id=...,
        name=...,
        remove_headers_configs=...,
        security_headers_configs=...,
        server_timing_headers_configs=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="corsConfigs")
    def cors_configs(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyCorsConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="customHeadersConfigs")
    def custom_headers_configs(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyCustomHeadersConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="removeHeadersConfigs")
    def remove_headers_configs(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyRemoveHeadersConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="securityHeadersConfigs")
    def security_headers_configs(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicySecurityHeadersConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="serverTimingHeadersConfigs")
    def server_timing_headers_configs(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyServerTimingHeadersConfigResult]: ...

class AwaitableGetResponseHeadersPolicyResult(GetResponseHeadersPolicyResult):
    def __await__(self): ...

def get_response_headers_policy(
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResponseHeadersPolicyResult: ...
def get_response_headers_policy_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResponseHeadersPolicyResult]: ...
