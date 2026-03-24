

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogResourcePolicyArgs', 'LogResourcePolicy']
@pulumi.input_type
class LogResourcePolicyArgs:
    def __init__(__self__, *, policy_document: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]], policy_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LogResourcePolicyState:
    def __init__(__self__, *, policy_document: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_scope.setter
    def policy_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/logResourcePolicy:LogResourcePolicy")
class LogResourcePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_document: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LogResourcePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy_document: Optional[pulumi.Input[Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ...) -> LogResourcePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


