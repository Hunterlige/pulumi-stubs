

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrivateLinkAssociationArgs', 'PrivateLinkAssociation']
@pulumi.input_type
class PrivateLinkAssociationArgs:
    def __init__(__self__, *, group_id: pulumi.Input[_builtins.str], pla_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[PrivateLinkAssociationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plaId")
    def pla_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pla_id.setter
    def pla_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[PrivateLinkAssociationPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[PrivateLinkAssociationPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:authorization:PrivateLinkAssociation")
class PrivateLinkAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., group_id: Optional[pulumi.Input[_builtins.str]] = ..., pla_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[PrivateLinkAssociationPropertiesArgs, PrivateLinkAssociationPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateLinkAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PrivateLinkAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.PrivateLinkAssociationPropertiesExpandedResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


