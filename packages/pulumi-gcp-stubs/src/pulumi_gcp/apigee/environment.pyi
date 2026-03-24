

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
__all__ = ['EnvironmentArgs', 'Environment']
@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *, org_id: pulumi.Input[_builtins.str], api_proxy_type: Optional[pulumi.Input[_builtins.str]] = ..., client_ip_resolution_config: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]] = ..., deployment_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., forward_proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[EnvironmentNodeConfigArgs]] = ..., properties: Optional[pulumi.Input[EnvironmentPropertiesArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_proxy_type.setter
    def api_proxy_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIpResolutionConfig")
    def client_ip_resolution_config(self) -> Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]]:
        
        ...
    
    @client_ip_resolution_config.setter
    def client_ip_resolution_config(self, value: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProxyUri")
    def forward_proxy_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forward_proxy_uri.setter
    def forward_proxy_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[EnvironmentNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[EnvironmentNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[EnvironmentPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[EnvironmentPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EnvironmentState:
    def __init__(__self__, *, api_proxy_type: Optional[pulumi.Input[_builtins.str]] = ..., client_ip_resolution_config: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]] = ..., deployment_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., forward_proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[EnvironmentNodeConfigArgs]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[EnvironmentPropertiesArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_proxy_type.setter
    def api_proxy_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIpResolutionConfig")
    def client_ip_resolution_config(self) -> Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]]:
        
        ...
    
    @client_ip_resolution_config.setter
    def client_ip_resolution_config(self, value: Optional[pulumi.Input[EnvironmentClientIpResolutionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProxyUri")
    def forward_proxy_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forward_proxy_uri.setter
    def forward_proxy_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[EnvironmentNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[EnvironmentNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[EnvironmentPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[EnvironmentPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/environment:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_proxy_type: Optional[pulumi.Input[_builtins.str]] = ..., client_ip_resolution_config: Optional[pulumi.Input[Union[EnvironmentClientIpResolutionConfigArgs, EnvironmentClientIpResolutionConfigArgsDict]]] = ..., deployment_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., forward_proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[EnvironmentNodeConfigArgs, EnvironmentNodeConfigArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[EnvironmentPropertiesArgs, EnvironmentPropertiesArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EnvironmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_proxy_type: Optional[pulumi.Input[_builtins.str]] = ..., client_ip_resolution_config: Optional[pulumi.Input[Union[EnvironmentClientIpResolutionConfigArgs, EnvironmentClientIpResolutionConfigArgsDict]]] = ..., deployment_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., forward_proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[EnvironmentNodeConfigArgs, EnvironmentNodeConfigArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[EnvironmentPropertiesArgs, EnvironmentPropertiesArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> Environment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIpResolutionConfig")
    def client_ip_resolution_config(self) -> pulumi.Output[Optional[outputs.EnvironmentClientIpResolutionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProxyUri")
    def forward_proxy_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.EnvironmentNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[outputs.EnvironmentProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


