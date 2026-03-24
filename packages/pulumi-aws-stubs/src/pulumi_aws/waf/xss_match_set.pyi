

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
__all__ = ['XssMatchSetArgs', 'XssMatchSet']
@pulumi.input_type
class XssMatchSetArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchTuples")
    def xss_match_tuples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]]:
        
        ...
    
    @xss_match_tuples.setter
    def xss_match_tuples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _XssMatchSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]] = ...) -> None:
        
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchTuples")
    def xss_match_tuples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]]:
        
        ...
    
    @xss_match_tuples.setter
    def xss_match_tuples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[XssMatchSetXssMatchTupleArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:waf/xssMatchSet:XssMatchSet")
class XssMatchSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[Union[XssMatchSetXssMatchTupleArgs, XssMatchSetXssMatchTupleArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[XssMatchSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., xss_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[Union[XssMatchSetXssMatchTupleArgs, XssMatchSetXssMatchTupleArgsDict]]]]] = ...) -> XssMatchSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchTuples")
    def xss_match_tuples(self) -> pulumi.Output[Optional[Sequence[outputs.XssMatchSetXssMatchTuple]]]:
        
        ...
    


