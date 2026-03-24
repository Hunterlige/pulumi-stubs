

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImageUploadUrlForEntityTypeResult', 'AwaitableGetImageUploadUrlForEntityTypeResult', 'get_image_upload_url_for_entity_type', 'get_image_upload_url_for_entity_type_output']
@pulumi.output_type
class GetImageUploadUrlForEntityTypeResult:
    
    def __init__(__self__, content_url=..., image_exists=..., relative_path=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentUrl")
    def content_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageExists")
    def image_exists(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetImageUploadUrlForEntityTypeResult(GetImageUploadUrlForEntityTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetImageUploadUrlForEntityTypeResult]:
        ...
    


def get_image_upload_url_for_entity_type(entity_type: Optional[_builtins.str] = ..., entity_type_name: Optional[_builtins.str] = ..., hub_name: Optional[_builtins.str] = ..., relative_path: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageUploadUrlForEntityTypeResult:
    
    ...

def get_image_upload_url_for_entity_type_output(entity_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., entity_type_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., relative_path: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageUploadUrlForEntityTypeResult]:
    
    ...

