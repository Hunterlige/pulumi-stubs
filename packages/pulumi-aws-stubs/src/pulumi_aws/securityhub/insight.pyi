

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
__all__ = ['InsightArgs', 'Insight']
@pulumi.input_type
class InsightArgs:
    def __init__(__self__, *, filters: pulumi.Input[InsightFiltersArgs], group_by_attribute: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Input[InsightFiltersArgs]:
        
        ...
    
    @filters.setter
    def filters(self, value: pulumi.Input[InsightFiltersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByAttribute")
    def group_by_attribute(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_by_attribute.setter
    def group_by_attribute(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InsightState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[InsightFiltersArgs]] = ..., group_by_attribute: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[InsightFiltersArgs]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[InsightFiltersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByAttribute")
    def group_by_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_by_attribute.setter
    def group_by_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:securityhub/insight:Insight")
class Insight(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., filters: Optional[pulumi.Input[Union[InsightFiltersArgs, InsightFiltersArgsDict]]] = ..., group_by_attribute: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InsightArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Union[InsightFiltersArgs, InsightFiltersArgsDict]]] = ..., group_by_attribute: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Insight:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Output[outputs.InsightFilters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByAttribute")
    def group_by_attribute(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


