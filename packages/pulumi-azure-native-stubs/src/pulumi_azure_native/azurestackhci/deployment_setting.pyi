

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentSettingArgs', 'DeploymentSetting']
@pulumi.input_type
class DeploymentSettingArgs:
    def __init__(__self__, *, arc_node_resource_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cluster_name: pulumi.Input[_builtins.str], deployment_configuration: pulumi.Input[DeploymentConfigurationArgs], deployment_mode: pulumi.Input[Union[_builtins.str, DeploymentMode]], resource_group_name: pulumi.Input[_builtins.str], deployment_settings_name: Optional[pulumi.Input[_builtins.str]] = ..., operation_type: Optional[pulumi.Input[Union[_builtins.str, OperationType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @arc_node_resource_ids.setter
    def arc_node_resource_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> pulumi.Input[DeploymentConfigurationArgs]:
        
        ...
    
    @deployment_configuration.setter
    def deployment_configuration(self, value: pulumi.Input[DeploymentConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Input[Union[_builtins.str, DeploymentMode]]:
        
        ...
    
    @deployment_mode.setter
    def deployment_mode(self, value: pulumi.Input[Union[_builtins.str, DeploymentMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentSettingsName")
    def deployment_settings_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_settings_name.setter
    def deployment_settings_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OperationType]]]:
        
        ...
    
    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OperationType]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:DeploymentSetting")
class DeploymentSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arc_node_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_configuration: Optional[pulumi.Input[Union[DeploymentConfigurationArgs, DeploymentConfigurationArgsDict]]] = ..., deployment_mode: Optional[pulumi.Input[Union[_builtins.str, DeploymentMode]]] = ..., deployment_settings_name: Optional[pulumi.Input[_builtins.str]] = ..., operation_type: Optional[pulumi.Input[Union[_builtins.str, OperationType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeploymentSettingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DeploymentSetting:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> pulumi.Output[outputs.DeploymentConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> pulumi.Output[outputs.EceReportedPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


