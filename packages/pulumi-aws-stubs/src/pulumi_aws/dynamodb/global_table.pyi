

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
__all__ = ['GlobalTableArgs', 'GlobalTable']
@pulumi.input_type
class GlobalTableArgs:
    def __init__(__self__, *, replicas: pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]]): # -> None:
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
class _GlobalTableState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]]] = ...) -> None:
        
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GlobalTableReplicaArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:dynamodb/globalTable:GlobalTable")
class GlobalTable(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GlobalTableReplicaArgs, GlobalTableReplicaArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GlobalTableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GlobalTableReplicaArgs, GlobalTableReplicaArgsDict]]]]] = ...) -> GlobalTable:
        
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
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Sequence[outputs.GlobalTableReplica]]:
        
        ...
    


