

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceResult', 'AwaitableGetWorkspaceResult', 'get_workspace', 'get_workspace_output']
@pulumi.output_type
class GetWorkspaceResult:
    
    def __init__(__self__, adla_resource_id=..., azure_api_version=..., connectivity_endpoints=..., csp_workspace_admin_properties=..., default_data_lake_storage=..., encryption=..., extra_properties=..., id=..., identity=..., location=..., managed_resource_group_name=..., managed_virtual_network=..., managed_virtual_network_settings=..., name=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., purview_configuration=..., settings=..., sql_administrator_login=..., sql_administrator_login_password=..., tags=..., trusted_service_bypass_enabled=..., type=..., virtual_network_profile=..., workspace_repository_configuration=..., workspace_uid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adlaResourceId")
    def adla_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityEndpoints")
    def connectivity_endpoints(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cspWorkspaceAdminProperties")
    def csp_workspace_admin_properties(self) -> Optional[outputs.CspWorkspaceAdminPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStorage")
    def default_data_lake_storage(self) -> Optional[outputs.DataLakeStorageAccountDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraProperties")
    def extra_properties(self) -> Any:
        
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
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedVirtualNetwork")
    def managed_virtual_network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedVirtualNetworkSettings")
    def managed_virtual_network_settings(self) -> Optional[outputs.ManagedVirtualNetworkSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]:
        
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
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> Optional[outputs.PurviewConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Mapping[str, Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlAdministratorLogin")
    def sql_administrator_login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlAdministratorLoginPassword")
    def sql_administrator_login_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedServiceBypassEnabled")
    def trusted_service_bypass_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkProfile")
    def virtual_network_profile(self) -> Optional[outputs.VirtualNetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceRepositoryConfiguration")
    def workspace_repository_configuration(self) -> Optional[outputs.WorkspaceRepositoryConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceUID")
    def workspace_uid(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceResult]:
        ...
    


def get_workspace(resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceResult:
    
    ...

def get_workspace_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceResult]:
    
    ...

