

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionCommitmentArgs', 'RegionCommitment']
@pulumi.input_type
class RegionCommitmentArgs:
    def __init__(__self__, *, plan: pulumi.Input[_builtins.str], auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., category: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., existing_reservations: Optional[pulumi.Input[_builtins.str]] = ..., license_resource: Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plan.setter
    def plan(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingReservations")
    def existing_reservations(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @existing_reservations.setter
    def existing_reservations(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseResource")
    def license_resource(self) -> Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]]:
        
        ...
    
    @license_resource.setter
    def license_resource(self, value: Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionCommitmentState:
    def __init__(__self__, *, auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., category: Optional[pulumi.Input[_builtins.str]] = ..., commitment_id: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., existing_reservations: Optional[pulumi.Input[_builtins.str]] = ..., license_resource: Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plan: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., start_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_message: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentId")
    def commitment_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @commitment_id.setter
    def commitment_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimestamp")
    def end_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_timestamp.setter
    def end_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingReservations")
    def existing_reservations(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @existing_reservations.setter
    def existing_reservations(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseResource")
    def license_resource(self) -> Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]]:
        
        ...
    
    @license_resource.setter
    def license_resource(self, value: Optional[pulumi.Input[RegionCommitmentLicenseResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionCommitmentResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimestamp")
    def start_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_timestamp.setter
    def start_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/regionCommitment:RegionCommitment")
class RegionCommitment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., category: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., existing_reservations: Optional[pulumi.Input[_builtins.str]] = ..., license_resource: Optional[pulumi.Input[Union[RegionCommitmentLicenseResourceArgs, RegionCommitmentLicenseResourceArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plan: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionCommitmentResourceArgs, RegionCommitmentResourceArgsDict]]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionCommitmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., auto_renew: Optional[pulumi.Input[_builtins.bool]] = ..., category: Optional[pulumi.Input[_builtins.str]] = ..., commitment_id: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., existing_reservations: Optional[pulumi.Input[_builtins.str]] = ..., license_resource: Optional[pulumi.Input[Union[RegionCommitmentLicenseResourceArgs, RegionCommitmentLicenseResourceArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plan: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionCommitmentResourceArgs, RegionCommitmentResourceArgsDict]]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., start_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_message: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> RegionCommitment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentId")
    def commitment_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimestamp")
    def end_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingReservations")
    def existing_reservations(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseResource")
    def license_resource(self) -> pulumi.Output[Optional[outputs.RegionCommitmentLicenseResource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[outputs.RegionCommitmentResource]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimestamp")
    def start_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


