

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectResult', 'AwaitableGetProjectResult', 'get_project', 'get_project_output']
@pulumi.output_type
class GetProjectResult:
    
    def __init__(__self__, auto_create_network=..., billing_account=..., deletion_policy=..., effective_labels=..., folder_id=..., id=..., labels=..., name=..., number=..., org_id=..., project_id=..., pulumi_labels=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoCreateNetwork")
    def auto_create_network(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetProjectResult(GetProjectResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectResult]:
        ...
    


def get_project(project_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectResult:
    
    ...

def get_project_output(project_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectResult]:
    
    ...

