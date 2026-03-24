

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SqlVirtualMachineGroupArgs', 'SqlVirtualMachineGroup']
@pulumi.input_type
class SqlVirtualMachineGroupArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], location: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_offer: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_sku: Optional[pulumi.Input[Union[_builtins.str, SqlVmGroupImageSku]]] = ..., sql_virtual_machine_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wsfc_domain_profile: Optional[pulumi.Input[WsfcDomainProfileArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_image_offer.setter
    def sql_image_offer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlVmGroupImageSku]]]:
        
        ...
    
    @sql_image_sku.setter
    def sql_image_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlVmGroupImageSku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineGroupName")
    def sql_virtual_machine_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_virtual_machine_group_name.setter
    def sql_virtual_machine_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> Optional[pulumi.Input[WsfcDomainProfileArgs]]:
        
        ...
    
    @wsfc_domain_profile.setter
    def wsfc_domain_profile(self, value: Optional[pulumi.Input[WsfcDomainProfileArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SqlVirtualMachineGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_offer: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_sku: Optional[pulumi.Input[Union[_builtins.str, SqlVmGroupImageSku]]] = ..., sql_virtual_machine_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wsfc_domain_profile: Optional[pulumi.Input[Union[WsfcDomainProfileArgs, WsfcDomainProfileArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SqlVirtualMachineGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SqlVirtualMachineGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfiguration")
    def cluster_configuration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagerType")
    def cluster_manager_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> pulumi.Output[Optional[outputs.WsfcDomainProfileResponse]]:
        
        ...
    


