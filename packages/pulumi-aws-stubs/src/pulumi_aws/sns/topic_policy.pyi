

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TopicPolicyArgs', 'TopicPolicy']
@pulumi.input_type
class TopicPolicyArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], policy: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]:
        
        ...
    
    @policy.setter
    def policy(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TopicPolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sns/topicPolicy:TopicPolicy")
class TopicPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TopicPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> TopicPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


