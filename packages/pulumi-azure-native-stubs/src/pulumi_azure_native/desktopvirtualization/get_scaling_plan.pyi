import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScalingPlanResult",
    "AwaitableGetScalingPlanResult",
    "get_scaling_plan",
    "get_scaling_plan_output",
]

@pulumi.output_type
class GetScalingPlanResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        etag=...,
        exclusion_tag=...,
        friendly_name=...,
        host_pool_references=...,
        host_pool_type=...,
        id=...,
        identity=...,
        kind=...,
        location=...,
        managed_by=...,
        name=...,
        object_id=...,
        plan=...,
        schedules=...,
        sku=...,
        system_data=...,
        tags=...,
        time_zone=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(
        self,
    ) -> Optional[Sequence[outputs.ScalingHostPoolReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponseIdentity]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plan(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponsePlan]: ...
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence[outputs.ScalingScheduleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponseSku]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetScalingPlanResult(GetScalingPlanResult):
    def __await__(self): ...

def get_scaling_plan(
    resource_group_name: Optional[_builtins.str] = ...,
    scaling_plan_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScalingPlanResult: ...
def get_scaling_plan_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scaling_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScalingPlanResult]: ...
