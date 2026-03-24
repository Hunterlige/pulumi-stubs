

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCatalogSyncErrorDetailsResult', 'AwaitableGetCatalogSyncErrorDetailsResult', 'get_catalog_sync_error_details', 'get_catalog_sync_error_details_output']
@pulumi.output_type
class GetCatalogSyncErrorDetailsResult:
    
    def __init__(__self__, conflicts=..., errors=..., operation_error=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conflicts(self) -> Sequence[outputs.CatalogConflictErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.CatalogSyncErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationError")
    def operation_error(self) -> outputs.CatalogErrorDetailsResponse:
        
        ...
    


class AwaitableGetCatalogSyncErrorDetailsResult(GetCatalogSyncErrorDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetCatalogSyncErrorDetailsResult]:
        ...
    


def get_catalog_sync_error_details(catalog_name: Optional[_builtins.str] = ..., dev_center_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCatalogSyncErrorDetailsResult:
    
    ...

def get_catalog_sync_error_details_output(catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_center_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCatalogSyncErrorDetailsResult]:
    
    ...

