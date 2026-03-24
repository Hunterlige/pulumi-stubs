

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StudioSessionMappingArgs', 'StudioSessionMapping']
@pulumi.input_type
class StudioSessionMappingArgs:
    def __init__(__self__, *, identity_type: pulumi.Input[_builtins.str], session_policy_arn: pulumi.Input[_builtins.str], studio_id: pulumi.Input[_builtins.str], identity_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicyArn")
    def session_policy_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @session_policy_arn.setter
    def session_policy_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @studio_id.setter
    def studio_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_name.setter
    def identity_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StudioSessionMappingState:
    def __init__(__self__, *, identity_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_name: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., session_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., studio_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_id.setter
    def identity_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_name.setter
    def identity_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicyArn")
    def session_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_policy_arn.setter
    def session_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @studio_id.setter
    def studio_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:emr/studioSessionMapping:StudioSessionMapping")
class StudioSessionMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., identity_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_name: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., session_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., studio_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StudioSessionMappingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., identity_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_name: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., session_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., studio_id: Optional[pulumi.Input[_builtins.str]] = ...) -> StudioSessionMapping:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicyArn")
    def session_policy_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


