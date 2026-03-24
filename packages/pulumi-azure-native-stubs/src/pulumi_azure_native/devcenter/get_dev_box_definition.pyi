

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDevBoxDefinitionResult', 'AwaitableGetDevBoxDefinitionResult', 'get_dev_box_definition', 'get_dev_box_definition_output']
@pulumi.output_type
class GetDevBoxDefinitionResult:
    
    def __init__(__self__, active_image_reference=..., azure_api_version=..., hibernate_support=..., id=..., image_reference=..., image_validation_error_details=..., image_validation_status=..., location=..., name=..., os_storage_type=..., provisioning_state=..., sku=..., system_data=..., tags=..., type=..., validation_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeImageReference")
    def active_image_reference(self) -> outputs.ImageReferenceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernateSupport")
    def hibernate_support(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> outputs.ImageReferenceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageValidationErrorDetails")
    def image_validation_error_details(self) -> outputs.ImageValidationErrorDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageValidationStatus")
    def image_validation_status(self) -> _builtins.str:
        
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
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
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
    
    @_builtins.property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDevBoxDefinitionResult(GetDevBoxDefinitionResult):
    def __await__(self): # -> Generator[Never, Any, GetDevBoxDefinitionResult]:
        ...
    


def get_dev_box_definition(dev_box_definition_name: Optional[_builtins.str] = ..., dev_center_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDevBoxDefinitionResult:
    
    ...

def get_dev_box_definition_output(dev_box_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_center_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDevBoxDefinitionResult]:
    
    ...

