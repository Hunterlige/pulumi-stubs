import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetPoolResult", "AwaitableGetPoolResult", "get_pool", "get_pool_output"]

@pulumi.output_type
class GetPoolResult:
    def __init__(
        __self__,
        assignments=...,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        pool_type=...,
        provisioning_state=...,
        reclaim_policy=...,
        resources=...,
        status=...,
        system_data=...,
        tags=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assignments(self) -> Optional[Sequence[outputs.AssignmentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> outputs.PoolTypeResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.ResourcesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.ResourceOperationalStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetPoolResult(GetPoolResult):
    def __await__(self): ...

def get_pool(
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPoolResult: ...
def get_pool_output(
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPoolResult]: ...
