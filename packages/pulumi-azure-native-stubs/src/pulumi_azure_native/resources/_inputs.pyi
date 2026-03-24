

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ActionOnUnmanageArgs', 'ActionOnUnmanageArgsDict', 'ContainerConfigurationArgs', 'ContainerConfigurationArgsDict', 'ContainerGroupSubnetIdArgs', 'ContainerGroupSubnetIdArgsDict', 'DebugSettingArgs', 'DebugSettingArgsDict', 'DenySettingsArgs', 'DenySettingsArgsDict', 'DeploymentExtensionConfigItemArgs', 'DeploymentExtensionConfigItemArgsDict', 'DeploymentExternalInputDefinitionArgs', 'DeploymentExternalInputDefinitionArgsDict', 'DeploymentExternalInputArgs', 'DeploymentExternalInputArgsDict', 'DeploymentParameterArgs', 'DeploymentParameterArgsDict', 'DeploymentPropertiesArgs', 'DeploymentPropertiesArgsDict', 'DeploymentStacksDebugSettingArgs', 'DeploymentStacksDebugSettingArgsDict', 'DeploymentStacksParametersLinkArgs', 'DeploymentStacksParametersLinkArgsDict', 'DeploymentStacksTemplateLinkArgs', 'DeploymentStacksTemplateLinkArgsDict', 'DeploymentStacksWhatIfResultPropertiesArgs', 'DeploymentStacksWhatIfResultPropertiesArgsDict', 'EnvironmentVariableArgs', 'EnvironmentVariableArgsDict', 'ExpressionEvaluationOptionsArgs', 'ExpressionEvaluationOptionsArgsDict', 'ExtendedLocationArgs', 'ExtendedLocationArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'KeyVaultParameterReferenceArgs', 'KeyVaultParameterReferenceArgsDict', 'KeyVaultReferenceArgs', 'KeyVaultReferenceArgsDict', 'LinkedTemplateArtifactArgs', 'LinkedTemplateArtifactArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'OnErrorDeploymentArgs', 'OnErrorDeploymentArgsDict', 'ParametersLinkArgs', 'ParametersLinkArgsDict', 'PlanArgs', 'PlanArgsDict', 'SkuArgs', 'SkuArgsDict', 'StorageAccountConfigurationArgs', 'StorageAccountConfigurationArgsDict', 'TagsArgs', 'TagsArgsDict', 'TemplateLinkArgs', 'TemplateLinkArgsDict']
class ActionOnUnmanageArgsDict(TypedDict):
    
    resources: pulumi.Input[Union[_builtins.str, UnmanageActionResourceMode]]
    management_groups: NotRequired[pulumi.Input[Union[_builtins.str, UnmanageActionManagementGroupMode]]]
    resource_groups: NotRequired[pulumi.Input[Union[_builtins.str, UnmanageActionResourceGroupMode]]]
    resources_without_delete_support: NotRequired[pulumi.Input[Union[_builtins.str, ResourcesWithoutDeleteSupportAction]]]


@pulumi.input_type
class ActionOnUnmanageArgs:
    def __init__(__self__, *, resources: pulumi.Input[Union[_builtins.str, UnmanageActionResourceMode]], management_groups: Optional[pulumi.Input[Union[_builtins.str, UnmanageActionManagementGroupMode]]] = ..., resource_groups: Optional[pulumi.Input[Union[_builtins.str, UnmanageActionResourceGroupMode]]] = ..., resources_without_delete_support: Optional[pulumi.Input[Union[_builtins.str, ResourcesWithoutDeleteSupportAction]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Union[_builtins.str, UnmanageActionResourceMode]]:
        
        ...
    
    @resources.setter
    def resources(self, value: pulumi.Input[Union[_builtins.str, UnmanageActionResourceMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[pulumi.Input[Union[_builtins.str, UnmanageActionManagementGroupMode]]]:
        
        ...
    
    @management_groups.setter
    def management_groups(self, value: Optional[pulumi.Input[Union[_builtins.str, UnmanageActionManagementGroupMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[pulumi.Input[Union[_builtins.str, UnmanageActionResourceGroupMode]]]:
        
        ...
    
    @resource_groups.setter
    def resource_groups(self, value: Optional[pulumi.Input[Union[_builtins.str, UnmanageActionResourceGroupMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcesWithoutDeleteSupport")
    def resources_without_delete_support(self) -> Optional[pulumi.Input[Union[_builtins.str, ResourcesWithoutDeleteSupportAction]]]:
        
        ...
    
    @resources_without_delete_support.setter
    def resources_without_delete_support(self, value: Optional[pulumi.Input[Union[_builtins.str, ResourcesWithoutDeleteSupportAction]]]): # -> None:
        ...
    


class ContainerConfigurationArgsDict(TypedDict):
    
    container_group_name: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgsDict]]]]


@pulumi.input_type
class ContainerConfigurationArgs:
    def __init__(__self__, *, container_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerGroupName")
    def container_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_group_name.setter
    def container_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]]): # -> None:
        ...
    


class ContainerGroupSubnetIdArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContainerGroupSubnetIdArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DebugSettingArgsDict(TypedDict):
    
    detail_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DebugSettingArgs:
    def __init__(__self__, *, detail_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detail_level.setter
    def detail_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DenySettingsArgsDict(TypedDict):
    
    mode: pulumi.Input[Union[_builtins.str, DenySettingsMode]]
    apply_to_child_scopes: NotRequired[pulumi.Input[_builtins.bool]]
    excluded_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DenySettingsArgs:
    def __init__(__self__, *, mode: pulumi.Input[Union[_builtins.str, DenySettingsMode]], apply_to_child_scopes: Optional[pulumi.Input[_builtins.bool]] = ..., excluded_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., excluded_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[_builtins.str, DenySettingsMode]]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[Union[_builtins.str, DenySettingsMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyToChildScopes")
    def apply_to_child_scopes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_to_child_scopes.setter
    def apply_to_child_scopes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_actions.setter
    def excluded_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_principals.setter
    def excluded_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DeploymentExtensionConfigItemArgsDict(TypedDict):
    
    key_vault_reference: NotRequired[pulumi.Input[KeyVaultParameterReferenceArgsDict]]
    value: NotRequired[Any]


@pulumi.input_type
class DeploymentExtensionConfigItemArgs:
    def __init__(__self__, *, key_vault_reference: Optional[pulumi.Input[KeyVaultParameterReferenceArgs]] = ..., value: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> Optional[pulumi.Input[KeyVaultParameterReferenceArgs]]:
        
        ...
    
    @key_vault_reference.setter
    def key_vault_reference(self, value: Optional[pulumi.Input[KeyVaultParameterReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[Any]): # -> None:
        ...
    


class DeploymentExternalInputDefinitionArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    config: NotRequired[Any]


@pulumi.input_type
class DeploymentExternalInputDefinitionArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], config: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[Any]:
        
        ...
    
    @config.setter
    def config(self, value: Optional[Any]): # -> None:
        ...
    


class DeploymentExternalInputArgsDict(TypedDict):
    
    value: Any


@pulumi.input_type
class DeploymentExternalInputArgs:
    def __init__(__self__, *, value: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Any:
        
        ...
    
    @value.setter
    def value(self, value: Any): # -> None:
        ...
    


class DeploymentParameterArgsDict(TypedDict):
    
    expression: NotRequired[pulumi.Input[_builtins.str]]
    reference: NotRequired[pulumi.Input[KeyVaultParameterReferenceArgsDict]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[Any]


@pulumi.input_type
class DeploymentParameterArgs:
    def __init__(__self__, *, expression: Optional[pulumi.Input[_builtins.str]] = ..., reference: Optional[pulumi.Input[KeyVaultParameterReferenceArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input[KeyVaultParameterReferenceArgs]]:
        
        ...
    
    @reference.setter
    def reference(self, value: Optional[pulumi.Input[KeyVaultParameterReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[Any]): # -> None:
        ...
    


class DeploymentPropertiesArgsDict(TypedDict):
    
    mode: pulumi.Input[DeploymentMode]
    debug_setting: NotRequired[pulumi.Input[DebugSettingArgsDict]]
    expression_evaluation_options: NotRequired[pulumi.Input[ExpressionEvaluationOptionsArgsDict]]
    on_error_deployment: NotRequired[pulumi.Input[OnErrorDeploymentArgsDict]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgsDict]]]]
    parameters_link: NotRequired[pulumi.Input[ParametersLinkArgsDict]]
    template: NotRequired[Any]
    template_link: NotRequired[pulumi.Input[TemplateLinkArgsDict]]


@pulumi.input_type
class DeploymentPropertiesArgs:
    def __init__(__self__, *, mode: pulumi.Input[DeploymentMode], debug_setting: Optional[pulumi.Input[DebugSettingArgs]] = ..., expression_evaluation_options: Optional[pulumi.Input[ExpressionEvaluationOptionsArgs]] = ..., on_error_deployment: Optional[pulumi.Input[OnErrorDeploymentArgs]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]] = ..., parameters_link: Optional[pulumi.Input[ParametersLinkArgs]] = ..., template: Optional[Any] = ..., template_link: Optional[pulumi.Input[TemplateLinkArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[DeploymentMode]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[DeploymentMode]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> Optional[pulumi.Input[DebugSettingArgs]]:
        
        ...
    
    @debug_setting.setter
    def debug_setting(self, value: Optional[pulumi.Input[DebugSettingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionEvaluationOptions")
    def expression_evaluation_options(self) -> Optional[pulumi.Input[ExpressionEvaluationOptionsArgs]]:
        
        ...
    
    @expression_evaluation_options.setter
    def expression_evaluation_options(self, value: Optional[pulumi.Input[ExpressionEvaluationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onErrorDeployment")
    def on_error_deployment(self) -> Optional[pulumi.Input[OnErrorDeploymentArgs]]:
        
        ...
    
    @on_error_deployment.setter
    def on_error_deployment(self, value: Optional[pulumi.Input[OnErrorDeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> Optional[pulumi.Input[ParametersLinkArgs]]:
        
        ...
    
    @parameters_link.setter
    def parameters_link(self, value: Optional[pulumi.Input[ParametersLinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[Any]:
        
        ...
    
    @template.setter
    def template(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLink")
    def template_link(self) -> Optional[pulumi.Input[TemplateLinkArgs]]:
        
        ...
    
    @template_link.setter
    def template_link(self, value: Optional[pulumi.Input[TemplateLinkArgs]]): # -> None:
        ...
    


class DeploymentStacksDebugSettingArgsDict(TypedDict):
    
    detail_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentStacksDebugSettingArgs:
    def __init__(__self__, *, detail_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detail_level.setter
    def detail_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeploymentStacksParametersLinkArgsDict(TypedDict):
    
    uri: pulumi.Input[_builtins.str]
    content_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentStacksParametersLinkArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], content_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeploymentStacksTemplateLinkArgsDict(TypedDict):
    
    content_version: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    query_string: NotRequired[pulumi.Input[_builtins.str]]
    relative_path: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentStacksTemplateLinkArgs:
    def __init__(__self__, *, content_version: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., query_string: Optional[pulumi.Input[_builtins.str]] = ..., relative_path: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relative_path.setter
    def relative_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeploymentStacksWhatIfResultPropertiesArgsDict(TypedDict):
    
    action_on_unmanage: pulumi.Input[ActionOnUnmanageArgsDict]
    deny_settings: pulumi.Input[DenySettingsArgsDict]
    deployment_stack_resource_id: pulumi.Input[_builtins.str]
    retention_interval: pulumi.Input[_builtins.str]
    debug_setting: NotRequired[pulumi.Input[DeploymentStacksDebugSettingArgsDict]]
    deployment_scope: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    extension_configs: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[DeploymentExtensionConfigItemArgsDict]]]]]]
    external_input_definitions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputDefinitionArgsDict]]]]
    external_inputs: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputArgsDict]]]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgsDict]]]]
    parameters_link: NotRequired[pulumi.Input[DeploymentStacksParametersLinkArgsDict]]
    template: NotRequired[Any]
    template_link: NotRequired[pulumi.Input[DeploymentStacksTemplateLinkArgsDict]]
    validation_level: NotRequired[pulumi.Input[Union[_builtins.str, ValidationLevel]]]


@pulumi.input_type
class DeploymentStacksWhatIfResultPropertiesArgs:
    def __init__(__self__, *, action_on_unmanage: pulumi.Input[ActionOnUnmanageArgs], deny_settings: pulumi.Input[DenySettingsArgs], deployment_stack_resource_id: pulumi.Input[_builtins.str], retention_interval: pulumi.Input[_builtins.str], debug_setting: Optional[pulumi.Input[DeploymentStacksDebugSettingArgs]] = ..., deployment_scope: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., extension_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[DeploymentExtensionConfigItemArgs]]]]]] = ..., external_input_definitions: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputDefinitionArgs]]]] = ..., external_inputs: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputArgs]]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]] = ..., parameters_link: Optional[pulumi.Input[DeploymentStacksParametersLinkArgs]] = ..., template: Optional[Any] = ..., template_link: Optional[pulumi.Input[DeploymentStacksTemplateLinkArgs]] = ..., validation_level: Optional[pulumi.Input[Union[_builtins.str, ValidationLevel]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> pulumi.Input[ActionOnUnmanageArgs]:
        
        ...
    
    @action_on_unmanage.setter
    def action_on_unmanage(self, value: pulumi.Input[ActionOnUnmanageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> pulumi.Input[DenySettingsArgs]:
        
        ...
    
    @deny_settings.setter
    def deny_settings(self, value: pulumi.Input[DenySettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStackResourceId")
    def deployment_stack_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @deployment_stack_resource_id.setter
    def deployment_stack_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @retention_interval.setter
    def retention_interval(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> Optional[pulumi.Input[DeploymentStacksDebugSettingArgs]]:
        
        ...
    
    @debug_setting.setter
    def debug_setting(self, value: Optional[pulumi.Input[DeploymentStacksDebugSettingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_scope.setter
    def deployment_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionConfigs")
    def extension_configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[DeploymentExtensionConfigItemArgs]]]]]]:
        
        ...
    
    @extension_configs.setter
    def extension_configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[DeploymentExtensionConfigItemArgs]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalInputDefinitions")
    def external_input_definitions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputDefinitionArgs]]]]:
        
        ...
    
    @external_input_definitions.setter
    def external_input_definitions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalInputs")
    def external_inputs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputArgs]]]]:
        
        ...
    
    @external_inputs.setter
    def external_inputs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentExternalInputArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> Optional[pulumi.Input[DeploymentStacksParametersLinkArgs]]:
        
        ...
    
    @parameters_link.setter
    def parameters_link(self, value: Optional[pulumi.Input[DeploymentStacksParametersLinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[Any]:
        
        ...
    
    @template.setter
    def template(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLink")
    def template_link(self) -> Optional[pulumi.Input[DeploymentStacksTemplateLinkArgs]]:
        
        ...
    
    @template_link.setter
    def template_link(self, value: Optional[pulumi.Input[DeploymentStacksTemplateLinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[pulumi.Input[Union[_builtins.str, ValidationLevel]]]:
        
        ...
    
    @validation_level.setter
    def validation_level(self, value: Optional[pulumi.Input[Union[_builtins.str, ValidationLevel]]]): # -> None:
        ...
    


class EnvironmentVariableArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    secure_value: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], secure_value: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureValue")
    def secure_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secure_value.setter
    def secure_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExpressionEvaluationOptionsArgsDict(TypedDict):
    
    scope: NotRequired[pulumi.Input[Union[_builtins.str, ExpressionEvaluationOptionsScopeType]]]


@pulumi.input_type
class ExpressionEvaluationOptionsArgs:
    def __init__(__self__, *, scope: Optional[pulumi.Input[Union[_builtins.str, ExpressionEvaluationOptionsScopeType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[_builtins.str, ExpressionEvaluationOptionsScopeType]]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Union[_builtins.str, ExpressionEvaluationOptionsScopeType]]]): # -> None:
        ...
    


class ExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]] = ...) -> None:
        
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
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class KeyVaultParameterReferenceArgsDict(TypedDict):
    
    key_vault: pulumi.Input[KeyVaultReferenceArgsDict]
    secret_name: pulumi.Input[_builtins.str]
    secret_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultParameterReferenceArgs:
    def __init__(__self__, *, key_vault: pulumi.Input[KeyVaultReferenceArgs], secret_name: pulumi.Input[_builtins.str], secret_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Input[KeyVaultReferenceArgs]:
        
        ...
    
    @key_vault.setter
    def key_vault(self, value: pulumi.Input[KeyVaultReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyVaultReferenceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class KeyVaultReferenceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LinkedTemplateArtifactArgsDict(TypedDict):
    
    path: pulumi.Input[_builtins.str]
    template: Any


@pulumi.input_type
class LinkedTemplateArtifactArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], template: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Any:
        
        ...
    
    @template.setter
    def template(self, value: Any): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OnErrorDeploymentArgsDict(TypedDict):
    
    deployment_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[OnErrorDeploymentType]]


@pulumi.input_type
class OnErrorDeploymentArgs:
    def __init__(__self__, *, deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[OnErrorDeploymentType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[OnErrorDeploymentType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[OnErrorDeploymentType]]): # -> None:
        ...
    


class ParametersLinkArgsDict(TypedDict):
    
    uri: pulumi.Input[_builtins.str]
    content_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ParametersLinkArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], content_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PlanArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.str]]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., product: Optional[pulumi.Input[_builtins.str]] = ..., promotion_code: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def product(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageAccountConfigurationArgsDict(TypedDict):
    
    storage_account_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StorageAccountConfigurationArgs:
    def __init__(__self__, *, storage_account_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_key.setter
    def storage_account_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TagsArgsDict(TypedDict):
    
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TagsArgs:
    def __init__(__self__, *, tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TemplateLinkArgsDict(TypedDict):
    
    content_version: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    query_string: NotRequired[pulumi.Input[_builtins.str]]
    relative_path: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateLinkArgs:
    def __init__(__self__, *, content_version: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., query_string: Optional[pulumi.Input[_builtins.str]] = ..., relative_path: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relative_path.setter
    def relative_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


