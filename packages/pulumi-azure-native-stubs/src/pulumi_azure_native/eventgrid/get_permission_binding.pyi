import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPermissionBindingResult",
    "AwaitableGetPermissionBindingResult",
    "get_permission_binding",
    "get_permission_binding_output",
]

@pulumi.output_type
class GetPermissionBindingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        client_group_name=...,
        description=...,
        id=...,
        name=...,
        permission=...,
        provisioning_state=...,
        system_data=...,
        topic_space_name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientGroupName")
    def client_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="topicSpaceName")
    def topic_space_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPermissionBindingResult(GetPermissionBindingResult):
    def __await__(self): ...

def get_permission_binding(
    namespace_name: Optional[_builtins.str] = ...,
    permission_binding_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPermissionBindingResult: ...
def get_permission_binding_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    permission_binding_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPermissionBindingResult]: ...
