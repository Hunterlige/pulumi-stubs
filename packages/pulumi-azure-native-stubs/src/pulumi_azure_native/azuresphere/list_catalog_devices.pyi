import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListCatalogDevicesResult",
    "AwaitableListCatalogDevicesResult",
    "list_catalog_devices",
    "list_catalog_devices_output",
]

@pulumi.output_type
class ListCatalogDevicesResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.DeviceResponse]: ...

class AwaitableListCatalogDevicesResult(ListCatalogDevicesResult):
    def __await__(self): ...

def list_catalog_devices(
    catalog_name: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    maxpagesize: Optional[_builtins.int] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip: Optional[_builtins.int] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListCatalogDevicesResult: ...
def list_catalog_devices_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    maxpagesize: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListCatalogDevicesResult]: ...
