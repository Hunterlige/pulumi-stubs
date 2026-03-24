

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectionRaiBlocklistItemResult', 'AwaitableGetConnectionRaiBlocklistItemResult', 'get_connection_rai_blocklist_item', 'get_connection_rai_blocklist_item_output']
@pulumi.output_type
class GetConnectionRaiBlocklistItemResult:
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.RaiBlocklistItemPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectionRaiBlocklistItemResult(GetConnectionRaiBlocklistItemResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectionRaiBlocklistItemResult]:
        ...
    


def get_connection_rai_blocklist_item(connection_name: Optional[_builtins.str] = ..., rai_blocklist_item_name: Optional[_builtins.str] = ..., rai_blocklist_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectionRaiBlocklistItemResult:
    
    ...

def get_connection_rai_blocklist_item_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., rai_blocklist_item_name: Optional[pulumi.Input[_builtins.str]] = ..., rai_blocklist_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectionRaiBlocklistItemResult]:
    
    ...

