

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProductDetailsResult', 'AwaitableListProductDetailsResult', 'list_product_details', 'list_product_details_output']
@pulumi.output_type
class ListProductDetailsResult:
    
    def __init__(__self__, compute_role=..., data_disk_images=..., gallery_package_blob_sas_uri=..., is_system_extension=..., os_disk_image=..., product_kind=..., support_multiple_extensions=..., uri=..., version=..., vm_os_type=..., vm_scale_set_enabled=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRole")
    def compute_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskImages")
    def data_disk_images(self) -> Sequence[outputs.DataDiskImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryPackageBlobSasUri")
    def gallery_package_blob_sas_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSystemExtension")
    def is_system_extension(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskImage")
    def os_disk_image(self) -> outputs.OsDiskImageResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productKind")
    def product_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportMultipleExtensions")
    def support_multiple_extensions(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmOsType")
    def vm_os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmScaleSetEnabled")
    def vm_scale_set_enabled(self) -> _builtins.bool:
        
        ...
    


class AwaitableListProductDetailsResult(ListProductDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListProductDetailsResult]:
        ...
    


def list_product_details(product_name: Optional[_builtins.str] = ..., registration_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProductDetailsResult:
    
    ...

def list_product_details_output(product_name: Optional[pulumi.Input[_builtins.str]] = ..., registration_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProductDetailsResult]:
    
    ...

