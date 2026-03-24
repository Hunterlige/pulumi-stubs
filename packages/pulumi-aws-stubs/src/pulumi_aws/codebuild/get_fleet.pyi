import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetFleetResult", "AwaitableGetFleetResult", "get_fleet", "get_fleet_output"]

@pulumi.output_type
class GetFleetResult:
    def __init__(
        __self__,
        arn=...,
        base_capacity=...,
        compute_configurations=...,
        compute_type=...,
        created=...,
        environment_type=...,
        fleet_service_role=...,
        id=...,
        image_id=...,
        last_modified=...,
        name=...,
        overflow_behavior=...,
        region=...,
        scaling_configurations=...,
        statuses=...,
        tags=...,
        vpc_configs=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="computeConfigurations")
    def compute_configurations(
        self,
    ) -> Sequence[outputs.GetFleetComputeConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fleetServiceRole")
    def fleet_service_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overflowBehavior")
    def overflow_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scalingConfigurations")
    def scaling_configurations(
        self,
    ) -> Sequence[outputs.GetFleetScalingConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.GetFleetStatusResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> Sequence[outputs.GetFleetVpcConfigResult]: ...

class AwaitableGetFleetResult(GetFleetResult):
    def __await__(self): ...

def get_fleet(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFleetResult: ...
def get_fleet_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFleetResult]: ...
