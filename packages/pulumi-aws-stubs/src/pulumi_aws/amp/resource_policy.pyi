

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
__all__ = ['ResourcePolicyArgs', 'ResourcePolicy']
@pulumi.input_type
class ResourcePolicyArgs:
    def __init__(__self__, *, policy_document: pulumi.Input[_builtins.str], workspace_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourcePolicyState:
    def __init__(__self__, *, policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ResourcePolicyTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:amp/resourcePolicy:ResourcePolicy")
class ResourcePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ResourcePolicyTimeoutsArgs, ResourcePolicyTimeoutsArgsDict]]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourcePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ResourcePolicyTimeoutsArgs, ResourcePolicyTimeoutsArgsDict]]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ResourcePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ResourcePolicyTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


