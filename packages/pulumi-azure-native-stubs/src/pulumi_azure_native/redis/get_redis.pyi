

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRedisResult', 'AwaitableGetRedisResult', 'get_redis', 'get_redis_output']
@pulumi.output_type
class GetRedisResult:
    
    def __init__(__self__, access_keys=..., azure_api_version=..., disable_access_key_authentication=..., enable_non_ssl_port=..., host_name=..., id=..., identity=..., instances=..., linked_servers=..., location=..., minimum_tls_version=..., name=..., port=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., redis_configuration=..., redis_version=..., replicas_per_master=..., replicas_per_primary=..., shard_count=..., sku=..., ssl_port=..., static_ip=..., subnet_id=..., system_data=..., tags=..., tenant_settings=..., type=..., update_channel=..., zonal_allocation_policy=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeys")
    def access_keys(self) -> outputs.RedisAccessKeysResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAccessKeyAuthentication")
    def disable_access_key_authentication(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNonSslPort")
    def enable_non_ssl_port(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.RedisInstanceDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedServers")
    def linked_servers(self) -> Sequence[outputs.RedisLinkedServerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfiguration")
    def redis_configuration(self) -> Optional[outputs.RedisCommonPropertiesRedisConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicasPerMaster")
    def replicas_per_master(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicasPerPrimary")
    def replicas_per_primary(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPort")
    def ssl_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIP")
    def static_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantSettings")
    def tenant_settings(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateChannel")
    def update_channel(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalAllocationPolicy")
    def zonal_allocation_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetRedisResult(GetRedisResult):
    def __await__(self): # -> Generator[Never, Any, GetRedisResult]:
        ...
    


def get_redis(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRedisResult:
    
    ...

def get_redis_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRedisResult]:
    
    ...

