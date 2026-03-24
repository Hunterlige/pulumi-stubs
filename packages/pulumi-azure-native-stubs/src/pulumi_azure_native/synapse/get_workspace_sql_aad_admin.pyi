

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceSqlAadAdminResult', 'AwaitableGetWorkspaceSqlAadAdminResult', 'get_workspace_sql_aad_admin', 'get_workspace_sql_aad_admin_output']
@pulumi.output_type
class GetWorkspaceSqlAadAdminResult:
    
    def __init__(__self__, administrator_type=..., azure_api_version=..., id=..., login=..., name=..., sid=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceSqlAadAdminResult(GetWorkspaceSqlAadAdminResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceSqlAadAdminResult]:
        ...
    


def get_workspace_sql_aad_admin(resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceSqlAadAdminResult:
    
    ...

def get_workspace_sql_aad_admin_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceSqlAadAdminResult]:
    
    ...

