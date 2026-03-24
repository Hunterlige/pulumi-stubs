

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentPoolArgs', 'AgentPool']
@pulumi.input_type
class AgentPoolArgs:
    def __init__(__self__, *, count: pulumi.Input[_builtins.float], kubernetes_cluster_name: pulumi.Input[_builtins.str], mode: pulumi.Input[Union[_builtins.str, AgentPoolMode]], resource_group_name: pulumi.Input[_builtins.str], vm_sku_name: pulumi.Input[_builtins.str], administrator_configuration: Optional[pulumi.Input[AdministratorConfigurationArgs]] = ..., agent_options: Optional[pulumi.Input[AgentOptionsArgs]] = ..., agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., attached_network_configuration: Optional[pulumi.Input[AttachedNetworkConfigurationArgs]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., taints: Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]] = ..., upgrade_settings: Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @count.setter
    def count(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterName")
    def kubernetes_cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kubernetes_cluster_name.setter
    def kubernetes_cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[_builtins.str, AgentPoolMode]]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[Union[_builtins.str, AgentPoolMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSkuName")
    def vm_sku_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vm_sku_name.setter
    def vm_sku_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> Optional[pulumi.Input[AdministratorConfigurationArgs]]:
        
        ...
    
    @administrator_configuration.setter
    def administrator_configuration(self, value: Optional[pulumi.Input[AdministratorConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentOptions")
    def agent_options(self) -> Optional[pulumi.Input[AgentOptionsArgs]]:
        
        ...
    
    @agent_options.setter
    def agent_options(self, value: Optional[pulumi.Input[AgentOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedNetworkConfiguration")
    def attached_network_configuration(self) -> Optional[pulumi.Input[AttachedNetworkConfigurationArgs]]:
        
        ...
    
    @attached_network_configuration.setter
    def attached_network_configuration(self, value: Optional[pulumi.Input[AttachedNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[ExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]]:
        
        ...
    
    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KubernetesLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]]:
        
        ...
    
    @upgrade_settings.setter
    def upgrade_settings(self, value: Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:networkcloud:AgentPool")
class AgentPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., administrator_configuration: Optional[pulumi.Input[Union[AdministratorConfigurationArgs, AdministratorConfigurationArgsDict]]] = ..., agent_options: Optional[pulumi.Input[Union[AgentOptionsArgs, AgentOptionsArgsDict]]] = ..., agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., attached_network_configuration: Optional[pulumi.Input[Union[AttachedNetworkConfigurationArgs, AttachedNetworkConfigurationArgsDict]]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., count: Optional[pulumi.Input[_builtins.float]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., kubernetes_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[KubernetesLabelArgs, KubernetesLabelArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, AgentPoolMode]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., taints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[KubernetesLabelArgs, KubernetesLabelArgsDict]]]]] = ..., upgrade_settings: Optional[pulumi.Input[Union[AgentPoolUpgradeSettingsArgs, AgentPoolUpgradeSettingsArgsDict]]] = ..., vm_sku_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AgentPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> pulumi.Output[Optional[outputs.AdministratorConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentOptions")
    def agent_options(self) -> pulumi.Output[Optional[outputs.AgentOptionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedNetworkConfiguration")
    def attached_network_configuration(self) -> pulumi.Output[Optional[outputs.AttachedNetworkConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[outputs.KubernetesLabelResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
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
    def taints(self) -> pulumi.Output[Optional[Sequence[outputs.KubernetesLabelResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output[Optional[outputs.AgentPoolUpgradeSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSkuName")
    def vm_sku_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


