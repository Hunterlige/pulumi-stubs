

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureHybridBenefitPropertiesResponse', 'DatabaseInstancePropertiesResponse', 'DomainControllerPropertiesResponse', 'DomainUserCredentialsResponse', 'GmsaDetailsResponse', 'LogAnalyticsConfigurationResponse', 'ManagedGatewayPropertiesResponse', 'ManagedIdentityResponse', 'ManagedInstanceOperationStatusResponse', 'ManagementServerPropertiesResponse', 'MonitoredResourcePropertiesResponse', 'MonitoringInstancePropertiesResponse', 'SystemDataResponse', 'UserIdentityResponse']
@pulumi.output_type
class AzureHybridBenefitPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scom_license_type: Optional[_builtins.str] = ..., sql_server_license_type: Optional[_builtins.str] = ..., windows_server_license_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scomLicenseType")
    def scom_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsServerLicenseType")
    def windows_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstancePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_fqdn: _builtins.str, dw_database_id: _builtins.str, dw_database_name: _builtins.str, operational_database_id: _builtins.str, database_instance_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFqdn")
    def database_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dwDatabaseId")
    def dw_database_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dwDatabaseName")
    def dw_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationalDatabaseId")
    def operational_database_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseInstanceId")
    def database_instance_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainControllerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_server: Optional[_builtins.str] = ..., domain_name: Optional[_builtins.str] = ..., ou_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServer")
    def dns_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ouPath")
    def ou_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainUserCredentialsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_vault_url: Optional[_builtins.str] = ..., password_secret: Optional[_builtins.str] = ..., user_name_secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userNameSecret")
    def user_name_secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GmsaDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_name: Optional[_builtins.str] = ..., gmsa_account: Optional[_builtins.str] = ..., load_balancer_ip: Optional[_builtins.str] = ..., management_server_group_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaAccount")
    def gmsa_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerIP")
    def load_balancer_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementServerGroupName")
    def management_server_group_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogAnalyticsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_types: Optional[Sequence[_builtins.str]] = ..., import_data: Optional[_builtins.bool] = ..., workspace_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importData")
    def import_data(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedGatewayPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_status: _builtins.str, health_status: _builtins.str, install_type: _builtins.str, management_server_endpoint: _builtins.str, provisioning_state: _builtins.str, version: _builtins.str, computer_name: Optional[_builtins.str] = ..., domain_name: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installType")
    def install_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementServerEndpoint")
    def management_server_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class ManagedInstanceOperationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, operation_name: _builtins.str, operation_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationState")
    def operation_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagementServerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: _builtins.str, health_state: _builtins.str, server_name: _builtins.str, server_roles: _builtins.str, vm_res_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRoles")
    def server_roles(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmResId")
    def vm_res_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MonitoredResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_version: _builtins.str, connection_status: _builtins.str, health_status: _builtins.str, install_type: _builtins.str, management_server_endpoint: _builtins.str, provisioning_state: _builtins.str, computer_name: Optional[_builtins.str] = ..., domain_name: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installType")
    def install_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementServerEndpoint")
    def management_server_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitoringInstancePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_analytics_properties: outputs.LogAnalyticsConfigurationResponse, management_endpoints: Sequence[outputs.ManagementServerPropertiesResponse], operations_status: Sequence[outputs.ManagedInstanceOperationStatusResponse], product_version: _builtins.str, provisioning_state: _builtins.str, azure_hybrid_benefit: Optional[outputs.AzureHybridBenefitPropertiesResponse] = ..., database_instance: Optional[outputs.DatabaseInstancePropertiesResponse] = ..., domain_controller: Optional[outputs.DomainControllerPropertiesResponse] = ..., domain_user_credentials: Optional[outputs.DomainUserCredentialsResponse] = ..., gmsa_details: Optional[outputs.GmsaDetailsResponse] = ..., v_net_subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsProperties")
    def log_analytics_properties(self) -> outputs.LogAnalyticsConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementEndpoints")
    def management_endpoints(self) -> Sequence[outputs.ManagementServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationsStatus")
    def operations_status(self) -> Sequence[outputs.ManagedInstanceOperationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productVersion")
    def product_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> Optional[outputs.AzureHybridBenefitPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseInstance")
    def database_instance(self) -> Optional[outputs.DatabaseInstancePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainController")
    def domain_controller(self) -> Optional[outputs.DomainControllerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainUserCredentials")
    def domain_user_credentials(self) -> Optional[outputs.DomainUserCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gmsaDetails")
    def gmsa_details(self) -> Optional[outputs.GmsaDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vNetSubnetId")
    def v_net_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


