

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
__all__ = ['GalleryInVMAccessControlProfileVersionArgs', 'GalleryInVMAccessControlProfileVersion']
@pulumi.input_type
class GalleryInVMAccessControlProfileVersionArgs:
    def __init__(__self__, *, default_access: pulumi.Input[Union[_builtins.str, EndpointAccess]], gallery_name: pulumi.Input[_builtins.str], in_vm_access_control_profile_name: pulumi.Input[_builtins.str], mode: pulumi.Input[Union[_builtins.str, AccessControlRulesMode]], resource_group_name: pulumi.Input[_builtins.str], exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., in_vm_access_control_profile_version_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[AccessControlRulesArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_locations: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAccess")
    def default_access(self) -> pulumi.Input[Union[_builtins.str, EndpointAccess]]:
        
        ...
    
    @default_access.setter
    def default_access(self, value: pulumi.Input[Union[_builtins.str, EndpointAccess]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inVMAccessControlProfileName")
    def in_vm_access_control_profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @in_vm_access_control_profile_name.setter
    def in_vm_access_control_profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[_builtins.str, AccessControlRulesMode]]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[Union[_builtins.str, AccessControlRulesMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inVMAccessControlProfileVersionName")
    def in_vm_access_control_profile_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_vm_access_control_profile_version_name.setter
    def in_vm_access_control_profile_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[AccessControlRulesArgs]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[AccessControlRulesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocations")
    def target_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]:
        
        ...
    
    @target_locations.setter
    def target_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class GalleryInVMAccessControlProfileVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_access: Optional[pulumi.Input[Union[_builtins.str, EndpointAccess]]] = ..., exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., in_vm_access_control_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., in_vm_access_control_profile_version_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, AccessControlRulesMode]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Union[AccessControlRulesArgs, AccessControlRulesArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_locations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TargetRegionArgs, TargetRegionArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GalleryInVMAccessControlProfileVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> GalleryInVMAccessControlProfileVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAccess")
    def default_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter(name="publishedDate")
    def published_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> pulumi.Output[outputs.ReplicationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[outputs.AccessControlRulesResponse]]:
        
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
    @pulumi.getter(name="targetLocations")
    def target_locations(self) -> pulumi.Output[Optional[Sequence[outputs.TargetRegionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


