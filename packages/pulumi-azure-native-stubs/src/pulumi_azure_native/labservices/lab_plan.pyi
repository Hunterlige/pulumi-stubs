

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
__all__ = ['LabPlanArgs', 'LabPlan']
@pulumi.input_type
class LabPlanArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_auto_shutdown_profile: Optional[pulumi.Input[AutoShutdownProfileArgs]] = ..., default_connection_profile: Optional[pulumi.Input[ConnectionProfileArgs]] = ..., default_network_profile: Optional[pulumi.Input[LabPlanNetworkProfileArgs]] = ..., identity: Optional[pulumi.Input[IdentityArgs]] = ..., lab_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., linked_lms_instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., shared_gallery_id: Optional[pulumi.Input[_builtins.str]] = ..., support_info: Optional[pulumi.Input[SupportInfoArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_regions.setter
    def allowed_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(self) -> Optional[pulumi.Input[AutoShutdownProfileArgs]]:
        
        ...
    
    @default_auto_shutdown_profile.setter
    def default_auto_shutdown_profile(self, value: Optional[pulumi.Input[AutoShutdownProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(self) -> Optional[pulumi.Input[ConnectionProfileArgs]]:
        
        ...
    
    @default_connection_profile.setter
    def default_connection_profile(self, value: Optional[pulumi.Input[ConnectionProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(self) -> Optional[pulumi.Input[LabPlanNetworkProfileArgs]]:
        
        ...
    
    @default_network_profile.setter
    def default_network_profile(self, value: Optional[pulumi.Input[LabPlanNetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labPlanName")
    def lab_plan_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lab_plan_name.setter
    def lab_plan_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @linked_lms_instance.setter
    def linked_lms_instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_gallery_id.setter
    def shared_gallery_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> Optional[pulumi.Input[SupportInfoArgs]]:
        
        ...
    
    @support_info.setter
    def support_info(self, value: Optional[pulumi.Input[SupportInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:labservices:LabPlan")
class LabPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_auto_shutdown_profile: Optional[pulumi.Input[Union[AutoShutdownProfileArgs, AutoShutdownProfileArgsDict]]] = ..., default_connection_profile: Optional[pulumi.Input[Union[ConnectionProfileArgs, ConnectionProfileArgsDict]]] = ..., default_network_profile: Optional[pulumi.Input[Union[LabPlanNetworkProfileArgs, LabPlanNetworkProfileArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ..., lab_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., linked_lms_instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., shared_gallery_id: Optional[pulumi.Input[_builtins.str]] = ..., support_info: Optional[pulumi.Input[Union[SupportInfoArgs, SupportInfoArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LabPlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LabPlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(self) -> pulumi.Output[Optional[outputs.AutoShutdownProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(self) -> pulumi.Output[Optional[outputs.ConnectionProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(self) -> pulumi.Output[Optional[outputs.LabPlanNetworkProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> pulumi.Output[outputs.ResourceOperationErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> pulumi.Output[Optional[outputs.SupportInfoResponse]]:
        
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
    


