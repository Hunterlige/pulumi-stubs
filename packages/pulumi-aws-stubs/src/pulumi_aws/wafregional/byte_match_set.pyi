

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
__all__ = ['ByteMatchSetArgs', 'ByteMatchSet']
@pulumi.input_type
class ByteMatchSetArgs:
    def __init__(__self__, *, byte_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchTuples")
    def byte_match_tuples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]]:
        
        ...
    
    @byte_match_tuples.setter
    def byte_match_tuples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]]): # -> None:
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
class _ByteMatchSetState:
    def __init__(__self__, *, byte_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchTuples")
    def byte_match_tuples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]]:
        
        ...
    
    @byte_match_tuples.setter
    def byte_match_tuples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ByteMatchSetByteMatchTupleArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:wafregional/byteMatchSet:ByteMatchSet")
class ByteMatchSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., byte_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ByteMatchSetByteMatchTupleArgs, ByteMatchSetByteMatchTupleArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ByteMatchSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., byte_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ByteMatchSetByteMatchTupleArgs, ByteMatchSetByteMatchTupleArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ByteMatchSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchTuples")
    def byte_match_tuples(self) -> pulumi.Output[Optional[Sequence[outputs.ByteMatchSetByteMatchTuple]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


