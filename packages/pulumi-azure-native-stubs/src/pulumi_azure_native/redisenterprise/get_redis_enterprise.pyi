import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRedisEnterpriseResult",
    "AwaitableGetRedisEnterpriseResult",
    "get_redis_enterprise",
    "get_redis_enterprise_output",
]

@pulumi.output_type
class GetRedisEnterpriseResult:
    def __init__(
        __self__,
        azure_api_version=...,
        encryption=...,
        high_availability=...,
        host_name=...,
        id=...,
        identity=...,
        kind=...,
        location=...,
        minimum_tls_version=...,
        name=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        redis_version=...,
        redundancy_mode=...,
        resource_state=...,
        sku=...,
        tags=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.ClusterPropertiesResponseEncryption]: ...
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redundancyMode")
    def redundancy_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetRedisEnterpriseResult(GetRedisEnterpriseResult):
    def __await__(self): ...

def get_redis_enterprise(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRedisEnterpriseResult: ...
def get_redis_enterprise_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRedisEnterpriseResult]: ...
