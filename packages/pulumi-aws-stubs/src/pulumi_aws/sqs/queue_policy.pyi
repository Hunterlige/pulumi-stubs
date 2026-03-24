

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueuePolicyArgs', 'QueuePolicy']
@pulumi.input_type
class QueuePolicyArgs:
    def __init__(__self__, *, policy: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]], queue_url: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]:
        
        ...
    
    @policy.setter
    def policy(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @queue_url.setter
    def queue_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _QueuePolicyState:
    def __init__(__self__, *, policy: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., queue_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_url.setter
    def queue_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sqs/queuePolicy:QueuePolicy")
class QueuePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., queue_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: QueuePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., queue_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> QueuePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


