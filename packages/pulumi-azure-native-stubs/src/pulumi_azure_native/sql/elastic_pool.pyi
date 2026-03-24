

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ElasticPoolArgs', 'ElasticPool']
@pulumi.input_type
class ElasticPoolArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], auto_pause_delay: Optional[pulumi.Input[_builtins.int]] = ..., availability_zone: Optional[pulumi.Input[Union[_builtins.str, AvailabilityZoneType]]] = ..., elastic_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., high_availability_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., license_type: Optional[pulumi.Input[Union[_builtins.str, ElasticPoolLicenseType]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., max_size_bytes: Optional[pulumi.Input[_builtins.float]] = ..., min_capacity: Optional[pulumi.Input[_builtins.float]] = ..., per_database_settings: Optional[pulumi.Input[ElasticPoolPerDatabaseSettingsArgs]] = ..., preferred_enclave_type: Optional[pulumi.Input[Union[_builtins.str, AlwaysEncryptedEnclaveType]]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPauseDelay")
    def auto_pause_delay(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @auto_pause_delay.setter
    def auto_pause_delay(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[Union[_builtins.str, AvailabilityZoneType]]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[Union[_builtins.str, AvailabilityZoneType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticPoolName")
    def elastic_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_pool_name.setter
    def elastic_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="highAvailabilityReplicaCount")
    def high_availability_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @high_availability_replica_count.setter
    def high_availability_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticPoolLicenseType]]]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticPoolLicenseType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_configuration_id.setter
    def maintenance_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_size_bytes.setter
    def max_size_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perDatabaseSettings")
    def per_database_settings(self) -> Optional[pulumi.Input[ElasticPoolPerDatabaseSettingsArgs]]:
        
        ...
    
    @per_database_settings.setter
    def per_database_settings(self, value: Optional[pulumi.Input[ElasticPoolPerDatabaseSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredEnclaveType")
    def preferred_enclave_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AlwaysEncryptedEnclaveType]]]:
        
        ...
    
    @preferred_enclave_type.setter
    def preferred_enclave_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AlwaysEncryptedEnclaveType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:ElasticPool")
class ElasticPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_pause_delay: Optional[pulumi.Input[_builtins.int]] = ..., availability_zone: Optional[pulumi.Input[Union[_builtins.str, AvailabilityZoneType]]] = ..., elastic_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., high_availability_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., license_type: Optional[pulumi.Input[Union[_builtins.str, ElasticPoolLicenseType]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., max_size_bytes: Optional[pulumi.Input[_builtins.float]] = ..., min_capacity: Optional[pulumi.Input[_builtins.float]] = ..., per_database_settings: Optional[pulumi.Input[Union[ElasticPoolPerDatabaseSettingsArgs, ElasticPoolPerDatabaseSettingsArgsDict]]] = ..., preferred_enclave_type: Optional[pulumi.Input[Union[_builtins.str, AlwaysEncryptedEnclaveType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ElasticPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ElasticPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPauseDelay")
    def auto_pause_delay(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="highAvailabilityReplicaCount")
    def high_availability_replica_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perDatabaseSettings")
    def per_database_settings(self) -> pulumi.Output[Optional[outputs.ElasticPoolPerDatabaseSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredEnclaveType")
    def preferred_enclave_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


