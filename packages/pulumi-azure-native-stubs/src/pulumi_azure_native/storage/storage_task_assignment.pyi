

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StorageTaskAssignmentArgs', 'StorageTaskAssignment']
@pulumi.input_type
class StorageTaskAssignmentArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], properties: pulumi.Input[StorageTaskAssignmentPropertiesArgs], resource_group_name: pulumi.Input[_builtins.str], storage_task_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[StorageTaskAssignmentPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[StorageTaskAssignmentPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTaskAssignmentName")
    def storage_task_assignment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_task_assignment_name.setter
    def storage_task_assignment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:StorageTaskAssignment")
class StorageTaskAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[StorageTaskAssignmentPropertiesArgs, StorageTaskAssignmentPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_task_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StorageTaskAssignmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> StorageTaskAssignment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.StorageTaskAssignmentPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


