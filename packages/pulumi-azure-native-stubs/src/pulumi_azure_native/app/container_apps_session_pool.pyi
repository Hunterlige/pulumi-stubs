

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
__all__ = ['ContainerAppsSessionPoolArgs', 'ContainerAppsSessionPool']
@pulumi.input_type
class ContainerAppsSessionPoolArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], container_type: Optional[pulumi.Input[Union[_builtins.str, ContainerType]]] = ..., custom_container_template: Optional[pulumi.Input[CustomContainerTemplateArgs]] = ..., dynamic_pool_configuration: Optional[pulumi.Input[DynamicPoolConfigurationArgs]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_identity_settings: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedIdentitySettingArgs]]]] = ..., pool_management_type: Optional[pulumi.Input[Union[_builtins.str, PoolManagementType]]] = ..., scale_configuration: Optional[pulumi.Input[ScaleConfigurationArgs]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[SessionPoolSecretArgs]]]] = ..., session_network_configuration: Optional[pulumi.Input[SessionNetworkConfigurationArgs]] = ..., session_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ContainerType]]]:
        
        ...
    
    @container_type.setter
    def container_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ContainerType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContainerTemplate")
    def custom_container_template(self) -> Optional[pulumi.Input[CustomContainerTemplateArgs]]:
        
        ...
    
    @custom_container_template.setter
    def custom_container_template(self, value: Optional[pulumi.Input[CustomContainerTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicPoolConfiguration")
    def dynamic_pool_configuration(self) -> Optional[pulumi.Input[DynamicPoolConfigurationArgs]]:
        
        ...
    
    @dynamic_pool_configuration.setter
    def dynamic_pool_configuration(self, value: Optional[pulumi.Input[DynamicPoolConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentitySettings")
    def managed_identity_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedIdentitySettingArgs]]]]:
        
        ...
    
    @managed_identity_settings.setter
    def managed_identity_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedIdentitySettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolManagementType")
    def pool_management_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PoolManagementType]]]:
        
        ...
    
    @pool_management_type.setter
    def pool_management_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PoolManagementType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleConfiguration")
    def scale_configuration(self) -> Optional[pulumi.Input[ScaleConfigurationArgs]]:
        
        ...
    
    @scale_configuration.setter
    def scale_configuration(self, value: Optional[pulumi.Input[ScaleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SessionPoolSecretArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SessionPoolSecretArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionNetworkConfiguration")
    def session_network_configuration(self) -> Optional[pulumi.Input[SessionNetworkConfigurationArgs]]:
        
        ...
    
    @session_network_configuration.setter
    def session_network_configuration(self, value: Optional[pulumi.Input[SessionNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPoolName")
    def session_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_pool_name.setter
    def session_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:ContainerAppsSessionPool")
class ContainerAppsSessionPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., container_type: Optional[pulumi.Input[Union[_builtins.str, ContainerType]]] = ..., custom_container_template: Optional[pulumi.Input[Union[CustomContainerTemplateArgs, CustomContainerTemplateArgsDict]]] = ..., dynamic_pool_configuration: Optional[pulumi.Input[Union[DynamicPoolConfigurationArgs, DynamicPoolConfigurationArgsDict]]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_identity_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagedIdentitySettingArgs, ManagedIdentitySettingArgsDict]]]]] = ..., pool_management_type: Optional[pulumi.Input[Union[_builtins.str, PoolManagementType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scale_configuration: Optional[pulumi.Input[Union[ScaleConfigurationArgs, ScaleConfigurationArgsDict]]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SessionPoolSecretArgs, SessionPoolSecretArgsDict]]]]] = ..., session_network_configuration: Optional[pulumi.Input[Union[SessionNetworkConfigurationArgs, SessionNetworkConfigurationArgsDict]]] = ..., session_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContainerAppsSessionPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ContainerAppsSessionPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContainerTemplate")
    def custom_container_template(self) -> pulumi.Output[Optional[outputs.CustomContainerTemplateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicPoolConfiguration")
    def dynamic_pool_configuration(self) -> pulumi.Output[Optional[outputs.DynamicPoolConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentitySettings")
    def managed_identity_settings(self) -> pulumi.Output[Optional[Sequence[outputs.ManagedIdentitySettingResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolManagementEndpoint")
    def pool_management_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolManagementType")
    def pool_management_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleConfiguration")
    def scale_configuration(self) -> pulumi.Output[Optional[outputs.ScaleConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Output[Optional[Sequence[outputs.SessionPoolSecretResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionNetworkConfiguration")
    def session_network_configuration(self) -> pulumi.Output[Optional[outputs.SessionNetworkConfigurationResponse]]:
        
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
    


