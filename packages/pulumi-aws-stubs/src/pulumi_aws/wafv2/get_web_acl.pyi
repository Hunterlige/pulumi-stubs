import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAclResult",
    "AwaitableGetWebAclResult",
    "get_web_acl",
    "get_web_acl_output",
]

@pulumi.output_type
class GetWebAclResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        id=...,
        name=...,
        region=...,
        resource_arn=...,
        scope=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

class AwaitableGetWebAclResult(GetWebAclResult):
    def __await__(self): ...

def get_web_acl(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    resource_arn: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAclResult: ...
def get_web_acl_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAclResult]: ...
