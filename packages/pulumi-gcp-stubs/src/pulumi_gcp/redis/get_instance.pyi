

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
    
    def __init__(__self__, alternative_location_id=..., auth_enabled=..., auth_string=..., authorized_network=..., connect_mode=..., create_time=..., current_location_id=..., customer_managed_key=..., deletion_protection=..., display_name=..., effective_labels=..., effective_reserved_ip_range=..., host=..., id=..., labels=..., location_id=..., maintenance_policies=..., maintenance_schedules=..., maintenance_version=..., memory_size_gb=..., name=..., nodes=..., persistence_configs=..., persistence_iam_identity=..., port=..., project=..., pulumi_labels=..., read_endpoint=..., read_endpoint_port=..., read_replicas_mode=..., redis_configs=..., redis_version=..., region=..., replica_count=..., reserved_ip_range=..., secondary_ip_range=..., server_ca_certs=..., tier=..., transit_encryption_mode=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeLocationId")
    def alternative_location_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authString")
    def auth_string(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentLocationId")
    def current_location_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveReservedIpRange")
    def effective_reserved_ip_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence[outputs.GetInstanceMaintenancePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Sequence[outputs.GetInstanceMaintenanceScheduleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.GetInstanceNodeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfigs")
    def persistence_configs(self) -> Sequence[outputs.GetInstancePersistenceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceIamIdentity")
    def persistence_iam_identity(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
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
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readEndpointPort")
    def read_endpoint_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readReplicasMode")
    def read_replicas_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpRange")
    def secondary_ip_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> Sequence[outputs.GetInstanceServerCaCertResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceResult]:
        ...
    


def get_instance(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceResult:
    
    ...

def get_instance_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceResult]:
    
    ...

