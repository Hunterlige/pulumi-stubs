

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceResult', 'AwaitableGetWorkspaceResult', 'get_workspace', 'get_workspace_output']
@pulumi.output_type
class GetWorkspaceResult:
    
    def __init__(__self__, azure_api_version=..., creation_time=..., id=..., key_vault_identifier_id=..., location=..., name=..., owner_email=..., sku=..., studio_endpoint=..., tags=..., type=..., user_storage_account_id=..., workspace_id=..., workspace_state=..., workspace_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultIdentifierId")
    def key_vault_identifier_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="ownerEmail")
    def owner_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioEndpoint")
    def studio_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userStorageAccountId")
    def user_storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceState")
    def workspace_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceType")
    def workspace_type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceResult]:
        ...
    


def get_workspace(resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceResult:
    
    ...

def get_workspace_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceResult]:
    
    ...

