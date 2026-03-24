

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentStackAtResourceGroupArgs', 'DeploymentStackAtResourceGroup']
@pulumi.input_type
class DeploymentStackAtResourceGroupArgs:
    def __init__(__self__, *, action_on_unmanage: pulumi.Input[ActionOnUnmanageArgs], deny_settings: pulumi.Input[DenySettingsArgs], resource_group_name: pulumi.Input[_builtins.str], bypass_stack_out_of_sync_error: Optional[pulumi.Input[_builtins.bool]] = ..., debug_setting: Optional[pulumi.Input[DeploymentStacksDebugSettingArgs]] = ..., deployment_scope: Optional[pulumi.Input[_builtins.str]] = ..., deployment_stack_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[DeploymentParameterArgs]]]] = ..., parameters_link: Optional[pulumi.Input[DeploymentStacksParametersLinkArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template: Optional[Any] = ..., template_link: Optional[pulumi.Input[DeploymentStacksTemplateLinkArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassStackOutOfSyncError")
    def bypass_stack_out_of_sync_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bypass_stack_out_of_sync_error.setter
    def bypass_stack_out_of_sync_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="deploymentStackName")
    def deployment_stack_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_stack_name.setter
    def deployment_stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    


@pulumi.type_token(...)
class DeploymentStackAtResourceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action_on_unmanage: Optional[pulumi.Input[Union[ActionOnUnmanageArgs, ActionOnUnmanageArgsDict]]] = ..., bypass_stack_out_of_sync_error: Optional[pulumi.Input[_builtins.bool]] = ..., debug_setting: Optional[pulumi.Input[Union[DeploymentStacksDebugSettingArgs, DeploymentStacksDebugSettingArgsDict]]] = ..., deny_settings: Optional[pulumi.Input[Union[DenySettingsArgs, DenySettingsArgsDict]]] = ..., deployment_scope: Optional[pulumi.Input[_builtins.str]] = ..., deployment_stack_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[DeploymentParameterArgs, DeploymentParameterArgsDict]]]]] = ..., parameters_link: Optional[pulumi.Input[Union[DeploymentStacksParametersLinkArgs, DeploymentStacksParametersLinkArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template: Optional[Any] = ..., template_link: Optional[pulumi.Input[Union[DeploymentStacksTemplateLinkArgs, DeploymentStacksTemplateLinkArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeploymentStackAtResourceGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DeploymentStackAtResourceGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> pulumi.Output[outputs.ActionOnUnmanageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> pulumi.Output[Optional[outputs.DeploymentStacksDebugSettingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletedResources")
    def deleted_resources(self) -> pulumi.Output[Sequence[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> pulumi.Output[outputs.DenySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detachedResources")
    def detached_resources(self) -> pulumi.Output[Sequence[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> pulumi.Output[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failedResources")
    def failed_resources(self) -> pulumi.Output[Sequence[outputs.ResourceReferenceExtendedResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, outputs.DeploymentParameterResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> pulumi.Output[Optional[outputs.DeploymentStacksParametersLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.ManagedResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


