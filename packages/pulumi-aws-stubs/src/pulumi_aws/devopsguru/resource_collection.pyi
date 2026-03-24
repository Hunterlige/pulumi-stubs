

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourceCollectionArgs', 'ResourceCollection']
@pulumi.input_type
class ResourceCollectionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], cloudformation: Optional[pulumi.Input[ResourceCollectionCloudformationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[ResourceCollectionTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cloudformation(self) -> Optional[pulumi.Input[ResourceCollectionCloudformationArgs]]:
        
        ...
    
    @cloudformation.setter
    def cloudformation(self, value: Optional[pulumi.Input[ResourceCollectionCloudformationArgs]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[ResourceCollectionTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[ResourceCollectionTagsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourceCollectionState:
    def __init__(__self__, *, cloudformation: Optional[pulumi.Input[ResourceCollectionCloudformationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[ResourceCollectionTagsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cloudformation(self) -> Optional[pulumi.Input[ResourceCollectionCloudformationArgs]]:
        
        ...
    
    @cloudformation.setter
    def cloudformation(self, value: Optional[pulumi.Input[ResourceCollectionCloudformationArgs]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[ResourceCollectionTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[ResourceCollectionTagsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ResourceCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloudformation: Optional[pulumi.Input[Union[ResourceCollectionCloudformationArgs, ResourceCollectionCloudformationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Union[ResourceCollectionTagsArgs, ResourceCollectionTagsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourceCollectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cloudformation: Optional[pulumi.Input[Union[ResourceCollectionCloudformationArgs, ResourceCollectionCloudformationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Union[ResourceCollectionTagsArgs, ResourceCollectionTagsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> ResourceCollection:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cloudformation(self) -> pulumi.Output[Optional[outputs.ResourceCollectionCloudformation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[outputs.ResourceCollectionTags]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


