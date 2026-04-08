import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetImageResult", "AwaitableGetImageResult", "get_image", "get_image_output"]

@pulumi.output_type
class GetImageResult:
    def __init__(
        __self__,
        azure_api_version=...,
        component_id=...,
        description=...,
        id=...,
        image=...,
        image_id=...,
        image_name=...,
        image_type=...,
        name=...,
        provisioning_state=...,
        regional_data_boundary=...,
        system_data=...,
        type=...,
        uri=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

class AwaitableGetImageResult(GetImageResult):
    def __await__(self): ...

def get_image(
    catalog_name: Optional[_builtins.str] = ...,
    image_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImageResult: ...
def get_image_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    image_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImageResult]: ...
