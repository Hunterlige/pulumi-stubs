

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCatalogDevBoxDefinitionErrorDetailsResult', ..., 'get_catalog_dev_box_definition_error_details', ...]
@pulumi.output_type
class GetCatalogDevBoxDefinitionErrorDetailsResult:
    
    def __init__(__self__, errors=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.CatalogErrorDetailsResponse]:
        
        ...
    


class AwaitableGetCatalogDevBoxDefinitionErrorDetailsResult(GetCatalogDevBoxDefinitionErrorDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetCatalogDevBoxDefinitionErrorDetailsResult]:
        ...
    


def get_catalog_dev_box_definition_error_details(catalog_name: Optional[_builtins.str] = ..., dev_box_definition_name: Optional[_builtins.str] = ..., dev_center_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCatalogDevBoxDefinitionErrorDetailsResult:
    
    ...

def get_catalog_dev_box_definition_error_details_output(catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_box_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_center_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCatalogDevBoxDefinitionErrorDetailsResult]:
    
    ...

