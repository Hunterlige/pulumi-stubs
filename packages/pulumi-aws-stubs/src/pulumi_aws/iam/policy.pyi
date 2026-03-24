

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, policy: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]], delay_after_policy_creation_in_ms: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]:
        
        ...
    
    @policy.setter
    def policy(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delayAfterPolicyCreationInMs")
    def delay_after_policy_creation_in_ms(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @delay_after_policy_creation_in_ms.setter
    def delay_after_policy_creation_in_ms(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., attachment_count: Optional[pulumi.Input[_builtins.int]] = ..., delay_after_policy_creation_in_ms: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentCount")
    def attachment_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @attachment_count.setter
    def attachment_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delayAfterPolicyCreationInMs")
    def delay_after_policy_creation_in_ms(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @delay_after_policy_creation_in_ms.setter
    def delay_after_policy_creation_in_ms(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:iam/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delay_after_policy_creation_in_ms: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., attachment_count: Optional[pulumi.Input[_builtins.int]] = ..., delay_after_policy_creation_in_ms: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentCount")
    def attachment_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delayAfterPolicyCreationInMs")
    def delay_after_policy_creation_in_ms(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


