

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
__all__ = ['OptInArgs', 'OptIn']
@pulumi.input_type
class OptInArgs:
    def __init__(__self__, *, conditions: Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_datas: Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]]:
        
        ...
    
    @principals.setter
    def principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDatas")
    def resource_datas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]]:
        
        ...
    
    @resource_datas.setter
    def resource_datas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _OptInState:
    def __init__(__self__, *, conditions: Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_by: Optional[pulumi.Input[_builtins.str]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_datas: Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @last_updated_by.setter
    def last_updated_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]]:
        
        ...
    
    @principals.setter
    def principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInPrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDatas")
    def resource_datas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]]:
        
        ...
    
    @resource_datas.setter
    def resource_datas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OptInResourceDataArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:lakeformation/optIn:OptIn")
class OptIn(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInConditionArgs, OptInConditionArgsDict]]]]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInPrincipalArgs, OptInPrincipalArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_datas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInResourceDataArgs, OptInResourceDataArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[OptInArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInConditionArgs, OptInConditionArgsDict]]]]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_by: Optional[pulumi.Input[_builtins.str]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInPrincipalArgs, OptInPrincipalArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_datas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OptInResourceDataArgs, OptInResourceDataArgsDict]]]]] = ...) -> OptIn:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Optional[Sequence[outputs.OptInCondition]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> pulumi.Output[Optional[Sequence[outputs.OptInPrincipal]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDatas")
    def resource_datas(self) -> pulumi.Output[Optional[Sequence[outputs.OptInResourceData]]]:
        
        ...
    


