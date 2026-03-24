

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectCatalogImageDefinitionErrorDetailsResult', ..., 'get_project_catalog_image_definition_error_details', ...]
@pulumi.output_type
class GetProjectCatalogImageDefinitionErrorDetailsResult:
    
    def __init__(__self__, errors=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.CatalogErrorDetailsResponse]:
        
        ...
    


class AwaitableGetProjectCatalogImageDefinitionErrorDetailsResult(GetProjectCatalogImageDefinitionErrorDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectCatalogImageDefinitionErrorDetailsResult]:
        ...
    


def get_project_catalog_image_definition_error_details(catalog_name: Optional[_builtins.str] = ..., image_definition_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectCatalogImageDefinitionErrorDetailsResult:
    
    ...

def get_project_catalog_image_definition_error_details_output(catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., image_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectCatalogImageDefinitionErrorDetailsResult]:
    
    ...

