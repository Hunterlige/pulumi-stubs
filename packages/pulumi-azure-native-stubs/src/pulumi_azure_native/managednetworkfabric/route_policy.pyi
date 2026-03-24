

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
__all__ = ['RoutePolicyArgs', 'RoutePolicy']
@pulumi.input_type
class RoutePolicyArgs:
    def __init__(__self__, *, network_fabric_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], statements: pulumi.Input[Sequence[pulumi.Input[RoutePolicyStatementPropertiesArgs]]], address_family_type: Optional[pulumi.Input[Union[_builtins.str, AddressFamilyType]]] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., default_action: Optional[pulumi.Input[Union[_builtins.str, CommunityActionTypes]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., route_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_fabric_id.setter
    def network_fabric_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> pulumi.Input[Sequence[pulumi.Input[RoutePolicyStatementPropertiesArgs]]]:
        
        ...
    
    @statements.setter
    def statements(self, value: pulumi.Input[Sequence[pulumi.Input[RoutePolicyStatementPropertiesArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamilyType")
    def address_family_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AddressFamilyType]]]:
        
        ...
    
    @address_family_type.setter
    def address_family_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AddressFamilyType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[_builtins.str, CommunityActionTypes]]]:
        
        ...
    
    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[_builtins.str, CommunityActionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routePolicyName")
    def route_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_policy_name.setter
    def route_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:managednetworkfabric:RoutePolicy")
class RoutePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_family_type: Optional[pulumi.Input[Union[_builtins.str, AddressFamilyType]]] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., default_action: Optional[pulumi.Input[Union[_builtins.str, CommunityActionTypes]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_fabric_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., statements: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoutePolicyStatementPropertiesArgs, RoutePolicyStatementPropertiesArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RoutePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RoutePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamilyType")
    def address_family_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> pulumi.Output[Sequence[outputs.RoutePolicyStatementPropertiesResponse]]:
        
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
    


