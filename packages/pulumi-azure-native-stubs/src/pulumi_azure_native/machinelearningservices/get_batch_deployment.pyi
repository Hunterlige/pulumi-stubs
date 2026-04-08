import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBatchDeploymentResult",
    "AwaitableGetBatchDeploymentResult",
    "get_batch_deployment",
    "get_batch_deployment_output",
]

@pulumi.output_type
class GetBatchDeploymentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        identity=...,
        kind=...,
        location=...,
        name=...,
        properties=...,
        sku=...,
        system_data=...,
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
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.BatchDeploymentPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBatchDeploymentResult(GetBatchDeploymentResult):
    def __await__(self): ...

def get_batch_deployment(
    deployment_name: Optional[_builtins.str] = ...,
    endpoint_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBatchDeploymentResult: ...
def get_batch_deployment_output(
    deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBatchDeploymentResult]: ...
