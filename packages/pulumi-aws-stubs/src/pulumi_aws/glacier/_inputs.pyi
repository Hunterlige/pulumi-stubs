

import builtins as _builtins
import sys
import pulumi
from typing import Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VaultNotificationArgs', 'VaultNotificationArgsDict']
class VaultNotificationArgsDict(TypedDict):
    events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    sns_topic: pulumi.Input[_builtins.str]


@pulumi.input_type
class VaultNotificationArgs:
    def __init__(__self__, *, events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], sns_topic: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopic")
    def sns_topic(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sns_topic.setter
    def sns_topic(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


