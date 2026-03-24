

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceResult', 'AwaitableGetWorkspaceResult', 'get_workspace', 'get_workspace_output']
@pulumi.output_type
class GetWorkspaceResult:
    
    def __init__(__self__, access_connector=..., authorizations=..., azure_api_version=..., created_by=..., created_date_time=..., default_catalog=..., default_storage_firewall=..., disk_encryption_set_id=..., encryption=..., enhanced_security_compliance=..., id=..., is_uc_enabled=..., location=..., managed_disk_identity=..., managed_resource_group_id=..., name=..., parameters=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., required_nsg_rules=..., sku=..., storage_account_identity=..., system_data=..., tags=..., type=..., ui_definition_uri=..., updated_by=..., workspace_id=..., workspace_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConnector")
    def access_connector(self) -> Optional[outputs.WorkspacePropertiesResponseAccessConnector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Optional[Sequence[outputs.WorkspaceProviderAuthorizationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[outputs.CreatedByResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCatalog")
    def default_catalog(self) -> Optional[outputs.DefaultCatalogPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStorageFirewall")
    def default_storage_firewall(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.WorkspacePropertiesResponseEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityCompliance")
    def enhanced_security_compliance(self) -> Optional[outputs.EnhancedSecurityComplianceDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUcEnabled")
    def is_uc_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDiskIdentity")
    def managed_disk_identity(self) -> Optional[outputs.ManagedIdentityConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupId")
    def managed_resource_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[outputs.WorkspaceCustomParametersResponse]:
        
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
    @pulumi.getter(name="requiredNsgRules")
    def required_nsg_rules(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountIdentity")
    def storage_account_identity(self) -> Optional[outputs.ManagedIdentityConfigurationResponse]:
        
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
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiDefinitionUri")
    def ui_definition_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[outputs.CreatedByResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceUrl")
    def workspace_url(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceResult]:
        ...
    


def get_workspace(resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceResult:
    
    ...

def get_workspace_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceResult]:
    
    ...

