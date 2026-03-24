

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkbookTemplateResult', 'AwaitableGetWorkbookTemplateResult', 'get_workbook_template', 'get_workbook_template_output']
@pulumi.output_type
class GetWorkbookTemplateResult:
    
    def __init__(__self__, author=..., azure_api_version=..., galleries=..., id=..., localized=..., location=..., name=..., priority=..., tags=..., template_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def galleries(self) -> Sequence[outputs.WorkbookTemplateGalleryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def localized(self) -> Optional[Mapping[str, Sequence[outputs.WorkbookTemplateLocalizedGalleryResponse]]]:
        
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
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkbookTemplateResult(GetWorkbookTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkbookTemplateResult]:
        ...
    


def get_workbook_template(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkbookTemplateResult:
    
    ...

def get_workbook_template_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkbookTemplateResult]:
    
    ...

