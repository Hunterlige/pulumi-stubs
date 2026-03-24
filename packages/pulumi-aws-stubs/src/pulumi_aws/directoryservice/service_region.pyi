

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServiceRegionArgs', 'ServiceRegion']
@pulumi.input_type
class ServiceRegionArgs:
    def __init__(__self__, *, directory_id: pulumi.Input[_builtins.str], region_name: pulumi.Input[_builtins.str], vpc_settings: pulumi.Input[ServiceRegionVpcSettingsArgs], desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> pulumi.Input[ServiceRegionVpcSettingsArgs]:
        
        ...
    
    @vpc_settings.setter
    def vpc_settings(self, value: pulumi.Input[ServiceRegionVpcSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_number_of_domain_controllers.setter
    def desired_number_of_domain_controllers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceRegionState:
    def __init__(__self__, *, desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_settings: Optional[pulumi.Input[ServiceRegionVpcSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_number_of_domain_controllers.setter
    def desired_number_of_domain_controllers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> Optional[pulumi.Input[ServiceRegionVpcSettingsArgs]]:
        
        ...
    
    @vpc_settings.setter
    def vpc_settings(self, value: Optional[pulumi.Input[ServiceRegionVpcSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:directoryservice/serviceRegion:ServiceRegion")
class ServiceRegion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_settings: Optional[pulumi.Input[Union[ServiceRegionVpcSettingsArgs, ServiceRegionVpcSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceRegionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_settings: Optional[pulumi.Input[Union[ServiceRegionVpcSettingsArgs, ServiceRegionVpcSettingsArgsDict]]] = ...) -> ServiceRegion:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> pulumi.Output[outputs.ServiceRegionVpcSettings]:
        
        ...
    


