

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddonsConfigAddonsConfig', 'AddonsConfigAddonsConfigAdvancedApiOpsConfig', 'AddonsConfigAddonsConfigApiSecurityConfig', 'AddonsConfigAddonsConfigConnectorsPlatformConfig', 'AddonsConfigAddonsConfigIntegrationConfig', 'AddonsConfigAddonsConfigMonetizationConfig', 'ApiMetaData', 'ApiProductAttribute', 'ApiProductGraphqlOperationGroup', 'ApiProductGraphqlOperationGroupOperationConfig', ..., ..., ..., 'ApiProductGrpcOperationGroup', 'ApiProductGrpcOperationGroupOperationConfig', ..., 'ApiProductGrpcOperationGroupOperationConfigQuota', 'ApiProductOperationGroup', 'ApiProductOperationGroupOperationConfig', 'ApiProductOperationGroupOperationConfigAttribute', 'ApiProductOperationGroupOperationConfigOperation', 'ApiProductOperationGroupOperationConfigQuota', 'AppGroupAttribute', 'DeveloperAppAttribute', 'DeveloperAppCredential', 'DeveloperAppCredentialApiProduct', 'DeveloperAppCredentialAttribute', 'DeveloperAttribute', 'DnsZonePeeringConfig', 'EnvironmentClientIpResolutionConfig', ..., 'EnvironmentIamBindingCondition', 'EnvironmentIamMemberCondition', 'EnvironmentNodeConfig', 'EnvironmentProperties', 'EnvironmentPropertiesProperty', 'InstanceAccessLoggingConfig', 'KeystoresAliasesKeyCertFileCertsInfo', 'KeystoresAliasesKeyCertFileTimeouts', 'KeystoresAliasesPkcs12CertsInfo', 'KeystoresAliasesPkcs12CertsInfoCertInfo', 'KeystoresAliasesSelfSignedCertCertsInfo', 'KeystoresAliasesSelfSignedCertCertsInfoCertInfo', 'KeystoresAliasesSelfSignedCertSubject', ..., 'OrganizationProperties', 'OrganizationPropertiesProperty', 'SecurityActionAllow', 'SecurityActionConditionConfig', 'SecurityActionDeny', 'SecurityActionFlag', 'SecurityActionFlagHeader', 'SecurityFeedbackFeedbackContext', 'SecurityMonitoringConditionIncludeAllResources', 'SecurityProfileV2ProfileAssessmentConfig', 'SharedflowMetaData', 'TargetServerSSlInfo', 'TargetServerSSlInfoCommonName']
@pulumi.output_type
class AddonsConfigAddonsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, advanced_api_ops_config: Optional[outputs.AddonsConfigAddonsConfigAdvancedApiOpsConfig] = ..., api_security_config: Optional[outputs.AddonsConfigAddonsConfigApiSecurityConfig] = ..., connectors_platform_config: Optional[outputs.AddonsConfigAddonsConfigConnectorsPlatformConfig] = ..., integration_config: Optional[outputs.AddonsConfigAddonsConfigIntegrationConfig] = ..., monetization_config: Optional[outputs.AddonsConfigAddonsConfigMonetizationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedApiOpsConfig")
    def advanced_api_ops_config(self) -> Optional[outputs.AddonsConfigAddonsConfigAdvancedApiOpsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSecurityConfig")
    def api_security_config(self) -> Optional[outputs.AddonsConfigAddonsConfigApiSecurityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorsPlatformConfig")
    def connectors_platform_config(self) -> Optional[outputs.AddonsConfigAddonsConfigConnectorsPlatformConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationConfig")
    def integration_config(self) -> Optional[outputs.AddonsConfigAddonsConfigIntegrationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monetizationConfig")
    def monetization_config(self) -> Optional[outputs.AddonsConfigAddonsConfigMonetizationConfig]:
        
        ...
    


@pulumi.output_type
class AddonsConfigAddonsConfigAdvancedApiOpsConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AddonsConfigAddonsConfigApiSecurityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., expires_at: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AddonsConfigAddonsConfigConnectorsPlatformConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., expires_at: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AddonsConfigAddonsConfigIntegrationConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AddonsConfigAddonsConfigMonetizationConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApiMetaData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., sub_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subType")
    def sub_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductGraphqlOperationGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operation_config_type: Optional[_builtins.str] = ..., operation_configs: Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigType")
    def operation_config_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfig]]:
        
        ...
    


@pulumi.output_type
class ApiProductGraphqlOperationGroupOperationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_source: Optional[_builtins.str] = ..., attributes: Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfigAttribute]] = ..., operations: Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfigOperation]] = ..., quota: Optional[outputs.ApiProductGraphqlOperationGroupOperationConfigQuota] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfigAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[Sequence[outputs.ApiProductGraphqlOperationGroupOperationConfigOperation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[outputs.ApiProductGraphqlOperationGroupOperationConfigQuota]:
        
        ...
    


@pulumi.output_type
class ApiProductGraphqlOperationGroupOperationConfigAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductGraphqlOperationGroupOperationConfigOperation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operation: Optional[_builtins.str] = ..., operation_types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationTypes")
    def operation_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ApiProductGraphqlOperationGroupOperationConfigQuota(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interval: Optional[_builtins.str] = ..., limit: Optional[_builtins.str] = ..., time_unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductGrpcOperationGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operation_configs: Optional[Sequence[outputs.ApiProductGrpcOperationGroupOperationConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[Sequence[outputs.ApiProductGrpcOperationGroupOperationConfig]]:
        
        ...
    


@pulumi.output_type
class ApiProductGrpcOperationGroupOperationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_source: Optional[_builtins.str] = ..., attributes: Optional[Sequence[outputs.ApiProductGrpcOperationGroupOperationConfigAttribute]] = ..., methods: Optional[Sequence[_builtins.str]] = ..., quota: Optional[outputs.ApiProductGrpcOperationGroupOperationConfigQuota] = ..., service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Sequence[outputs.ApiProductGrpcOperationGroupOperationConfigAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[outputs.ApiProductGrpcOperationGroupOperationConfigQuota]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductGrpcOperationGroupOperationConfigAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductGrpcOperationGroupOperationConfigQuota(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interval: Optional[_builtins.str] = ..., limit: Optional[_builtins.str] = ..., time_unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductOperationGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operation_config_type: Optional[_builtins.str] = ..., operation_configs: Optional[Sequence[outputs.ApiProductOperationGroupOperationConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigType")
    def operation_config_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[Sequence[outputs.ApiProductOperationGroupOperationConfig]]:
        
        ...
    


@pulumi.output_type
class ApiProductOperationGroupOperationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_source: Optional[_builtins.str] = ..., attributes: Optional[Sequence[outputs.ApiProductOperationGroupOperationConfigAttribute]] = ..., operations: Optional[Sequence[outputs.ApiProductOperationGroupOperationConfigOperation]] = ..., quota: Optional[outputs.ApiProductOperationGroupOperationConfigQuota] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Sequence[outputs.ApiProductOperationGroupOperationConfigAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[Sequence[outputs.ApiProductOperationGroupOperationConfigOperation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[outputs.ApiProductOperationGroupOperationConfigQuota]:
        
        ...
    


@pulumi.output_type
class ApiProductOperationGroupOperationConfigAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductOperationGroupOperationConfigOperation(dict):
    def __init__(__self__, *, methods: Optional[Sequence[_builtins.str]] = ..., resource: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiProductOperationGroupOperationConfigQuota(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interval: Optional[_builtins.str] = ..., limit: Optional[_builtins.str] = ..., time_unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppGroupAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeveloperAppAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeveloperAppCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_products: Optional[Sequence[outputs.DeveloperAppCredentialApiProduct]] = ..., attributes: Optional[Sequence[outputs.DeveloperAppCredentialAttribute]] = ..., consumer_key: Optional[_builtins.str] = ..., consumer_secret: Optional[_builtins.str] = ..., expires_at: Optional[_builtins.str] = ..., issued_at: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[Sequence[outputs.DeveloperAppCredentialApiProduct]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Sequence[outputs.DeveloperAppCredentialAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerKey")
    def consumer_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerSecret")
    def consumer_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuedAt")
    def issued_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeveloperAppCredentialApiProduct(dict):
    def __init__(__self__, *, apiproduct: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apiproduct(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeveloperAppCredentialAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeveloperAttribute(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DnsZonePeeringConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_network_id: _builtins.str, target_project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProjectId")
    def target_project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnvironmentClientIpResolutionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_index_algorithm: Optional[outputs.EnvironmentClientIpResolutionConfigHeaderIndexAlgorithm] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerIndexAlgorithm")
    def header_index_algorithm(self) -> Optional[outputs.EnvironmentClientIpResolutionConfigHeaderIndexAlgorithm]:
        
        ...
    


@pulumi.output_type
class EnvironmentClientIpResolutionConfigHeaderIndexAlgorithm(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_header_index: _builtins.int, ip_header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipHeaderIndex")
    def ip_header_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipHeaderName")
    def ip_header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnvironmentIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class EnvironmentIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class EnvironmentNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, current_aggregate_node_count: Optional[_builtins.str] = ..., max_node_count: Optional[_builtins.str] = ..., min_node_count: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentAggregateNodeCount")
    def current_aggregate_node_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentProperties(dict):
    def __init__(__self__, *, properties: Optional[Sequence[outputs.EnvironmentPropertiesProperty]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[outputs.EnvironmentPropertiesProperty]]:
        
        ...
    


@pulumi.output_type
class EnvironmentPropertiesProperty(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceAccessLoggingConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool, filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesKeyCertFileCertsInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_constraints: _builtins.str, expiry_date: _builtins.str, is_valid: _builtins.str, issuer: _builtins.str, public_key: _builtins.str, serial_number: _builtins.str, sig_alg_name: _builtins.str, subject: _builtins.str, subject_alternative_names: Sequence[_builtins.str], valid_from: _builtins.str, version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesKeyCertFileTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., read: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesPkcs12CertsInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert_infos: Optional[Sequence[outputs.KeystoresAliasesPkcs12CertsInfoCertInfo]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certInfos")
    def cert_infos(self) -> Optional[Sequence[outputs.KeystoresAliasesPkcs12CertsInfoCertInfo]]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesPkcs12CertsInfoCertInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_constraints: Optional[_builtins.str] = ..., expiry_date: Optional[_builtins.str] = ..., is_valid: Optional[_builtins.str] = ..., issuer: Optional[_builtins.str] = ..., public_key: Optional[_builtins.str] = ..., serial_number: Optional[_builtins.str] = ..., sig_alg_name: Optional[_builtins.str] = ..., subject: Optional[_builtins.str] = ..., subject_alternative_names: Optional[Sequence[_builtins.str]] = ..., valid_from: Optional[_builtins.str] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesSelfSignedCertCertsInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert_infos: Optional[Sequence[outputs.KeystoresAliasesSelfSignedCertCertsInfoCertInfo]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certInfos")
    def cert_infos(self) -> Optional[Sequence[outputs.KeystoresAliasesSelfSignedCertCertsInfoCertInfo]]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesSelfSignedCertCertsInfoCertInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_constraints: Optional[_builtins.str] = ..., expiry_date: Optional[_builtins.str] = ..., is_valid: Optional[_builtins.str] = ..., issuer: Optional[_builtins.str] = ..., public_key: Optional[_builtins.str] = ..., serial_number: Optional[_builtins.str] = ..., sig_alg_name: Optional[_builtins.str] = ..., subject: Optional[_builtins.str] = ..., subject_alternative_names: Optional[Sequence[_builtins.str]] = ..., valid_from: Optional[_builtins.str] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesSelfSignedCertSubject(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, common_name: Optional[_builtins.str] = ..., country_code: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., org: Optional[_builtins.str] = ..., org_unit: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNames(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subject_alternative_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeName")
    def subject_alternative_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationProperties(dict):
    def __init__(__self__, *, properties: Optional[Sequence[outputs.OrganizationPropertiesProperty]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[outputs.OrganizationPropertiesProperty]]:
        
        ...
    


@pulumi.output_type
class OrganizationPropertiesProperty(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityActionAllow(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class SecurityActionConditionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_tokens: Optional[Sequence[_builtins.str]] = ..., api_keys: Optional[Sequence[_builtins.str]] = ..., api_products: Optional[Sequence[_builtins.str]] = ..., asns: Optional[Sequence[_builtins.str]] = ..., bot_reasons: Optional[Sequence[_builtins.str]] = ..., developer_apps: Optional[Sequence[_builtins.str]] = ..., developers: Optional[Sequence[_builtins.str]] = ..., http_methods: Optional[Sequence[_builtins.str]] = ..., ip_address_ranges: Optional[Sequence[_builtins.str]] = ..., region_codes: Optional[Sequence[_builtins.str]] = ..., user_agents: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokens")
    def access_tokens(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botReasons")
    def bot_reasons(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerApps")
    def developer_apps(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def developers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethods")
    def http_methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRanges")
    def ip_address_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCodes")
    def region_codes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAgents")
    def user_agents(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SecurityActionDeny(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SecurityActionFlag(dict):
    def __init__(__self__, *, headers: Optional[Sequence[outputs.SecurityActionFlagHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.SecurityActionFlagHeader]]:
        
        ...
    


@pulumi.output_type
class SecurityActionFlagHeader(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityFeedbackFeedbackContext(dict):
    def __init__(__self__, *, attribute: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityMonitoringConditionIncludeAllResources(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class SecurityProfileV2ProfileAssessmentConfig(dict):
    def __init__(__self__, *, assessment: _builtins.str, weight: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assessment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SharedflowMetaData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., sub_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subType")
    def sub_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TargetServerSSlInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, ciphers: Optional[Sequence[_builtins.str]] = ..., client_auth_enabled: Optional[_builtins.bool] = ..., common_name: Optional[outputs.TargetServerSSlInfoCommonName] = ..., enforce: Optional[_builtins.bool] = ..., ignore_validation_errors: Optional[_builtins.bool] = ..., key_alias: Optional[_builtins.str] = ..., key_store: Optional[_builtins.str] = ..., protocols: Optional[Sequence[_builtins.str]] = ..., trust_store: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ciphers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthEnabled")
    def client_auth_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[outputs.TargetServerSSlInfoCommonName]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreValidationErrors")
    def ignore_validation_errors(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlias")
    def key_alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStore")
    def key_store(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStore")
    def trust_store(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TargetServerSSlInfoCommonName(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, value: Optional[_builtins.str] = ..., wildcard_match: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wildcardMatch")
    def wildcard_match(self) -> Optional[_builtins.bool]:
        
        ...
    


