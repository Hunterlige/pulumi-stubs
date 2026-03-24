

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStoragePoolResult', 'AwaitableGetStoragePoolResult', 'get_storage_pool', 'get_storage_pool_output']
@pulumi.output_type
class GetStoragePoolResult:
    
    def __init__(__self__, capacity_provisioning_type=..., creation_timestamp=..., deletion_protection=..., description=..., effective_labels=..., id=..., kind=..., label_fingerprint=..., labels=..., name=..., performance_provisioning_type=..., pool_provisioned_capacity_gb=..., pool_provisioned_iops=..., pool_provisioned_throughput=..., project=..., pulumi_labels=..., resource_statuses=..., statuses=..., storage_pool_type=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvisioningType")
    def capacity_provisioning_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceProvisioningType")
    def performance_provisioning_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolProvisionedCapacityGb")
    def pool_provisioned_capacity_gb(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolProvisionedIops")
    def pool_provisioned_iops(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolProvisionedThroughput")
    def pool_provisioned_throughput(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> Sequence[outputs.GetStoragePoolResourceStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.GetStoragePoolStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePoolType")
    def storage_pool_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetStoragePoolResult(GetStoragePoolResult):
    def __await__(self): # -> Generator[Never, Any, GetStoragePoolResult]:
        ...
    


def get_storage_pool(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStoragePoolResult:
    
    ...

def get_storage_pool_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStoragePoolResult]:
    
    ...

