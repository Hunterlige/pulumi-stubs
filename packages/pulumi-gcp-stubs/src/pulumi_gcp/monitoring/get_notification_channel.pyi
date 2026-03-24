

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNotificationChannelResult', 'AwaitableGetNotificationChannelResult', 'get_notification_channel', 'get_notification_channel_output']
@pulumi.output_type
class GetNotificationChannelResult:
    
    def __init__(__self__, description=..., display_name=..., enabled=..., force_delete=..., id=..., labels=..., name=..., project=..., sensitive_labels=..., type=..., user_labels=..., verification_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveLabels")
    def sensitive_labels(self) -> Sequence[outputs.GetNotificationChannelSensitiveLabelResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNotificationChannelResult(GetNotificationChannelResult):
    def __await__(self): # -> Generator[Never, Any, GetNotificationChannelResult]:
        ...
    


def get_notification_channel(display_name: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., project: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., user_labels: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNotificationChannelResult:
    
    ...

def get_notification_channel_output(display_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., labels: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_labels: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNotificationChannelResult]:
    
    ...

