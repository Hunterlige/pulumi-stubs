

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
__all__ = ['BmcKeySetArgs', 'BmcKeySet']
@pulumi.input_type
class BmcKeySetArgs:
    def __init__(__self__, *, azure_group_id: pulumi.Input[_builtins.str], cluster_name: pulumi.Input[_builtins.str], expiration: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationArgs], privilege_level: pulumi.Input[Union[_builtins.str, BmcKeySetPrivilegeLevel]], resource_group_name: pulumi.Input[_builtins.str], user_list: pulumi.Input[Sequence[pulumi.Input[KeySetUserArgs]]], bmc_key_set_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @azure_group_id.setter
    def azure_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> pulumi.Input[Union[_builtins.str, BmcKeySetPrivilegeLevel]]:
        
        ...
    
    @privilege_level.setter
    def privilege_level(self, value: pulumi.Input[Union[_builtins.str, BmcKeySetPrivilegeLevel]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userList")
    def user_list(self) -> pulumi.Input[Sequence[pulumi.Input[KeySetUserArgs]]]:
        
        ...
    
    @user_list.setter
    def user_list(self, value: pulumi.Input[Sequence[pulumi.Input[KeySetUserArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcKeySetName")
    def bmc_key_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bmc_key_set_name.setter
    def bmc_key_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("azure-native:networkcloud:BmcKeySet")
class BmcKeySet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_group_id: Optional[pulumi.Input[_builtins.str]] = ..., bmc_key_set_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., privilege_level: Optional[pulumi.Input[Union[_builtins.str, BmcKeySetPrivilegeLevel]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_list: Optional[pulumi.Input[Sequence[pulumi.Input[Union[KeySetUserArgs, KeySetUserArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BmcKeySetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BmcKeySet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def expiration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastValidation")
    def last_validation(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> pulumi.Output[_builtins.str]:
        
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
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userList")
    def user_list(self) -> pulumi.Output[Sequence[outputs.KeySetUserResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userListStatus")
    def user_list_status(self) -> pulumi.Output[Sequence[outputs.KeySetUserStatusResponse]]:
        
        ...
    


