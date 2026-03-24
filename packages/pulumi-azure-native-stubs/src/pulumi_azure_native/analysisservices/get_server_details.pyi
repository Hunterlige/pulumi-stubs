

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerDetailsResult', 'AwaitableGetServerDetailsResult', 'get_server_details', 'get_server_details_output']
@pulumi.output_type
class GetServerDetailsResult:
    
    def __init__(__self__, as_administrators=..., azure_api_version=..., backup_blob_container_uri=..., gateway_details=..., id=..., ip_v4_firewall_settings=..., location=..., managed_mode=..., name=..., provisioning_state=..., querypool_connection_mode=..., server_full_name=..., server_monitor_mode=..., sku=..., state=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asAdministrators")
    def as_administrators(self) -> Optional[outputs.ServerAdministratorsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupBlobContainerUri")
    def backup_blob_container_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayDetails")
    def gateway_details(self) -> Optional[outputs.GatewayDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipV4FirewallSettings")
    def ip_v4_firewall_settings(self) -> Optional[outputs.IPv4FirewallSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedMode")
    def managed_mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="querypoolConnectionMode")
    def querypool_connection_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverFullName")
    def server_full_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverMonitorMode")
    def server_monitor_mode(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.ResourceSkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerDetailsResult(GetServerDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetServerDetailsResult]:
        ...
    


def get_server_details(resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerDetailsResult:
    
    ...

def get_server_details_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerDetailsResult]:
    
    ...

