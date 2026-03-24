

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSignalRResult', 'AwaitableGetSignalRResult', 'get_signal_r', 'get_signal_r_output']
@pulumi.output_type
class GetSignalRResult:
    
    def __init__(__self__, azure_api_version=..., cors=..., disable_aad_auth=..., disable_local_auth=..., external_ip=..., features=..., host_name=..., host_name_prefix=..., id=..., identity=..., kind=..., live_trace_configuration=..., location=..., name=..., network_acls=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., public_port=..., region_endpoint_enabled=..., resource_log_configuration=..., resource_stopped=..., server_port=..., serverless=..., shared_private_link_resources=..., sku=..., system_data=..., tags=..., tls=..., type=..., upstream=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.SignalRCorsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAadAuth")
    def disable_aad_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIP")
    def external_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[Sequence[outputs.SignalRFeatureResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostNamePrefix")
    def host_name_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveTraceConfiguration")
    def live_trace_configuration(self) -> Optional[outputs.LiveTraceConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkACLs")
    def network_acls(self) -> Optional[outputs.SignalRNetworkACLsResponse]:
        
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
    @pulumi.getter(name="publicPort")
    def public_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLogConfiguration")
    def resource_log_configuration(self) -> Optional[outputs.ResourceLogConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStopped")
    def resource_stopped(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serverless(self) -> Optional[outputs.ServerlessSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(self) -> Sequence[outputs.SharedPrivateLinkResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ResourceSkuResponse]:
        
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
    @pulumi.getter
    def tls(self) -> Optional[outputs.SignalRTlsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def upstream(self) -> Optional[outputs.ServerlessUpstreamSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSignalRResult(GetSignalRResult):
    def __await__(self): # -> Generator[Never, Any, GetSignalRResult]:
        ...
    


def get_signal_r(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSignalRResult:
    
    ...

def get_signal_r_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSignalRResult]:
    
    ...

