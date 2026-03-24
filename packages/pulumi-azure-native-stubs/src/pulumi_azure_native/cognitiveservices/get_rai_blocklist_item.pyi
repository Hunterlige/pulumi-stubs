

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRaiBlocklistItemResult', 'AwaitableGetRaiBlocklistItemResult', 'get_rai_blocklist_item', 'get_rai_blocklist_item_output']
@pulumi.output_type
class GetRaiBlocklistItemResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRaiBlocklistItemResult(GetRaiBlocklistItemResult):
    def __await__(self): # -> Generator[Never, Any, GetRaiBlocklistItemResult]:
        ...
    


def get_rai_blocklist_item(account_name: Optional[_builtins.str] = ..., rai_blocklist_item_name: Optional[_builtins.str] = ..., rai_blocklist_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRaiBlocklistItemResult:
    
    ...

def get_rai_blocklist_item_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., rai_blocklist_item_name: Optional[pulumi.Input[_builtins.str]] = ..., rai_blocklist_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRaiBlocklistItemResult]:
    
    ...

