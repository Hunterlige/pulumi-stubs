import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ActionOnUnmanageResponse",
    "ActionOnUnmanageResponseV1",
    "ActionOnUnmanageResponseV2",
    "ActionOnUnmanageResponseV3",
    "AliasPathMetadataResponse",
    "AliasPathResponse",
    "AliasPatternResponse",
    "AliasResponse",
    "ApiProfileResponse",
    "BasicDependencyResponse",
    "ContainerConfigurationResponse",
    "ContainerGroupSubnetIdResponse",
    "DebugSettingResponse",
    "DenySettingsResponse",
    "DependencyResponse",
    "DeploymentExtensionConfigItemResponse",
    "DeploymentExtensionResponse",
    "DeploymentParameterResponse",
    "DeploymentPropertiesExtendedResponse",
    "DeploymentStacksDebugSettingResponse",
    "DeploymentStacksDiagnosticResponse",
    "DeploymentStacksParametersLinkResponse",
    "DeploymentStacksWhatIfChangeResponse",
    ...,
    ...,
    "DeploymentStacksWhatIfPropertyChangeResponse",
    "DeploymentStacksWhatIfResourceChangeResponse",
    ...,
    ...,
    ...,
    "DeploymentStacksWhatIfResultPropertiesResponse",
    "DeploymentStacksWhatIfResultPropertiesResponseV1",
    "DeploymentStacksWhatIfResultPropertiesResponseV2",
    "EnvironmentVariableResponse",
    "ErrorAdditionalInfoResponse",
    "ErrorDetailResponse",
    "ErrorResponseResponse",
    "ExtendedLocationResponse",
    "IdentityResponse",
    "IdentityResponseUserAssignedIdentities",
    "KeyVaultParameterReferenceResponse",
    "KeyVaultReferenceResponse",
    "LinkedTemplateArtifactResponse",
    "ManagedResourceReferenceResponse",
    "ManagedServiceIdentityResponse",
    "OnErrorDeploymentExtendedResponse",
    "ParametersLinkResponse",
    "PlanResponse",
    "ProviderExtendedLocationResponse",
    "ProviderResourceTypeResponse",
    "ProviderResponse",
    "ResourceGroupPropertiesResponse",
    "ResourceReferenceExtendedResponse",
    "ResourceReferenceResponse",
    "ScriptStatusResponse",
    "SkuResponse",
    "StorageAccountConfigurationResponse",
    "SystemDataResponse",
    "TagsResponse",
    "TemplateLinkResponse",
    "TemplateSpecVersionInfoResponse",
    "UserAssignedIdentityResponse",
    "ZoneMappingResponse",
]

@pulumi.output_type
class ActionOnUnmanageResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: _builtins.str,
        management_groups: Optional[_builtins.str] = ...,
        resource_groups: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ActionOnUnmanageResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: _builtins.str,
        management_groups: Optional[_builtins.str] = ...,
        resource_groups: Optional[_builtins.str] = ...,
        resources_without_delete_support: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcesWithoutDeleteSupport")
    def resources_without_delete_support(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ActionOnUnmanageResponseV2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: _builtins.str,
        management_groups: Optional[_builtins.str] = ...,
        resource_groups: Optional[_builtins.str] = ...,
        resources_without_delete_support: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcesWithoutDeleteSupport")
    def resources_without_delete_support(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ActionOnUnmanageResponseV3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: _builtins.str,
        management_groups: Optional[_builtins.str] = ...,
        resource_groups: Optional[_builtins.str] = ...,
        resources_without_delete_support: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcesWithoutDeleteSupport")
    def resources_without_delete_support(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AliasPathMetadataResponse(dict):
    def __init__(
        __self__, *, attributes: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AliasPathResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata: outputs.AliasPathMetadataResponse,
        api_versions: Optional[Sequence[_builtins.str]] = ...,
        path: Optional[_builtins.str] = ...,
        pattern: Optional[outputs.AliasPatternResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.AliasPathMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[outputs.AliasPatternResponse]: ...

@pulumi.output_type
class AliasPatternResponse(dict):
    def __init__(
        __self__,
        *,
        phrase: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        variable: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def phrase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def variable(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AliasResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_metadata: outputs.AliasPathMetadataResponse,
        default_path: Optional[_builtins.str] = ...,
        default_pattern: Optional[outputs.AliasPatternResponse] = ...,
        name: Optional[_builtins.str] = ...,
        paths: Optional[Sequence[outputs.AliasPathResponse]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultMetadata")
    def default_metadata(self) -> outputs.AliasPathMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="defaultPath")
    def default_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultPattern")
    def default_pattern(self) -> Optional[outputs.AliasPatternResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[outputs.AliasPathResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_version: _builtins.str, profile_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> _builtins.str: ...

@pulumi.output_type
class BasicDependencyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
        resource_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_group_name: Optional[_builtins.str] = ...,
        subnet_ids: Optional[Sequence[outputs.ContainerGroupSubnetIdResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerGroupName")
    def container_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[Sequence[outputs.ContainerGroupSubnetIdResponse]]: ...

@pulumi.output_type
class ContainerGroupSubnetIdResponse(dict):
    def __init__(
        __self__, *, id: _builtins.str, name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DebugSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, detail_level: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DenySettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: _builtins.str,
        apply_to_child_scopes: Optional[_builtins.bool] = ...,
        excluded_actions: Optional[Sequence[_builtins.str]] = ...,
        excluded_principals: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applyToChildScopes")
    def apply_to_child_scopes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DependencyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        depends_on: Optional[Sequence[outputs.BasicDependencyResponse]] = ...,
        id: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
        resource_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[outputs.BasicDependencyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentExtensionConfigItemResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        key_vault_reference: Optional[outputs.KeyVaultParameterReferenceResponse] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(
        self,
    ) -> Optional[outputs.KeyVaultParameterReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

@pulumi.output_type
class DeploymentExtensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        version: _builtins.str,
        config: Optional[
            Mapping[str, outputs.DeploymentExtensionConfigItemResponse]
        ] = ...,
        config_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> Optional[Mapping[str, outputs.DeploymentExtensionConfigItemResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentParameterResponse(dict):
    def __init__(
        __self__,
        *,
        reference: Optional[outputs.KeyVaultParameterReferenceResponse] = ...,
        type: Optional[_builtins.str] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[outputs.KeyVaultParameterReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

@pulumi.output_type
class DeploymentPropertiesExtendedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        correlation_id: _builtins.str,
        debug_setting: outputs.DebugSettingResponse,
        dependencies: Sequence[outputs.DependencyResponse],
        duration: _builtins.str,
        error: outputs.ErrorResponseResponse,
        mode: _builtins.str,
        on_error_deployment: outputs.OnErrorDeploymentExtendedResponse,
        output_resources: Sequence[outputs.ResourceReferenceResponse],
        outputs: Any,
        parameters: Any,
        parameters_link: outputs.ParametersLinkResponse,
        providers: Sequence[outputs.ProviderResponse],
        provisioning_state: _builtins.str,
        template_hash: _builtins.str,
        template_link: outputs.TemplateLinkResponse,
        timestamp: _builtins.str,
        validated_resources: Sequence[outputs.ResourceReferenceResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> outputs.DebugSettingResponse: ...
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Sequence[outputs.DependencyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorResponseResponse: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onErrorDeployment")
    def on_error_deployment(self) -> outputs.OnErrorDeploymentExtendedResponse: ...
    @_builtins.property
    @pulumi.getter(name="outputResources")
    def output_resources(self) -> Sequence[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> outputs.ParametersLinkResponse: ...
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Sequence[outputs.ProviderResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="templateHash")
    def template_hash(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="templateLink")
    def template_link(self) -> outputs.TemplateLinkResponse: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validatedResources")
    def validated_resources(self) -> Sequence[outputs.ResourceReferenceResponse]: ...

@pulumi.output_type
class DeploymentStacksDebugSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, detail_level: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksDiagnosticResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        level: _builtins.str,
        message: _builtins.str,
        additional_info: Optional[Sequence[outputs.ErrorAdditionalInfoResponse]] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(
        self,
    ) -> Optional[Sequence[outputs.ErrorAdditionalInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksParametersLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, content_version: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfChangeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deny_settings_change: outputs.DeploymentStacksWhatIfChangeResponseDenySettingsChange,
        resource_changes: Sequence[
            outputs.DeploymentStacksWhatIfResourceChangeResponse
        ],
        deployment_scope_change: Optional[
            outputs.DeploymentStacksWhatIfChangeResponseDeploymentScopeChange
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="denySettingsChange")
    def deny_settings_change(
        self,
    ) -> outputs.DeploymentStacksWhatIfChangeResponseDenySettingsChange: ...
    @_builtins.property
    @pulumi.getter(name="resourceChanges")
    def resource_changes(
        self,
    ) -> Sequence[outputs.DeploymentStacksWhatIfResourceChangeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentScopeChange")
    def deployment_scope_change(
        self,
    ) -> Optional[
        outputs.DeploymentStacksWhatIfChangeResponseDeploymentScopeChange
    ]: ...

@pulumi.output_type
class DeploymentStacksWhatIfChangeResponseDenySettingsChange(dict):
    def __init__(
        __self__,
        *,
        after: Optional[outputs.DenySettingsResponse] = ...,
        before: Optional[outputs.DenySettingsResponse] = ...,
        delta: Optional[
            Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[outputs.DenySettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[outputs.DenySettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def delta(
        self,
    ) -> Optional[Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]]: ...

@pulumi.output_type
class DeploymentStacksWhatIfChangeResponseDeploymentScopeChange(dict):
    def __init__(
        __self__,
        *,
        after: Optional[_builtins.str] = ...,
        before: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfPropertyChangeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        change_type: _builtins.str,
        path: _builtins.str,
        after: Optional[Any] = ...,
        before: Optional[Any] = ...,
        children: Optional[
            Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def children(
        self,
    ) -> Optional[Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResourceChangeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_version: _builtins.str,
        change_certainty: _builtins.str,
        change_type: _builtins.str,
        extension: outputs.DeploymentExtensionResponse,
        id: _builtins.str,
        identifiers: Any,
        type: _builtins.str,
        deny_status_change: Optional[
            outputs.DeploymentStacksWhatIfResourceChangeResponseDenyStatusChange
        ] = ...,
        deployment_id: Optional[_builtins.str] = ...,
        management_status_change: Optional[
            outputs.DeploymentStacksWhatIfResourceChangeResponseManagementStatusChange
        ] = ...,
        resource_configuration_changes: Optional[
            outputs.DeploymentStacksWhatIfResourceChangeResponseResourceConfigurationChanges
        ] = ...,
        symbolic_name: Optional[_builtins.str] = ...,
        unsupported_reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="changeCertainty")
    def change_certainty(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def extension(self) -> outputs.DeploymentExtensionResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denyStatusChange")
    def deny_status_change(
        self,
    ) -> Optional[
        outputs.DeploymentStacksWhatIfResourceChangeResponseDenyStatusChange
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementStatusChange")
    def management_status_change(
        self,
    ) -> Optional[
        outputs.DeploymentStacksWhatIfResourceChangeResponseManagementStatusChange
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationChanges")
    def resource_configuration_changes(
        self,
    ) -> Optional[
        outputs.DeploymentStacksWhatIfResourceChangeResponseResourceConfigurationChanges
    ]: ...
    @_builtins.property
    @pulumi.getter(name="symbolicName")
    def symbolic_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unsupportedReason")
    def unsupported_reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResourceChangeResponseDenyStatusChange(dict):
    def __init__(
        __self__,
        *,
        after: Optional[_builtins.str] = ...,
        before: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResourceChangeResponseManagementStatusChange(dict):
    def __init__(
        __self__,
        *,
        after: Optional[_builtins.str] = ...,
        before: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResourceChangeResponseResourceConfigurationChanges(dict):
    def __init__(
        __self__,
        *,
        after: Optional[Any] = ...,
        before: Optional[Any] = ...,
        delta: Optional[
            Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def before(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def delta(
        self,
    ) -> Optional[Sequence[outputs.DeploymentStacksWhatIfPropertyChangeResponse]]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResultPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_on_unmanage: outputs.ActionOnUnmanageResponseV1,
        changes: outputs.DeploymentStacksWhatIfChangeResponse,
        correlation_id: _builtins.str,
        deny_settings: outputs.DenySettingsResponse,
        deployment_stack_last_modified: _builtins.str,
        deployment_stack_resource_id: _builtins.str,
        diagnostics: Sequence[outputs.DeploymentStacksDiagnosticResponse],
        error: outputs.ErrorDetailResponse,
        provisioning_state: _builtins.str,
        retention_interval: _builtins.str,
        debug_setting: Optional[outputs.DeploymentStacksDebugSettingResponse] = ...,
        deployment_scope: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, outputs.DeploymentParameterResponse]] = ...,
        parameters_link: Optional[outputs.DeploymentStacksParametersLinkResponse] = ...,
        validation_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> outputs.ActionOnUnmanageResponseV1: ...
    @_builtins.property
    @pulumi.getter
    def changes(self) -> outputs.DeploymentStacksWhatIfChangeResponse: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> outputs.DenySettingsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackLastModified")
    def deployment_stack_last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackResourceId")
    def deployment_stack_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Sequence[outputs.DeploymentStacksDiagnosticResponse]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(
        self,
    ) -> Optional[outputs.DeploymentStacksDebugSettingResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Mapping[str, outputs.DeploymentParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(
        self,
    ) -> Optional[outputs.DeploymentStacksParametersLinkResponse]: ...
    @_builtins.property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResultPropertiesResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_on_unmanage: outputs.ActionOnUnmanageResponseV2,
        changes: outputs.DeploymentStacksWhatIfChangeResponse,
        correlation_id: _builtins.str,
        deny_settings: outputs.DenySettingsResponse,
        deployment_stack_last_modified: _builtins.str,
        deployment_stack_resource_id: _builtins.str,
        diagnostics: Sequence[outputs.DeploymentStacksDiagnosticResponse],
        error: outputs.ErrorDetailResponse,
        provisioning_state: _builtins.str,
        retention_interval: _builtins.str,
        debug_setting: Optional[outputs.DeploymentStacksDebugSettingResponse] = ...,
        deployment_scope: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, outputs.DeploymentParameterResponse]] = ...,
        parameters_link: Optional[outputs.DeploymentStacksParametersLinkResponse] = ...,
        validation_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> outputs.ActionOnUnmanageResponseV2: ...
    @_builtins.property
    @pulumi.getter
    def changes(self) -> outputs.DeploymentStacksWhatIfChangeResponse: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> outputs.DenySettingsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackLastModified")
    def deployment_stack_last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackResourceId")
    def deployment_stack_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Sequence[outputs.DeploymentStacksDiagnosticResponse]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(
        self,
    ) -> Optional[outputs.DeploymentStacksDebugSettingResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Mapping[str, outputs.DeploymentParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(
        self,
    ) -> Optional[outputs.DeploymentStacksParametersLinkResponse]: ...
    @_builtins.property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentStacksWhatIfResultPropertiesResponseV2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_on_unmanage: outputs.ActionOnUnmanageResponseV3,
        changes: outputs.DeploymentStacksWhatIfChangeResponse,
        correlation_id: _builtins.str,
        deny_settings: outputs.DenySettingsResponse,
        deployment_stack_last_modified: _builtins.str,
        deployment_stack_resource_id: _builtins.str,
        diagnostics: Sequence[outputs.DeploymentStacksDiagnosticResponse],
        error: outputs.ErrorDetailResponse,
        provisioning_state: _builtins.str,
        retention_interval: _builtins.str,
        debug_setting: Optional[outputs.DeploymentStacksDebugSettingResponse] = ...,
        deployment_scope: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, outputs.DeploymentParameterResponse]] = ...,
        parameters_link: Optional[outputs.DeploymentStacksParametersLinkResponse] = ...,
        validation_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> outputs.ActionOnUnmanageResponseV3: ...
    @_builtins.property
    @pulumi.getter
    def changes(self) -> outputs.DeploymentStacksWhatIfChangeResponse: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> outputs.DenySettingsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackLastModified")
    def deployment_stack_last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStackResourceId")
    def deployment_stack_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Sequence[outputs.DeploymentStacksDiagnosticResponse]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(
        self,
    ) -> Optional[outputs.DeploymentStacksDebugSettingResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Mapping[str, outputs.DeploymentParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(
        self,
    ) -> Optional[outputs.DeploymentStacksParametersLinkResponse]: ...
    @_builtins.property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentVariableResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        secure_value: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secureValue")
    def secure_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorResponseResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorResponseResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class ExtendedLocationResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.IdentityResponseUserAssignedIdentities]
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
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.IdentityResponseUserAssignedIdentities]]: ...

@pulumi.output_type
class IdentityResponseUserAssignedIdentities(dict):
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
class KeyVaultParameterReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault: outputs.KeyVaultReferenceResponse,
        secret_name: _builtins.str,
        secret_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> outputs.KeyVaultReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultReferenceResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class LinkedTemplateArtifactResponse(dict):
    def __init__(__self__, *, path: _builtins.str, template: Any) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Any: ...

@pulumi.output_type
class ManagedResourceReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        deny_status: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denyStatus")
    def deny_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class OnErrorDeploymentExtendedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        deployment_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ParametersLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, content_version: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        product: Optional[_builtins.str] = ...,
        promotion_code: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProviderExtendedLocationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extended_locations: Optional[Sequence[_builtins.str]] = ...,
        location: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProviderResourceTypeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_profiles: Sequence[outputs.ApiProfileResponse],
        default_api_version: _builtins.str,
        aliases: Optional[Sequence[outputs.AliasResponse]] = ...,
        api_versions: Optional[Sequence[_builtins.str]] = ...,
        capabilities: Optional[_builtins.str] = ...,
        location_mappings: Optional[
            Sequence[outputs.ProviderExtendedLocationResponse]
        ] = ...,
        locations: Optional[Sequence[_builtins.str]] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        resource_type: Optional[_builtins.str] = ...,
        zone_mappings: Optional[Sequence[outputs.ZoneMappingResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiProfiles")
    def api_profiles(self) -> Sequence[outputs.ApiProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultApiVersion")
    def default_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[Sequence[outputs.AliasResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationMappings")
    def location_mappings(
        self,
    ) -> Optional[Sequence[outputs.ProviderExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneMappings")
    def zone_mappings(self) -> Optional[Sequence[outputs.ZoneMappingResponse]]: ...

@pulumi.output_type
class ProviderResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        registration_policy: _builtins.str,
        registration_state: _builtins.str,
        resource_types: Sequence[outputs.ProviderResourceTypeResponse],
        namespace: Optional[_builtins.str] = ...,
        provider_authorization_consent_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registrationPolicy")
    def registration_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registrationState")
    def registration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[outputs.ProviderResourceTypeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorizationConsentState")
    def provider_authorization_consent_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceGroupPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, provisioning_state: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceReferenceExtendedResponse(dict):
    def __init__(
        __self__, *, error: outputs.ErrorDetailResponse, id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceReferenceResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ScriptStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_instance_id: _builtins.str,
        end_time: _builtins.str,
        expiration_time: _builtins.str,
        start_time: _builtins.str,
        storage_account_id: _builtins.str,
        error: Optional[outputs.ErrorResponseResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerInstanceId")
    def container_instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorResponseResponse]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: Optional[_builtins.int] = ...,
        family: Optional[_builtins.str] = ...,
        model: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        size: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageAccountConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_account_key: Optional[_builtins.str] = ...,
        storage_account_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...

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
class TagsResponse(dict):
    def __init__(
        __self__, *, tags: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class TemplateLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_version: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        query_string: Optional[_builtins.str] = ...,
        relative_path: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateSpecVersionInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        time_created: _builtins.str,
        time_modified: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> _builtins.str: ...

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
class ZoneMappingResponse(dict):
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...
