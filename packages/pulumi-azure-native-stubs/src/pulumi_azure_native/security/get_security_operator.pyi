import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityOperatorResult",
    "AwaitableGetSecurityOperatorResult",
    "get_security_operator",
    "get_security_operator_output",
]

@pulumi.output_type
class GetSecurityOperatorResult:
    def __init__(
        __self__, azure_api_version=..., id=..., identity=..., name=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSecurityOperatorResult(GetSecurityOperatorResult):
    def __await__(self): ...

def get_security_operator(
    pricing_name: Optional[_builtins.str] = ...,
    security_operator_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityOperatorResult: ...
def get_security_operator_output(
    pricing_name: Optional[pulumi.Input[_builtins.str]] = ...,
    security_operator_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityOperatorResult]: ...
