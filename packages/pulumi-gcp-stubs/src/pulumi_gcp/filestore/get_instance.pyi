

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceResult', 'AwaitableGetInstanceResult', 'get_instance', 'get_instance_output']
@pulumi.output_type
class GetInstanceResult:
    
    def __init__(__self__, create_time=..., deletion_protection_enabled=..., deletion_protection_reason=..., description=..., desired_replica_state=..., directory_services=..., effective_labels=..., effective_replications=..., etag=..., file_shares=..., id=..., initial_replications=..., kms_key_name=..., labels=..., location=..., name=..., networks=..., performance_configs=..., project=..., protocol=..., pulumi_labels=..., tags=..., tier=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionReason")
    def deletion_protection_reason(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredReplicaState")
    def desired_replica_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServices")
    def directory_services(self) -> Sequence[outputs.GetInstanceDirectoryServiceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveReplications")
    def effective_replications(self) -> Sequence[outputs.GetInstanceEffectiveReplicationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> Sequence[outputs.GetInstanceFileShareResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplications")
    def initial_replications(self) -> Sequence[outputs.GetInstanceInitialReplicationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Sequence[outputs.GetInstanceNetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfigs")
    def performance_configs(self) -> Sequence[outputs.GetInstancePerformanceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceResult]:
        ...
    


def get_instance(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceResult:
    
    ...

def get_instance_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceResult]:
    
    ...

