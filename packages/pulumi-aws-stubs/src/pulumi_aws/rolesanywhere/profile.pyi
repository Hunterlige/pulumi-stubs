

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProfileArgs', 'Profile']
@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *, accept_role_session_name: Optional[pulumi.Input[_builtins.bool]] = ..., duration_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., require_instance_properties: Optional[pulumi.Input[_builtins.bool]] = ..., role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., session_policy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptRoleSessionName")
    def accept_role_session_name(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @accept_role_session_name.setter
    def accept_role_session_name(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration_seconds.setter
    def duration_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @managed_policy_arns.setter
    def managed_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInstanceProperties")
    def require_instance_properties(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_instance_properties.setter
    def require_instance_properties(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArns")
    def role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @role_arns.setter
    def role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicy")
    def session_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_policy.setter
    def session_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ProfileState:
    def __init__(__self__, *, accept_role_session_name: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., duration_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., require_instance_properties: Optional[pulumi.Input[_builtins.bool]] = ..., role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., session_policy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptRoleSessionName")
    def accept_role_session_name(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @accept_role_session_name.setter
    def accept_role_session_name(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @duration_seconds.setter
    def duration_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @managed_policy_arns.setter
    def managed_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInstanceProperties")
    def require_instance_properties(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_instance_properties.setter
    def require_instance_properties(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArns")
    def role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @role_arns.setter
    def role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicy")
    def session_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_policy.setter
    def session_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:rolesanywhere/profile:Profile")
class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accept_role_session_name: Optional[pulumi.Input[_builtins.bool]] = ..., duration_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., require_instance_properties: Optional[pulumi.Input[_builtins.bool]] = ..., role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., session_policy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ProfileArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accept_role_session_name: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., duration_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., require_instance_properties: Optional[pulumi.Input[_builtins.bool]] = ..., role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., session_policy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Profile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptRoleSessionName")
    def accept_role_session_name(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInstanceProperties")
    def require_instance_properties(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArns")
    def role_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPolicy")
    def session_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


