

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityFeedbackArgs', 'SecurityFeedback']
@pulumi.input_type
class SecurityFeedbackArgs:
    def __init__(__self__, *, feedback_contexts: pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]], feedback_id: pulumi.Input[_builtins.str], feedback_type: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], comment: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., reason: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackContexts")
    def feedback_contexts(self) -> pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]]:
        
        ...
    
    @feedback_contexts.setter
    def feedback_contexts(self, value: pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackId")
    def feedback_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @feedback_id.setter
    def feedback_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackType")
    def feedback_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @feedback_type.setter
    def feedback_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityFeedbackState:
    def __init__(__self__, *, comment: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., feedback_contexts: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]]] = ..., feedback_id: Optional[pulumi.Input[_builtins.str]] = ..., feedback_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., reason: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackContexts")
    def feedback_contexts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]]]:
        
        ...
    
    @feedback_contexts.setter
    def feedback_contexts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityFeedbackFeedbackContextArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackId")
    def feedback_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feedback_id.setter
    def feedback_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackType")
    def feedback_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feedback_type.setter
    def feedback_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/securityFeedback:SecurityFeedback")
class SecurityFeedback(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., feedback_contexts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityFeedbackFeedbackContextArgs, SecurityFeedbackFeedbackContextArgsDict]]]]] = ..., feedback_id: Optional[pulumi.Input[_builtins.str]] = ..., feedback_type: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., reason: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityFeedbackArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., feedback_contexts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityFeedbackFeedbackContextArgs, SecurityFeedbackFeedbackContextArgsDict]]]]] = ..., feedback_id: Optional[pulumi.Input[_builtins.str]] = ..., feedback_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., reason: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> SecurityFeedback:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackContexts")
    def feedback_contexts(self) -> pulumi.Output[Sequence[outputs.SecurityFeedbackFeedbackContext]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackId")
    def feedback_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="feedbackType")
    def feedback_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


