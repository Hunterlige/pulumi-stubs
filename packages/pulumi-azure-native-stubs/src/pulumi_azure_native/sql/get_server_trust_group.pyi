import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerTrustGroupResult",
    "AwaitableGetServerTrustGroupResult",
    "get_server_trust_group",
    "get_server_trust_group_output",
]

@pulumi.output_type
class GetServerTrustGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        group_members=...,
        id=...,
        name=...,
        trust_scopes=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupMembers")
    def group_members(self) -> Sequence[outputs.ServerInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trustScopes")
    def trust_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerTrustGroupResult(GetServerTrustGroupResult):
    def __await__(self): ...

def get_server_trust_group(
    location_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_trust_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerTrustGroupResult: ...
def get_server_trust_group_output(
    location_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_trust_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerTrustGroupResult]: ...
