

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JitRequestArgs', 'JitRequest']
@pulumi.input_type
class JitRequestArgs:
    def __init__(__self__, *, application_resource_id: pulumi.Input[_builtins.str], jit_authorization_policies: pulumi.Input[Sequence[pulumi.Input[JitAuthorizationPoliciesArgs]]], jit_scheduling_policy: pulumi.Input[JitSchedulingPolicyArgs], resource_group_name: pulumi.Input[_builtins.str], jit_request_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationResourceId")
    def application_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_resource_id.setter
    def application_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitAuthorizationPolicies")
    def jit_authorization_policies(self) -> pulumi.Input[Sequence[pulumi.Input[JitAuthorizationPoliciesArgs]]]:
        
        ...
    
    @jit_authorization_policies.setter
    def jit_authorization_policies(self, value: pulumi.Input[Sequence[pulumi.Input[JitAuthorizationPoliciesArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitSchedulingPolicy")
    def jit_scheduling_policy(self) -> pulumi.Input[JitSchedulingPolicyArgs]:
        
        ...
    
    @jit_scheduling_policy.setter
    def jit_scheduling_policy(self, value: pulumi.Input[JitSchedulingPolicyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitRequestName")
    def jit_request_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @jit_request_name.setter
    def jit_request_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:solutions:JitRequest")
class JitRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., jit_authorization_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JitAuthorizationPoliciesArgs, JitAuthorizationPoliciesArgsDict]]]]] = ..., jit_request_name: Optional[pulumi.Input[_builtins.str]] = ..., jit_scheduling_policy: Optional[pulumi.Input[Union[JitSchedulingPolicyArgs, JitSchedulingPolicyArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JitRequestArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> JitRequest:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationResourceId")
    def application_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[outputs.ApplicationClientDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitAuthorizationPolicies")
    def jit_authorization_policies(self) -> pulumi.Output[Sequence[outputs.JitAuthorizationPoliciesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitRequestState")
    def jit_request_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jitSchedulingPolicy")
    def jit_scheduling_policy(self) -> pulumi.Output[outputs.JitSchedulingPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherTenantId")
    def publisher_tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[outputs.ApplicationClientDetailsResponse]:
        
        ...
    


