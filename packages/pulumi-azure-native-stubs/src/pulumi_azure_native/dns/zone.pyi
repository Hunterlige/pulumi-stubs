

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
__all__ = ['ZoneArgs', 'Zone']
@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], location: Optional[pulumi.Input[_builtins.str]] = ..., registration_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., resolution_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone_name: Optional[pulumi.Input[_builtins.str]] = ..., zone_type: Optional[pulumi.Input[ZoneType]] = ...) -> None:
        
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @registration_virtual_networks.setter
    def registration_virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @resolution_virtual_networks.setter
    def resolution_virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> Optional[pulumi.Input[ZoneType]]:
        
        ...
    
    @zone_type.setter
    def zone_type(self, value: Optional[pulumi.Input[ZoneType]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:dns:Zone")
class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., registration_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]]] = ..., resolution_virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone_name: Optional[pulumi.Input[_builtins.str]] = ..., zone_type: Optional[pulumi.Input[ZoneType]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ZoneArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Zone:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNumberOfRecordsPerRecordSet")
    def max_number_of_records_per_record_set(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(self) -> pulumi.Output[Optional[Sequence[outputs.SubResourceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(self) -> pulumi.Output[Optional[Sequence[outputs.SubResourceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingKeys")
    def signing_keys(self) -> pulumi.Output[Sequence[outputs.SigningKeyResponse]]:
        
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
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


