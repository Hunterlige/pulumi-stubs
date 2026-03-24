import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityProfileResult",
    "AwaitableGetSecurityProfileResult",
    "get_security_profile",
    "get_security_profile_output",
]

@pulumi.output_type
class GetSecurityProfileResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        id=...,
        instance_id=...,
        name=...,
        organization_resource_id=...,
        permissions=...,
        region=...,
        security_profile_id=...,
        tags=...,
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
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationResourceId")
    def organization_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityProfileId")
    def security_profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetSecurityProfileResult(GetSecurityProfileResult):
    def __await__(self): ...

def get_security_profile(
    instance_id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    security_profile_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityProfileResult: ...
def get_security_profile_output(
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    security_profile_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityProfileResult]: ...
