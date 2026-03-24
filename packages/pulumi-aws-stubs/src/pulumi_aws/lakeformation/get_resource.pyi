import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResourceResult",
    "AwaitableGetResourceResult",
    "get_resource",
    "get_resource_output",
]

@pulumi.output_type
class GetResourceResult:
    def __init__(
        __self__,
        arn=...,
        hybrid_access_enabled=...,
        id=...,
        last_modified=...,
        region=...,
        role_arn=...,
        with_federation=...,
        with_privileged_access=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hybridAccessEnabled")
    def hybrid_access_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="withFederation")
    def with_federation(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="withPrivilegedAccess")
    def with_privileged_access(self) -> _builtins.bool: ...

class AwaitableGetResourceResult(GetResourceResult):
    def __await__(self): ...

def get_resource(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResourceResult: ...
def get_resource_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResourceResult]: ...
