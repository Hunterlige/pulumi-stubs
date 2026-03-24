

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApprovalArgs', 'Approval']
@pulumi.input_type
class ApprovalArgs:
    def __init__(__self__, *, request_metadata: pulumi.Input[RequestMetadataArgs], resource_uri: pulumi.Input[_builtins.str], approval_name: Optional[pulumi.Input[_builtins.str]] = ..., approvers: Optional[pulumi.Input[Sequence[pulumi.Input[ApproverArgs]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., grandparent_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., parent_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., state_changed_at: Optional[pulumi.Input[_builtins.str]] = ..., ticket_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMetadata")
    def request_metadata(self) -> pulumi.Input[RequestMetadataArgs]:
        
        ...
    
    @request_metadata.setter
    def request_metadata(self, value: pulumi.Input[RequestMetadataArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalName")
    def approval_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @approval_name.setter
    def approval_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def approvers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApproverArgs]]]]:
        
        ...
    
    @approvers.setter
    def approvers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApproverArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grandparentResourceId")
    def grandparent_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grandparent_resource_id.setter
    def grandparent_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResourceId")
    def parent_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_resource_id.setter
    def parent_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateChangedAt")
    def state_changed_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_changed_at.setter
    def state_changed_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ticketId")
    def ticket_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ticket_id.setter
    def ticket_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:mission:Approval")
class Approval(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., approval_name: Optional[pulumi.Input[_builtins.str]] = ..., approvers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApproverArgs, ApproverArgsDict]]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., grandparent_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., parent_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., request_metadata: Optional[pulumi.Input[Union[RequestMetadataArgs, RequestMetadataArgsDict]]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., state_changed_at: Optional[pulumi.Input[_builtins.str]] = ..., ticket_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApprovalArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Approval:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def approvers(self) -> pulumi.Output[Optional[Sequence[outputs.ApproverResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grandparentResourceId")
    def grandparent_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResourceId")
    def parent_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMetadata")
    def request_metadata(self) -> pulumi.Output[outputs.RequestMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateChangedAt")
    def state_changed_at(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ticketId")
    def ticket_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


