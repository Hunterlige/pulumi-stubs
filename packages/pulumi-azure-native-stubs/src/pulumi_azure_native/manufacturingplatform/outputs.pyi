import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdxProfileResponse",
    "AksProfileResponse",
    "ApplicationVersionResponse",
    "CmkProfileResponse",
    "DatabaseProfileResponse",
    "DenyAssignmentExclusionResponse",
    "EventHubProfileResponse",
    "FabricProfileResponse",
    "FunctionAppProfileResponse",
    "ManagedOnBehalfOfConfigurationResponse",
    "ManagedResourceGroupConfigurationResponse",
    "ManagedServiceIdentityResponse",
    "MdsResourcePropertiesResponse",
    "MoboBrokerResourceResponse",
    "MonitoringProfileResponse",
    "OpenAIProfileResponse",
    "RedisProfileResponse",
    "SkuResponse",
    "StorageProfileResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
    "UserManagedOpenAIProfileResponse",
]

@pulumi.output_type
class AdxProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_ingestion_uri: _builtins.str,
        id: _builtins.str,
        uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class AksProfileResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationVersionResponse(dict):
    def __init__(
        __self__,
        *,
        is_deprecated: _builtins.bool,
        is_latest: _builtins.bool,
        is_preview: _builtins.bool,
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isLatest")
    def is_latest(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class CmkProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> _builtins.str: ...

@pulumi.output_type
class DatabaseProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cosmos_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cosmosId")
    def cosmos_id(self) -> _builtins.str: ...

@pulumi.output_type
class DenyAssignmentExclusionResponse(dict):
    def __init__(__self__, *, id: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class EventHubProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, adx_instance_id: _builtins.str, host_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adxInstanceId")
    def adx_instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...

@pulumi.output_type
class FabricProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_uri: _builtins.str,
        one_lake_path: _builtins.str,
        one_lake_uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oneLakePath")
    def one_lake_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oneLakeUri")
    def one_lake_uri(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionAppProfileResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedOnBehalfOfConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mobo_broker_resources: Sequence[outputs.MoboBrokerResourceResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="moboBrokerResources")
    def mobo_broker_resources(self) -> Sequence[outputs.MoboBrokerResourceResponse]: ...

@pulumi.output_type
class ManagedResourceGroupConfigurationResponse(dict):
    def __init__(__self__, *, location: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class MdsResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aad_application_id: _builtins.str,
        adx_profile: outputs.AdxProfileResponse,
        aks_profile: outputs.AksProfileResponse,
        database_profile: outputs.DatabaseProfileResponse,
        event_hub_profile: outputs.EventHubProfileResponse,
        function_app_profile: outputs.FunctionAppProfileResponse,
        managed_on_behalf_of_configuration: outputs.ManagedOnBehalfOfConfigurationResponse,
        managed_resource_group_configuration: outputs.ManagedResourceGroupConfigurationResponse,
        monitoring_profile: outputs.MonitoringProfileResponse,
        provisioning_state: _builtins.str,
        redis_profile: outputs.RedisProfileResponse,
        service_url: _builtins.str,
        storage_profile: outputs.StorageProfileResponse,
        aks_admin_group_id: Optional[_builtins.str] = ...,
        cmk_profile: Optional[outputs.CmkProfileResponse] = ...,
        deny_assignment_exclusions: Optional[
            Sequence[outputs.DenyAssignmentExclusionResponse]
        ] = ...,
        enable_copilot: Optional[_builtins.bool] = ...,
        enable_diagnostic_settings: Optional[_builtins.bool] = ...,
        fabric_profile: Optional[outputs.FabricProfileResponse] = ...,
        open_ai_profile: Optional[outputs.OpenAIProfileResponse] = ...,
        redundancy_state: Optional[_builtins.str] = ...,
        resource_state: Optional[_builtins.str] = ...,
        user_managed_open_ai_profile: Optional[
            outputs.UserManagedOpenAIProfileResponse
        ] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadApplicationId")
    def aad_application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="adxProfile")
    def adx_profile(self) -> outputs.AdxProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="aksProfile")
    def aks_profile(self) -> outputs.AksProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="databaseProfile")
    def database_profile(self) -> outputs.DatabaseProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="eventHubProfile")
    def event_hub_profile(self) -> outputs.EventHubProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="functionAppProfile")
    def function_app_profile(self) -> outputs.FunctionAppProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(
        self,
    ) -> outputs.ManagedOnBehalfOfConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> outputs.ManagedResourceGroupConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="monitoringProfile")
    def monitoring_profile(self) -> outputs.MonitoringProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redisProfile")
    def redis_profile(self) -> outputs.RedisProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> outputs.StorageProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="aksAdminGroupId")
    def aks_admin_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cmkProfile")
    def cmk_profile(self) -> Optional[outputs.CmkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="denyAssignmentExclusions")
    def deny_assignment_exclusions(
        self,
    ) -> Optional[Sequence[outputs.DenyAssignmentExclusionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCopilot")
    def enable_copilot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableDiagnosticSettings")
    def enable_diagnostic_settings(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> Optional[outputs.FabricProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="openAIProfile")
    def open_ai_profile(self) -> Optional[outputs.OpenAIProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="redundancyState")
    def redundancy_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userManagedOpenAIProfile")
    def user_managed_open_ai_profile(
        self,
    ) -> Optional[outputs.UserManagedOpenAIProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MoboBrokerResourceResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class MonitoringProfileResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class OpenAIProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        embedding_model_capacity: Optional[_builtins.int] = ...,
        embedding_model_name: Optional[_builtins.str] = ...,
        embedding_model_sku_name: Optional[_builtins.str] = ...,
        embedding_model_version: Optional[_builtins.str] = ...,
        gpt_model_capacity: Optional[_builtins.int] = ...,
        gpt_model_name: Optional[_builtins.str] = ...,
        gpt_model_sku_name: Optional[_builtins.str] = ...,
        gpt_model_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelCapacity")
    def embedding_model_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelName")
    def embedding_model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelSkuName")
    def embedding_model_sku_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelVersion")
    def embedding_model_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gptModelCapacity")
    def gpt_model_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gptModelName")
    def gpt_model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gptModelSkuName")
    def gpt_model_sku_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gptModelVersion")
    def gpt_model_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RedisProfileResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        capacity: Optional[_builtins.int] = ...,
        family: Optional[_builtins.str] = ...,
        size: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageProfileResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class UserManagedOpenAIProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        embedding_model_deployment_name: _builtins.str,
        embedding_model_type: _builtins.str,
        gpt_model_deployment_name: _builtins.str,
        id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelDeploymentName")
    def embedding_model_deployment_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelType")
    def embedding_model_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gptModelDeploymentName")
    def gpt_model_deployment_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
