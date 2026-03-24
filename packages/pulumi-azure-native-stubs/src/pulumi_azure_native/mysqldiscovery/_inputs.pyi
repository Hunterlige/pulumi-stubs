

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ErrorArgs', 'ErrorArgsDict', 'ExtendedLocationArgs', 'ExtendedLocationArgsDict']
class ErrorArgsDict(TypedDict):
    
    code: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    possible_cause: NotRequired[pulumi.Input[_builtins.str]]
    recommended_action: NotRequired[pulumi.Input[_builtins.str]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    summary_message: NotRequired[pulumi.Input[_builtins.str]]
    updated_time_stamp: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ErrorArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., possible_cause: Optional[pulumi.Input[_builtins.str]] = ..., recommended_action: Optional[pulumi.Input[_builtins.str]] = ..., run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ..., summary_message: Optional[pulumi.Input[_builtins.str]] = ..., updated_time_stamp: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCause")
    def possible_cause(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @possible_cause.setter
    def possible_cause(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recommended_action.setter
    def recommended_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @summary_message.setter
    def summary_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimeStamp")
    def updated_time_stamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_time_stamp.setter
    def updated_time_stamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


