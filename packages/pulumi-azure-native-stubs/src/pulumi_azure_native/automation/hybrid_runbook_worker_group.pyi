

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HybridRunbookWorkerGroupArgs', 'HybridRunbookWorkerGroup']
@pulumi.input_type
class HybridRunbookWorkerGroupArgs:
    def __init__(__self__, *, automation_account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], credential: Optional[pulumi.Input[RunAsCredentialAssociationPropertyArgs]] = ..., hybrid_runbook_worker_group_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> Optional[pulumi.Input[RunAsCredentialAssociationPropertyArgs]]:
        
        ...
    
    @credential.setter
    def credential(self, value: Optional[pulumi.Input[RunAsCredentialAssociationPropertyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridRunbookWorkerGroupName")
    def hybrid_runbook_worker_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hybrid_runbook_worker_group_name.setter
    def hybrid_runbook_worker_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:automation:HybridRunbookWorkerGroup")
class HybridRunbookWorkerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., credential: Optional[pulumi.Input[Union[RunAsCredentialAssociationPropertyArgs, RunAsCredentialAssociationPropertyArgsDict]]] = ..., hybrid_runbook_worker_group_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HybridRunbookWorkerGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> HybridRunbookWorkerGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> pulumi.Output[Optional[outputs.RunAsCredentialAssociationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
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
    


