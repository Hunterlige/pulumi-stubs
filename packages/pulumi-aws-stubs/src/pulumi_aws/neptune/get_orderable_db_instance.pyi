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
        max_iops_per_db_instance=...,
        max_iops_per_gib=...,
        max_storage_size=...,
        min_iops_per_db_instance=...,
        min_iops_per_gib=...,
        min_storage_size=...,
        multi_az_capable=...,
        preferred_instance_classes=...,
        read_replica_capable=...,
        region=...,
        storage_type=...,
        supports_enhanced_monitoring=...,
        supports_iam_database_authentication=...,
        supports_iops=...,
        supports_performance_insights=...,
        supports_storage_encryption=...,
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
    @pulumi.getter(name="maxIopsPerDbInstance")
    def max_iops_per_db_instance(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxIopsPerGib")
    def max_iops_per_gib(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="maxStorageSize")
    def max_storage_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minIopsPerDbInstance")
    def min_iops_per_db_instance(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minIopsPerGib")
    def min_iops_per_gib(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="minStorageSize")
    def min_storage_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="multiAzCapable")
    def multi_az_capable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="preferredInstanceClasses")
    def preferred_instance_classes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="readReplicaCapable")
    def read_replica_capable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportsEnhancedMonitoring")
    def supports_enhanced_monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="supportsIamDatabaseAuthentication")
    def supports_iam_database_authentication(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="supportsIops")
    def supports_iops(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="supportsPerformanceInsights")
    def supports_performance_insights(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="supportsStorageEncryption")
    def supports_storage_encryption(self) -> _builtins.bool: ...
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
