

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddonsConfigAddonsConfigArgs', 'AddonsConfigAddonsConfigArgsDict', 'AddonsConfigAddonsConfigAdvancedApiOpsConfigArgs', ..., 'AddonsConfigAddonsConfigApiSecurityConfigArgs', 'AddonsConfigAddonsConfigApiSecurityConfigArgsDict', ..., ..., 'AddonsConfigAddonsConfigIntegrationConfigArgs', 'AddonsConfigAddonsConfigIntegrationConfigArgsDict', 'AddonsConfigAddonsConfigMonetizationConfigArgs', 'AddonsConfigAddonsConfigMonetizationConfigArgsDict', 'ApiMetaDataArgs', 'ApiMetaDataArgsDict', 'ApiProductAttributeArgs', 'ApiProductAttributeArgsDict', 'ApiProductGraphqlOperationGroupArgs', 'ApiProductGraphqlOperationGroupArgsDict', 'ApiProductGraphqlOperationGroupOperationConfigArgs', ..., ..., ..., ..., ..., ..., ..., 'ApiProductGrpcOperationGroupArgs', 'ApiProductGrpcOperationGroupArgsDict', 'ApiProductGrpcOperationGroupOperationConfigArgs', ..., ..., ..., ..., ..., 'ApiProductOperationGroupArgs', 'ApiProductOperationGroupArgsDict', 'ApiProductOperationGroupOperationConfigArgs', 'ApiProductOperationGroupOperationConfigArgsDict', ..., ..., ..., ..., 'ApiProductOperationGroupOperationConfigQuotaArgs', ..., 'AppGroupAttributeArgs', 'AppGroupAttributeArgsDict', 'DeveloperAppAttributeArgs', 'DeveloperAppAttributeArgsDict', 'DeveloperAppCredentialArgs', 'DeveloperAppCredentialArgsDict', 'DeveloperAppCredentialApiProductArgs', 'DeveloperAppCredentialApiProductArgsDict', 'DeveloperAppCredentialAttributeArgs', 'DeveloperAppCredentialAttributeArgsDict', 'DeveloperAttributeArgs', 'DeveloperAttributeArgsDict', 'DnsZonePeeringConfigArgs', 'DnsZonePeeringConfigArgsDict', 'EnvironmentClientIpResolutionConfigArgs', 'EnvironmentClientIpResolutionConfigArgsDict', ..., ..., 'EnvironmentIamBindingConditionArgs', 'EnvironmentIamBindingConditionArgsDict', 'EnvironmentIamMemberConditionArgs', 'EnvironmentIamMemberConditionArgsDict', 'EnvironmentNodeConfigArgs', 'EnvironmentNodeConfigArgsDict', 'EnvironmentPropertiesArgs', 'EnvironmentPropertiesArgsDict', 'EnvironmentPropertiesPropertyArgs', 'EnvironmentPropertiesPropertyArgsDict', 'InstanceAccessLoggingConfigArgs', 'InstanceAccessLoggingConfigArgsDict', 'KeystoresAliasesKeyCertFileCertsInfoArgs', 'KeystoresAliasesKeyCertFileCertsInfoArgsDict', 'KeystoresAliasesKeyCertFileTimeoutsArgs', 'KeystoresAliasesKeyCertFileTimeoutsArgsDict', 'KeystoresAliasesPkcs12CertsInfoArgs', 'KeystoresAliasesPkcs12CertsInfoArgsDict', 'KeystoresAliasesPkcs12CertsInfoCertInfoArgs', 'KeystoresAliasesPkcs12CertsInfoCertInfoArgsDict', 'KeystoresAliasesSelfSignedCertCertsInfoArgs', 'KeystoresAliasesSelfSignedCertCertsInfoArgsDict', ..., ..., 'KeystoresAliasesSelfSignedCertSubjectArgs', 'KeystoresAliasesSelfSignedCertSubjectArgsDict', ..., ..., 'OrganizationPropertiesArgs', 'OrganizationPropertiesArgsDict', 'OrganizationPropertiesPropertyArgs', 'OrganizationPropertiesPropertyArgsDict', 'SecurityActionAllowArgs', 'SecurityActionAllowArgsDict', 'SecurityActionConditionConfigArgs', 'SecurityActionConditionConfigArgsDict', 'SecurityActionDenyArgs', 'SecurityActionDenyArgsDict', 'SecurityActionFlagArgs', 'SecurityActionFlagArgsDict', 'SecurityActionFlagHeaderArgs', 'SecurityActionFlagHeaderArgsDict', 'SecurityFeedbackFeedbackContextArgs', 'SecurityFeedbackFeedbackContextArgsDict', 'SecurityMonitoringConditionIncludeAllResourcesArgs', ..., 'SecurityProfileV2ProfileAssessmentConfigArgs', 'SecurityProfileV2ProfileAssessmentConfigArgsDict', 'SharedflowMetaDataArgs', 'SharedflowMetaDataArgsDict', 'TargetServerSSlInfoArgs', 'TargetServerSSlInfoArgsDict', 'TargetServerSSlInfoCommonNameArgs', 'TargetServerSSlInfoCommonNameArgsDict']
class AddonsConfigAddonsConfigArgsDict(TypedDict):
    advanced_api_ops_config: NotRequired[pulumi.Input[AddonsConfigAddonsConfigAdvancedApiOpsConfigArgsDict]]
    api_security_config: NotRequired[pulumi.Input[AddonsConfigAddonsConfigApiSecurityConfigArgsDict]]
    connectors_platform_config: NotRequired[pulumi.Input[AddonsConfigAddonsConfigConnectorsPlatformConfigArgsDict]]
    integration_config: NotRequired[pulumi.Input[AddonsConfigAddonsConfigIntegrationConfigArgsDict]]
    monetization_config: NotRequired[pulumi.Input[AddonsConfigAddonsConfigMonetizationConfigArgsDict]]


@pulumi.input_type
class AddonsConfigAddonsConfigArgs:
    def __init__(__self__, *, advanced_api_ops_config: Optional[pulumi.Input[AddonsConfigAddonsConfigAdvancedApiOpsConfigArgs]] = ..., api_security_config: Optional[pulumi.Input[AddonsConfigAddonsConfigApiSecurityConfigArgs]] = ..., connectors_platform_config: Optional[pulumi.Input[AddonsConfigAddonsConfigConnectorsPlatformConfigArgs]] = ..., integration_config: Optional[pulumi.Input[AddonsConfigAddonsConfigIntegrationConfigArgs]] = ..., monetization_config: Optional[pulumi.Input[AddonsConfigAddonsConfigMonetizationConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedApiOpsConfig")
    def advanced_api_ops_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigAdvancedApiOpsConfigArgs]]:
        
        ...
    
    @advanced_api_ops_config.setter
    def advanced_api_ops_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigAdvancedApiOpsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSecurityConfig")
    def api_security_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigApiSecurityConfigArgs]]:
        
        ...
    
    @api_security_config.setter
    def api_security_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigApiSecurityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorsPlatformConfig")
    def connectors_platform_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigConnectorsPlatformConfigArgs]]:
        
        ...
    
    @connectors_platform_config.setter
    def connectors_platform_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigConnectorsPlatformConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationConfig")
    def integration_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigIntegrationConfigArgs]]:
        
        ...
    
    @integration_config.setter
    def integration_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigIntegrationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monetizationConfig")
    def monetization_config(self) -> Optional[pulumi.Input[AddonsConfigAddonsConfigMonetizationConfigArgs]]:
        
        ...
    
    @monetization_config.setter
    def monetization_config(self, value: Optional[pulumi.Input[AddonsConfigAddonsConfigMonetizationConfigArgs]]): # -> None:
        ...
    


class AddonsConfigAddonsConfigAdvancedApiOpsConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AddonsConfigAddonsConfigAdvancedApiOpsConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AddonsConfigAddonsConfigApiSecurityConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expires_at: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddonsConfigAddonsConfigApiSecurityConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expires_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AddonsConfigAddonsConfigConnectorsPlatformConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expires_at: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddonsConfigAddonsConfigConnectorsPlatformConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expires_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AddonsConfigAddonsConfigIntegrationConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AddonsConfigAddonsConfigIntegrationConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AddonsConfigAddonsConfigMonetizationConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AddonsConfigAddonsConfigMonetizationConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ApiMetaDataArgsDict(TypedDict):
    created_at: NotRequired[pulumi.Input[_builtins.str]]
    last_modified_at: NotRequired[pulumi.Input[_builtins.str]]
    sub_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiMetaDataArgs:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., sub_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subType")
    def sub_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sub_type.setter
    def sub_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductGraphqlOperationGroupArgsDict(TypedDict):
    operation_config_type: NotRequired[pulumi.Input[_builtins.str]]
    operation_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigArgsDict]]]]


@pulumi.input_type
class ApiProductGraphqlOperationGroupArgs:
    def __init__(__self__, *, operation_config_type: Optional[pulumi.Input[_builtins.str]] = ..., operation_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigType")
    def operation_config_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation_config_type.setter
    def operation_config_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigArgs]]]]:
        
        ...
    
    @operation_configs.setter
    def operation_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigArgs]]]]): # -> None:
        ...
    


class ApiProductGraphqlOperationGroupOperationConfigArgsDict(TypedDict):
    api_source: NotRequired[pulumi.Input[_builtins.str]]
    attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigAttributeArgsDict]]]]
    operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigOperationArgsDict]]]]
    quota: NotRequired[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigQuotaArgsDict]]


@pulumi.input_type
class ApiProductGraphqlOperationGroupOperationConfigArgs:
    def __init__(__self__, *, api_source: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigAttributeArgs]]]] = ..., operations: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigOperationArgs]]]] = ..., quota: Optional[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigQuotaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_source.setter
    def api_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigOperationArgs]]]]:
        
        ...
    
    @operations.setter
    def operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigOperationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[ApiProductGraphqlOperationGroupOperationConfigQuotaArgs]]): # -> None:
        ...
    


class ApiProductGraphqlOperationGroupOperationConfigAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductGraphqlOperationGroupOperationConfigAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductGraphqlOperationGroupOperationConfigOperationArgsDict(TypedDict):
    operation: NotRequired[pulumi.Input[_builtins.str]]
    operation_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ApiProductGraphqlOperationGroupOperationConfigOperationArgs:
    def __init__(__self__, *, operation: Optional[pulumi.Input[_builtins.str]] = ..., operation_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationTypes")
    def operation_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @operation_types.setter
    def operation_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ApiProductGraphqlOperationGroupOperationConfigQuotaArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.str]]
    limit: NotRequired[pulumi.Input[_builtins.str]]
    time_unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductGraphqlOperationGroupOperationConfigQuotaArgs:
    def __init__(__self__, *, interval: Optional[pulumi.Input[_builtins.str]] = ..., limit: Optional[pulumi.Input[_builtins.str]] = ..., time_unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @limit.setter
    def limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductGrpcOperationGroupArgsDict(TypedDict):
    operation_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigArgsDict]]]]


@pulumi.input_type
class ApiProductGrpcOperationGroupArgs:
    def __init__(__self__, *, operation_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigArgs]]]]:
        
        ...
    
    @operation_configs.setter
    def operation_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigArgs]]]]): # -> None:
        ...
    


class ApiProductGrpcOperationGroupOperationConfigArgsDict(TypedDict):
    api_source: NotRequired[pulumi.Input[_builtins.str]]
    attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigAttributeArgsDict]]]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    quota: NotRequired[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigQuotaArgsDict]]
    service: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductGrpcOperationGroupOperationConfigArgs:
    def __init__(__self__, *, api_source: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigAttributeArgs]]]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., quota: Optional[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigQuotaArgs]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_source.setter
    def api_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[ApiProductGrpcOperationGroupOperationConfigQuotaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductGrpcOperationGroupOperationConfigAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductGrpcOperationGroupOperationConfigAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductGrpcOperationGroupOperationConfigQuotaArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.str]]
    limit: NotRequired[pulumi.Input[_builtins.str]]
    time_unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductGrpcOperationGroupOperationConfigQuotaArgs:
    def __init__(__self__, *, interval: Optional[pulumi.Input[_builtins.str]] = ..., limit: Optional[pulumi.Input[_builtins.str]] = ..., time_unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @limit.setter
    def limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductOperationGroupArgsDict(TypedDict):
    operation_config_type: NotRequired[pulumi.Input[_builtins.str]]
    operation_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigArgsDict]]]]


@pulumi.input_type
class ApiProductOperationGroupArgs:
    def __init__(__self__, *, operation_config_type: Optional[pulumi.Input[_builtins.str]] = ..., operation_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigType")
    def operation_config_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation_config_type.setter
    def operation_config_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationConfigs")
    def operation_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigArgs]]]]:
        
        ...
    
    @operation_configs.setter
    def operation_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigArgs]]]]): # -> None:
        ...
    


class ApiProductOperationGroupOperationConfigArgsDict(TypedDict):
    api_source: NotRequired[pulumi.Input[_builtins.str]]
    attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigAttributeArgsDict]]]]
    operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigOperationArgsDict]]]]
    quota: NotRequired[pulumi.Input[ApiProductOperationGroupOperationConfigQuotaArgsDict]]


@pulumi.input_type
class ApiProductOperationGroupOperationConfigArgs:
    def __init__(__self__, *, api_source: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigAttributeArgs]]]] = ..., operations: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigOperationArgs]]]] = ..., quota: Optional[pulumi.Input[ApiProductOperationGroupOperationConfigQuotaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSource")
    def api_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_source.setter
    def api_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigOperationArgs]]]]:
        
        ...
    
    @operations.setter
    def operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProductOperationGroupOperationConfigOperationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[ApiProductOperationGroupOperationConfigQuotaArgs]]:
        
        ...
    
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[ApiProductOperationGroupOperationConfigQuotaArgs]]): # -> None:
        ...
    


class ApiProductOperationGroupOperationConfigAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductOperationGroupOperationConfigAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductOperationGroupOperationConfigOperationArgsDict(TypedDict):
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductOperationGroupOperationConfigOperationArgs:
    def __init__(__self__, *, methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApiProductOperationGroupOperationConfigQuotaArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.str]]
    limit: NotRequired[pulumi.Input[_builtins.str]]
    time_unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiProductOperationGroupOperationConfigQuotaArgs:
    def __init__(__self__, *, interval: Optional[pulumi.Input[_builtins.str]] = ..., limit: Optional[pulumi.Input[_builtins.str]] = ..., time_unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @limit.setter
    def limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppGroupAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppGroupAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeveloperAppAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeveloperAppAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeveloperAppCredentialArgsDict(TypedDict):
    api_products: NotRequired[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialApiProductArgsDict]]]]
    attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialAttributeArgsDict]]]]
    consumer_key: NotRequired[pulumi.Input[_builtins.str]]
    consumer_secret: NotRequired[pulumi.Input[_builtins.str]]
    expires_at: NotRequired[pulumi.Input[_builtins.str]]
    issued_at: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeveloperAppCredentialArgs:
    def __init__(__self__, *, api_products: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialApiProductArgs]]]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialAttributeArgs]]]] = ..., consumer_key: Optional[pulumi.Input[_builtins.str]] = ..., consumer_secret: Optional[pulumi.Input[_builtins.str]] = ..., expires_at: Optional[pulumi.Input[_builtins.str]] = ..., issued_at: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialApiProductArgs]]]]:
        
        ...
    
    @api_products.setter
    def api_products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialApiProductArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerKey")
    def consumer_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_key.setter
    def consumer_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerSecret")
    def consumer_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_secret.setter
    def consumer_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuedAt")
    def issued_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issued_at.setter
    def issued_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeveloperAppCredentialApiProductArgsDict(TypedDict):
    apiproduct: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeveloperAppCredentialApiProductArgs:
    def __init__(__self__, *, apiproduct: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apiproduct(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @apiproduct.setter
    def apiproduct(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeveloperAppCredentialAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeveloperAppCredentialAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeveloperAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeveloperAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DnsZonePeeringConfigArgsDict(TypedDict):
    target_network_id: pulumi.Input[_builtins.str]
    target_project_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class DnsZonePeeringConfigArgs:
    def __init__(__self__, *, target_network_id: pulumi.Input[_builtins.str], target_project_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_network_id.setter
    def target_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProjectId")
    def target_project_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_project_id.setter
    def target_project_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EnvironmentClientIpResolutionConfigArgsDict(TypedDict):
    header_index_algorithm: NotRequired[pulumi.Input[EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgsDict]]


@pulumi.input_type
class EnvironmentClientIpResolutionConfigArgs:
    def __init__(__self__, *, header_index_algorithm: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerIndexAlgorithm")
    def header_index_algorithm(self) -> Optional[pulumi.Input[EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgs]]:
        
        ...
    
    @header_index_algorithm.setter
    def header_index_algorithm(self, value: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgs]]): # -> None:
        ...
    


class EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgsDict(TypedDict):
    ip_header_index: pulumi.Input[_builtins.int]
    ip_header_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class EnvironmentClientIpResolutionConfigHeaderIndexAlgorithmArgs:
    def __init__(__self__, *, ip_header_index: pulumi.Input[_builtins.int], ip_header_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipHeaderIndex")
    def ip_header_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @ip_header_index.setter
    def ip_header_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipHeaderName")
    def ip_header_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_header_name.setter
    def ip_header_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EnvironmentIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentNodeConfigArgsDict(TypedDict):
    current_aggregate_node_count: NotRequired[pulumi.Input[_builtins.str]]
    max_node_count: NotRequired[pulumi.Input[_builtins.str]]
    min_node_count: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentNodeConfigArgs:
    def __init__(__self__, *, current_aggregate_node_count: Optional[pulumi.Input[_builtins.str]] = ..., max_node_count: Optional[pulumi.Input[_builtins.str]] = ..., min_node_count: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentAggregateNodeCount")
    def current_aggregate_node_count(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @current_aggregate_node_count.setter
    def current_aggregate_node_count(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_node_count.setter
    def max_node_count(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentPropertiesArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentPropertiesPropertyArgsDict]]]]


@pulumi.input_type
class EnvironmentPropertiesArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentPropertiesPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentPropertiesPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentPropertiesPropertyArgs]]]]): # -> None:
        ...
    


class EnvironmentPropertiesPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentPropertiesPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceAccessLoggingConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    filter: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceAccessLoggingConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], filter: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeystoresAliasesKeyCertFileCertsInfoArgsDict(TypedDict):
    basic_constraints: pulumi.Input[_builtins.str]
    expiry_date: pulumi.Input[_builtins.str]
    is_valid: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    public_key: pulumi.Input[_builtins.str]
    serial_number: pulumi.Input[_builtins.str]
    sig_alg_name: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]
    subject_alternative_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    valid_from: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.int]


@pulumi.input_type
class KeystoresAliasesKeyCertFileCertsInfoArgs:
    def __init__(__self__, *, basic_constraints: pulumi.Input[_builtins.str], expiry_date: pulumi.Input[_builtins.str], is_valid: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], public_key: pulumi.Input[_builtins.str], serial_number: pulumi.Input[_builtins.str], sig_alg_name: pulumi.Input[_builtins.str], subject: pulumi.Input[_builtins.str], subject_alternative_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], valid_from: pulumi.Input[_builtins.str], version: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @basic_constraints.setter
    def basic_constraints(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expiry_date.setter
    def expiry_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @is_valid.setter
    def is_valid(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sig_alg_name.setter
    def sig_alg_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @valid_from.setter
    def valid_from(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class KeystoresAliasesKeyCertFileTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    read: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeystoresAliasesKeyCertFileTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., read: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @read.setter
    def read(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeystoresAliasesPkcs12CertsInfoArgsDict(TypedDict):
    cert_infos: NotRequired[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoCertInfoArgsDict]]]]


@pulumi.input_type
class KeystoresAliasesPkcs12CertsInfoArgs:
    def __init__(__self__, *, cert_infos: Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoCertInfoArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certInfos")
    def cert_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoCertInfoArgs]]]]:
        
        ...
    
    @cert_infos.setter
    def cert_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesPkcs12CertsInfoCertInfoArgs]]]]): # -> None:
        ...
    


class KeystoresAliasesPkcs12CertsInfoCertInfoArgsDict(TypedDict):
    basic_constraints: NotRequired[pulumi.Input[_builtins.str]]
    expiry_date: NotRequired[pulumi.Input[_builtins.str]]
    is_valid: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    public_key: NotRequired[pulumi.Input[_builtins.str]]
    serial_number: NotRequired[pulumi.Input[_builtins.str]]
    sig_alg_name: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]
    subject_alternative_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    valid_from: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class KeystoresAliasesPkcs12CertsInfoCertInfoArgs:
    def __init__(__self__, *, basic_constraints: Optional[pulumi.Input[_builtins.str]] = ..., expiry_date: Optional[pulumi.Input[_builtins.str]] = ..., is_valid: Optional[pulumi.Input[_builtins.str]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., sig_alg_name: Optional[pulumi.Input[_builtins.str]] = ..., subject: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_constraints.setter
    def basic_constraints(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sig_alg_name.setter
    def sig_alg_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class KeystoresAliasesSelfSignedCertCertsInfoArgsDict(TypedDict):
    cert_infos: NotRequired[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgsDict]]]]


@pulumi.input_type
class KeystoresAliasesSelfSignedCertCertsInfoArgs:
    def __init__(__self__, *, cert_infos: Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certInfos")
    def cert_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgs]]]]:
        
        ...
    
    @cert_infos.setter
    def cert_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgs]]]]): # -> None:
        ...
    


class KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgsDict(TypedDict):
    basic_constraints: NotRequired[pulumi.Input[_builtins.str]]
    expiry_date: NotRequired[pulumi.Input[_builtins.str]]
    is_valid: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    public_key: NotRequired[pulumi.Input[_builtins.str]]
    serial_number: NotRequired[pulumi.Input[_builtins.str]]
    sig_alg_name: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]
    subject_alternative_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    valid_from: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class KeystoresAliasesSelfSignedCertCertsInfoCertInfoArgs:
    def __init__(__self__, *, basic_constraints: Optional[pulumi.Input[_builtins.str]] = ..., expiry_date: Optional[pulumi.Input[_builtins.str]] = ..., is_valid: Optional[pulumi.Input[_builtins.str]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., sig_alg_name: Optional[pulumi.Input[_builtins.str]] = ..., subject: Optional[pulumi.Input[_builtins.str]] = ..., subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConstraints")
    def basic_constraints(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_constraints.setter
    def basic_constraints(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigAlgName")
    def sig_alg_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sig_alg_name.setter
    def sig_alg_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class KeystoresAliasesSelfSignedCertSubjectArgsDict(TypedDict):
    common_name: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    org: NotRequired[pulumi.Input[_builtins.str]]
    org_unit: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeystoresAliasesSelfSignedCertSubjectArgs:
    def __init__(__self__, *, common_name: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., locality: Optional[pulumi.Input[_builtins.str]] = ..., org: Optional[pulumi.Input[_builtins.str]] = ..., org_unit: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org.setter
    def org(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_unit.setter
    def org_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgsDict(TypedDict):
    subject_alternative_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs:
    def __init__(__self__, *, subject_alternative_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeName")
    def subject_alternative_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject_alternative_name.setter
    def subject_alternative_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationPropertiesArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[OrganizationPropertiesPropertyArgsDict]]]]


@pulumi.input_type
class OrganizationPropertiesArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationPropertiesPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationPropertiesPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationPropertiesPropertyArgs]]]]): # -> None:
        ...
    


class OrganizationPropertiesPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OrganizationPropertiesPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityActionAllowArgsDict(TypedDict):
    ...


@pulumi.input_type
class SecurityActionAllowArgs:
    def __init__(__self__) -> None:
        ...
    


class SecurityActionConditionConfigArgsDict(TypedDict):
    access_tokens: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    api_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    api_products: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    asns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bot_reasons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    developer_apps: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    developers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    http_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_address_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_agents: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SecurityActionConditionConfigArgs:
    def __init__(__self__, *, access_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., api_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., api_products: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., asns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bot_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., developer_apps: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., developers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., http_methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_address_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., user_agents: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokens")
    def access_tokens(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @access_tokens.setter
    def access_tokens(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_keys.setter
    def api_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_products.setter
    def api_products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def asns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @asns.setter
    def asns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botReasons")
    def bot_reasons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @bot_reasons.setter
    def bot_reasons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerApps")
    def developer_apps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @developer_apps.setter
    def developer_apps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def developers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @developers.setter
    def developers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethods")
    def http_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @http_methods.setter
    def http_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRanges")
    def ip_address_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_address_ranges.setter
    def ip_address_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCodes")
    def region_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @region_codes.setter
    def region_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAgents")
    def user_agents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_agents.setter
    def user_agents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SecurityActionDenyArgsDict(TypedDict):
    response_code: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SecurityActionDenyArgs:
    def __init__(__self__, *, response_code: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SecurityActionFlagArgsDict(TypedDict):
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityActionFlagHeaderArgsDict]]]]


@pulumi.input_type
class SecurityActionFlagArgs:
    def __init__(__self__, *, headers: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityActionFlagHeaderArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityActionFlagHeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityActionFlagHeaderArgs]]]]): # -> None:
        ...
    


class SecurityActionFlagHeaderArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityActionFlagHeaderArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityFeedbackFeedbackContextArgsDict(TypedDict):
    attribute: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class SecurityFeedbackFeedbackContextArgs:
    def __init__(__self__, *, attribute: pulumi.Input[_builtins.str], values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attribute.setter
    def attribute(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class SecurityMonitoringConditionIncludeAllResourcesArgsDict(TypedDict):
    ...


@pulumi.input_type
class SecurityMonitoringConditionIncludeAllResourcesArgs:
    def __init__(__self__) -> None:
        ...
    


class SecurityProfileV2ProfileAssessmentConfigArgsDict(TypedDict):
    assessment: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecurityProfileV2ProfileAssessmentConfigArgs:
    def __init__(__self__, *, assessment: pulumi.Input[_builtins.str], weight: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assessment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @assessment.setter
    def assessment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SharedflowMetaDataArgsDict(TypedDict):
    created_at: NotRequired[pulumi.Input[_builtins.str]]
    last_modified_at: NotRequired[pulumi.Input[_builtins.str]]
    sub_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SharedflowMetaDataArgs:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., sub_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subType")
    def sub_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sub_type.setter
    def sub_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetServerSSlInfoArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ciphers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    client_auth_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    common_name: NotRequired[pulumi.Input[TargetServerSSlInfoCommonNameArgsDict]]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_validation_errors: NotRequired[pulumi.Input[_builtins.bool]]
    key_alias: NotRequired[pulumi.Input[_builtins.str]]
    key_store: NotRequired[pulumi.Input[_builtins.str]]
    protocols: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    trust_store: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetServerSSlInfoArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], ciphers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., common_name: Optional[pulumi.Input[TargetServerSSlInfoCommonNameArgs]] = ..., enforce: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_validation_errors: Optional[pulumi.Input[_builtins.bool]] = ..., key_alias: Optional[pulumi.Input[_builtins.str]] = ..., key_store: Optional[pulumi.Input[_builtins.str]] = ..., protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., trust_store: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ciphers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ciphers.setter
    def ciphers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthEnabled")
    def client_auth_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @client_auth_enabled.setter
    def client_auth_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[TargetServerSSlInfoCommonNameArgs]]:
        
        ...
    
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[TargetServerSSlInfoCommonNameArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreValidationErrors")
    def ignore_validation_errors(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_validation_errors.setter
    def ignore_validation_errors(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlias")
    def key_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_alias.setter
    def key_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStore")
    def key_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_store.setter
    def key_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @protocols.setter
    def protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStore")
    def trust_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_store.setter
    def trust_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetServerSSlInfoCommonNameArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.str]]
    wildcard_match: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TargetServerSSlInfoCommonNameArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[_builtins.str]] = ..., wildcard_match: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wildcardMatch")
    def wildcard_match(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wildcard_match.setter
    def wildcard_match(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


