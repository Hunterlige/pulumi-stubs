import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInvocationResult",
    "AwaitableGetInvocationResult",
    "get_invocation",
    "get_invocation_output",
]

@pulumi.output_type
class GetInvocationResult:
    def __init__(
        __self__,
        function_name=...,
        id=...,
        input=...,
        qualifier=...,
        region=...,
        result=...,
        tenant_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

class AwaitableGetInvocationResult(GetInvocationResult):
    def __await__(self): ...

def get_invocation(
    function_name: Optional[_builtins.str] = ...,
    input: Optional[_builtins.str] = ...,
    qualifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tenant_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInvocationResult: ...
def get_invocation_output(
    function_name: Optional[pulumi.Input[_builtins.str]] = ...,
    input: Optional[pulumi.Input[_builtins.str]] = ...,
    qualifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tenant_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInvocationResult]: ...
