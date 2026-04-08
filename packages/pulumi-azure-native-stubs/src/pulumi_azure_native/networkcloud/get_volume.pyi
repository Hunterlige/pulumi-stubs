import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVolumeResult",
    "AwaitableGetVolumeResult",
    "get_volume",
    "get_volume_output",
]

@pulumi.output_type
class GetVolumeResult:
    def __init__(
        __self__,
        attached_to=...,
        azure_api_version=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        extended_location=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        serial_number=...,
        size_mi_b=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedTo")
    def attached_to(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizeMiB")
    def size_mi_b(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVolumeResult(GetVolumeResult):
    def __await__(self): ...

def get_volume(
    resource_group_name: Optional[_builtins.str] = ...,
    volume_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVolumeResult: ...
def get_volume_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVolumeResult]: ...
