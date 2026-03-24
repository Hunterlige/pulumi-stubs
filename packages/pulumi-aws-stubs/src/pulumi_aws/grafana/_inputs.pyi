

import builtins as _builtins
import sys
import pulumi
from typing import Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkspaceNetworkAccessControlArgs', 'WorkspaceNetworkAccessControlArgsDict', 'WorkspaceVpcConfigurationArgs', 'WorkspaceVpcConfigurationArgsDict']
class WorkspaceNetworkAccessControlArgsDict(TypedDict):
    prefix_list_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpce_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class WorkspaceNetworkAccessControlArgs:
    def __init__(__self__, *, prefix_list_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vpce_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @prefix_list_ids.setter
    def prefix_list_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @vpce_ids.setter
    def vpce_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class WorkspaceVpcConfigurationArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class WorkspaceVpcConfigurationArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


