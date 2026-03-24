

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
__all__ = ['GeoMatchSetArgs', 'GeoMatchSet']
@pulumi.input_type
class GeoMatchSetArgs:
    def __init__(__self__, *, geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchConstraints")
    def geo_match_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]]:
        
        ...
    
    @geo_match_constraints.setter
    def geo_match_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GeoMatchSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchConstraints")
    def geo_match_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]]:
        
        ...
    
    @geo_match_constraints.setter
    def geo_match_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeoMatchSetGeoMatchConstraintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:waf/geoMatchSet:GeoMatchSet")
class GeoMatchSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GeoMatchSetGeoMatchConstraintArgs, GeoMatchSetGeoMatchConstraintArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[GeoMatchSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., geo_match_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GeoMatchSetGeoMatchConstraintArgs, GeoMatchSetGeoMatchConstraintArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> GeoMatchSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchConstraints")
    def geo_match_constraints(self) -> pulumi.Output[Optional[Sequence[outputs.GeoMatchSetGeoMatchConstraint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


