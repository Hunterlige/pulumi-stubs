

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseArgs', 'Database']
@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], access_keys_authentication: Optional[pulumi.Input[Union[_builtins.str, AccessKeysAuthentication]]] = ..., client_protocol: Optional[pulumi.Input[Union[_builtins.str, Protocol]]] = ..., clustering_policy: Optional[pulumi.Input[Union[_builtins.str, ClusteringPolicy]]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., defer_upgrade: Optional[pulumi.Input[Union[_builtins.str, DeferUpgradeSetting]]] = ..., eviction_policy: Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]] = ..., geo_replication: Optional[pulumi.Input[DatabasePropertiesGeoReplicationArgs]] = ..., modules: Optional[pulumi.Input[Sequence[pulumi.Input[ModuleArgs]]]] = ..., persistence: Optional[pulumi.Input[PersistenceArgs]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeysAuthentication")
    def access_keys_authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AccessKeysAuthentication]]]:
        
        ...
    
    @access_keys_authentication.setter
    def access_keys_authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AccessKeysAuthentication]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientProtocol")
    def client_protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, Protocol]]]:
        
        ...
    
    @client_protocol.setter
    def client_protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, Protocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusteringPolicy")
    def clustering_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, ClusteringPolicy]]]:
        
        ...
    
    @clustering_policy.setter
    def clustering_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, ClusteringPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferUpgrade")
    def defer_upgrade(self) -> Optional[pulumi.Input[Union[_builtins.str, DeferUpgradeSetting]]]:
        
        ...
    
    @defer_upgrade.setter
    def defer_upgrade(self, value: Optional[pulumi.Input[Union[_builtins.str, DeferUpgradeSetting]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]]:
        
        ...
    
    @eviction_policy.setter
    def eviction_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoReplication")
    def geo_replication(self) -> Optional[pulumi.Input[DatabasePropertiesGeoReplicationArgs]]:
        
        ...
    
    @geo_replication.setter
    def geo_replication(self, value: Optional[pulumi.Input[DatabasePropertiesGeoReplicationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def modules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ModuleArgs]]]]:
        
        ...
    
    @modules.setter
    def modules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ModuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def persistence(self) -> Optional[pulumi.Input[PersistenceArgs]]:
        
        ...
    
    @persistence.setter
    def persistence(self, value: Optional[pulumi.Input[PersistenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:redisenterprise:Database")
class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_keys_authentication: Optional[pulumi.Input[Union[_builtins.str, AccessKeysAuthentication]]] = ..., client_protocol: Optional[pulumi.Input[Union[_builtins.str, Protocol]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., clustering_policy: Optional[pulumi.Input[Union[_builtins.str, ClusteringPolicy]]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., defer_upgrade: Optional[pulumi.Input[Union[_builtins.str, DeferUpgradeSetting]]] = ..., eviction_policy: Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]] = ..., geo_replication: Optional[pulumi.Input[Union[DatabasePropertiesGeoReplicationArgs, DatabasePropertiesGeoReplicationArgsDict]]] = ..., modules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ModuleArgs, ModuleArgsDict]]]]] = ..., persistence: Optional[pulumi.Input[Union[PersistenceArgs, PersistenceArgsDict]]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Database:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeysAuthentication")
    def access_keys_authentication(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientProtocol")
    def client_protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusteringPolicy")
    def clustering_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferUpgrade")
    def defer_upgrade(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoReplication")
    def geo_replication(self) -> pulumi.Output[Optional[outputs.DatabasePropertiesResponseGeoReplication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def modules(self) -> pulumi.Output[Optional[Sequence[outputs.ModuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def persistence(self) -> pulumi.Output[Optional[outputs.PersistenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


