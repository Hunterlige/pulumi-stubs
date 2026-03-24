import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrderableDbInstanceResult",
    "AwaitableGetOrderableDbInstanceResult",
    "get_orderable_db_instance",
    "get_orderable_db_instance_output",
]

@pulumi.output_type
class GetOrderableDbInstanceResult:
    def __init__(
        __self__,
        availability_zones=...,
        engine=...,
        engine_version=...,
        id=...,
        instance_class=...,
        license_model=...,
        preferred_instance_classes=...,
        region=...,
        vpc=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredInstanceClasses")
    def preferred_instance_classes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> _builtins.bool: ...

class AwaitableGetOrderableDbInstanceResult(GetOrderableDbInstanceResult):
    def __await__(self): ...

def get_orderable_db_instance(
    engine: Optional[_builtins.str] = ...,
    engine_version: Optional[_builtins.str] = ...,
    instance_class: Optional[_builtins.str] = ...,
    license_model: Optional[_builtins.str] = ...,
    preferred_instance_classes: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    vpc: Optional[_builtins.bool] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrderableDbInstanceResult: ...
def get_orderable_db_instance_output(
    engine: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    engine_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_class: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    license_model: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    preferred_instance_classes: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    vpc: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrderableDbInstanceResult]: ...
