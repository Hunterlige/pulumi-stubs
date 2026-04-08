import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAutoScaleVCoreResult",
    "AwaitableGetAutoScaleVCoreResult",
    "get_auto_scale_v_core",
    "get_auto_scale_v_core_output",
]

@pulumi.output_type
class GetAutoScaleVCoreResult:
    def __init__(
        __self__,
        azure_api_version=...,
        capacity_limit=...,
        capacity_object_id=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        sku=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityLimit")
    def capacity_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="capacityObjectId")
    def capacity_object_id(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.AutoScaleVCoreSkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAutoScaleVCoreResult(GetAutoScaleVCoreResult):
    def __await__(self): ...

def get_auto_scale_v_core(
    resource_group_name: Optional[_builtins.str] = ...,
    vcore_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAutoScaleVCoreResult: ...
def get_auto_scale_v_core_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vcore_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAutoScaleVCoreResult]: ...
