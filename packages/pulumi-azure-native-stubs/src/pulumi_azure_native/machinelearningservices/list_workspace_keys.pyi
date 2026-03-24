

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWorkspaceKeysResult', 'AwaitableListWorkspaceKeysResult', 'list_workspace_keys', 'list_workspace_keys_output']
@pulumi.output_type
class ListWorkspaceKeysResult:
    def __init__(__self__, app_insights_instrumentation_key=..., container_registry_credentials=..., notebook_access_keys=..., user_storage_arm_id=..., user_storage_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInsightsInstrumentationKey")
    def app_insights_instrumentation_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRegistryCredentials")
    def container_registry_credentials(self) -> Optional[outputs.RegistryListCredentialsResultResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookAccessKeys")
    def notebook_access_keys(self) -> Optional[outputs.ListNotebookKeysResultResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userStorageArmId")
    def user_storage_arm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userStorageKey")
    def user_storage_key(self) -> _builtins.str:
        
        ...
    


class AwaitableListWorkspaceKeysResult(ListWorkspaceKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListWorkspaceKeysResult]:
        ...
    


def list_workspace_keys(resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWorkspaceKeysResult:
    
    ...

def list_workspace_keys_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWorkspaceKeysResult]:
    
    ...

