import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFactoryDataPlaneAccessResult",
    "AwaitableGetFactoryDataPlaneAccessResult",
    "get_factory_data_plane_access",
    "get_factory_data_plane_access_output",
]

@pulumi.output_type
class GetFactoryDataPlaneAccessResult:
    def __init__(
        __self__, access_token=..., data_plane_url=..., policy=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneUrl")
    def data_plane_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[outputs.UserAccessPolicyResponse]: ...

class AwaitableGetFactoryDataPlaneAccessResult(GetFactoryDataPlaneAccessResult):
    def __await__(self): ...

def get_factory_data_plane_access(
    access_resource_path: Optional[_builtins.str] = ...,
    expire_time: Optional[_builtins.str] = ...,
    factory_name: Optional[_builtins.str] = ...,
    permissions: Optional[_builtins.str] = ...,
    profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    start_time: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFactoryDataPlaneAccessResult: ...
def get_factory_data_plane_access_output(
    access_resource_path: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    expire_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    permissions: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    profile_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    start_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFactoryDataPlaneAccessResult]: ...
