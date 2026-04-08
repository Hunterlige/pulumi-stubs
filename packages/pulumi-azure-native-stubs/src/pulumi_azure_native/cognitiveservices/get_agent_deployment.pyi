import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAgentDeploymentResult",
    "AwaitableGetAgentDeploymentResult",
    "get_agent_deployment",
    "get_agent_deployment_output",
]

@pulumi.output_type
class GetAgentDeploymentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
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
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAgentDeploymentResult(GetAgentDeploymentResult):
    def __await__(self): ...

def get_agent_deployment(
    account_name: Optional[_builtins.str] = ...,
    app_name: Optional[_builtins.str] = ...,
    deployment_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAgentDeploymentResult: ...
def get_agent_deployment_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    app_name: Optional[pulumi.Input[_builtins.str]] = ...,
    deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAgentDeploymentResult]: ...
