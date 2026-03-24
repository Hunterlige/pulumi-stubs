

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
__all__ = ['DevBoxDefinitionArgs', 'DevBoxDefinition']
@pulumi.input_type
class DevBoxDefinitionArgs:
    def __init__(__self__, *, dev_center_name: pulumi.Input[_builtins.str], image_reference: pulumi.Input[ImageReferenceArgs], resource_group_name: pulumi.Input[_builtins.str], sku: pulumi.Input[SkuArgs], dev_box_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., hibernate_support: Optional[pulumi.Input[Union[_builtins.str, HibernateSupport]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., os_storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Input[ImageReferenceArgs]:
        
        ...
    
    @image_reference.setter
    def image_reference(self, value: pulumi.Input[ImageReferenceArgs]): # -> None:
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
    def sku(self) -> pulumi.Input[SkuArgs]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dev_box_definition_name.setter
    def dev_box_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernateSupport")
    def hibernate_support(self) -> Optional[pulumi.Input[Union[_builtins.str, HibernateSupport]]]:
        
        ...
    
    @hibernate_support.setter
    def hibernate_support(self, value: Optional[pulumi.Input[Union[_builtins.str, HibernateSupport]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @os_storage_type.setter
    def os_storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:devcenter:DevBoxDefinition")
class DevBoxDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dev_box_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_center_name: Optional[pulumi.Input[_builtins.str]] = ..., hibernate_support: Optional[pulumi.Input[Union[_builtins.str, HibernateSupport]]] = ..., image_reference: Optional[pulumi.Input[Union[ImageReferenceArgs, ImageReferenceArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., os_storage_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DevBoxDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DevBoxDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeImageReference")
    def active_image_reference(self) -> pulumi.Output[outputs.ImageReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernateSupport")
    def hibernate_support(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Output[outputs.ImageReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageValidationErrorDetails")
    def image_validation_error_details(self) -> pulumi.Output[outputs.ImageValidationErrorDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageValidationStatus")
    def image_validation_status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]:
        
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
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


