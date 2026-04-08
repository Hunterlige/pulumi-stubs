import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDeploymentAtManagementGroupScopeResult",
    "AwaitableGetDeploymentAtManagementGroupScopeResult",
    "get_deployment_at_management_group_scope",
    "get_deployment_at_management_group_scope_output",
]

@pulumi.output_type
class GetDeploymentAtManagementGroupScopeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.DeploymentPropertiesExtendedResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDeploymentAtManagementGroupScopeResult(
    GetDeploymentAtManagementGroupScopeResult
):
    def __await__(self): ...

def get_deployment_at_management_group_scope(
    deployment_name: Optional[_builtins.str] = ...,
    group_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDeploymentAtManagementGroupScopeResult: ...
def get_deployment_at_management_group_scope_output(
    deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDeploymentAtManagementGroupScopeResult]: ...
