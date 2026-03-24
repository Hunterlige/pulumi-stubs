

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHybridRunbookWorkerGroupResult', 'AwaitableGetHybridRunbookWorkerGroupResult', 'get_hybrid_runbook_worker_group', 'get_hybrid_runbook_worker_group_output']
@pulumi.output_type
class GetHybridRunbookWorkerGroupResult:
    
    def __init__(__self__, azure_api_version=..., credential=..., group_type=..., id=..., location=..., name=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> Optional[outputs.RunAsCredentialAssociationPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetHybridRunbookWorkerGroupResult(GetHybridRunbookWorkerGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetHybridRunbookWorkerGroupResult]:
        ...
    


def get_hybrid_runbook_worker_group(automation_account_name: Optional[_builtins.str] = ..., hybrid_runbook_worker_group_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHybridRunbookWorkerGroupResult:
    
    ...

def get_hybrid_runbook_worker_group_output(automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_runbook_worker_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHybridRunbookWorkerGroupResult]:
    
    ...

