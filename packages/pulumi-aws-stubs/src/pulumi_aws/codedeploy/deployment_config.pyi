

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentConfigArgs', 'DeploymentConfig']
@pulumi.input_type
class DeploymentConfigArgs:
    def __init__(__self__, *, compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., minimum_healthy_hosts: Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_routing_config: Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]] = ..., zonal_config: Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_platform.setter
    def compute_platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_config_name.setter
    def deployment_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyHosts")
    def minimum_healthy_hosts(self) -> Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]]:
        
        ...
    
    @minimum_healthy_hosts.setter
    def minimum_healthy_hosts(self, value: Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficRoutingConfig")
    def traffic_routing_config(self) -> Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]]:
        
        ...
    
    @traffic_routing_config.setter
    def traffic_routing_config(self, value: Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalConfig")
    def zonal_config(self) -> Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]]:
        
        ...
    
    @zonal_config.setter
    def zonal_config(self, value: Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DeploymentConfigState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., minimum_healthy_hosts: Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_routing_config: Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]] = ..., zonal_config: Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_platform.setter
    def compute_platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigId")
    def deployment_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_config_id.setter
    def deployment_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_config_name.setter
    def deployment_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyHosts")
    def minimum_healthy_hosts(self) -> Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]]:
        
        ...
    
    @minimum_healthy_hosts.setter
    def minimum_healthy_hosts(self, value: Optional[pulumi.Input[DeploymentConfigMinimumHealthyHostsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficRoutingConfig")
    def traffic_routing_config(self) -> Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]]:
        
        ...
    
    @traffic_routing_config.setter
    def traffic_routing_config(self, value: Optional[pulumi.Input[DeploymentConfigTrafficRoutingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalConfig")
    def zonal_config(self) -> Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]]:
        
        ...
    
    @zonal_config.setter
    def zonal_config(self, value: Optional[pulumi.Input[DeploymentConfigZonalConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:codedeploy/deploymentConfig:DeploymentConfig")
class DeploymentConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., minimum_healthy_hosts: Optional[pulumi.Input[Union[DeploymentConfigMinimumHealthyHostsArgs, DeploymentConfigMinimumHealthyHostsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_routing_config: Optional[pulumi.Input[Union[DeploymentConfigTrafficRoutingConfigArgs, DeploymentConfigTrafficRoutingConfigArgsDict]]] = ..., zonal_config: Optional[pulumi.Input[Union[DeploymentConfigZonalConfigArgs, DeploymentConfigZonalConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DeploymentConfigArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_platform: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_config_name: Optional[pulumi.Input[_builtins.str]] = ..., minimum_healthy_hosts: Optional[pulumi.Input[Union[DeploymentConfigMinimumHealthyHostsArgs, DeploymentConfigMinimumHealthyHostsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_routing_config: Optional[pulumi.Input[Union[DeploymentConfigTrafficRoutingConfigArgs, DeploymentConfigTrafficRoutingConfigArgsDict]]] = ..., zonal_config: Optional[pulumi.Input[Union[DeploymentConfigZonalConfigArgs, DeploymentConfigZonalConfigArgsDict]]] = ...) -> DeploymentConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigId")
    def deployment_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyHosts")
    def minimum_healthy_hosts(self) -> pulumi.Output[Optional[outputs.DeploymentConfigMinimumHealthyHosts]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficRoutingConfig")
    def traffic_routing_config(self) -> pulumi.Output[Optional[outputs.DeploymentConfigTrafficRoutingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalConfig")
    def zonal_config(self) -> pulumi.Output[Optional[outputs.DeploymentConfigZonalConfig]]:
        
        ...
    


