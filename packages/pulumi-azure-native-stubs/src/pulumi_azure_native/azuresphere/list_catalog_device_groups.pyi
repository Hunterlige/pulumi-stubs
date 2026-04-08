import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListCatalogDeviceGroupsResult",
    "AwaitableListCatalogDeviceGroupsResult",
    "list_catalog_device_groups",
    "list_catalog_device_groups_output",
]

@pulumi.output_type
class ListCatalogDeviceGroupsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.DeviceGroupResponse]: ...

class AwaitableListCatalogDeviceGroupsResult(ListCatalogDeviceGroupsResult):
    def __await__(self): ...

def list_catalog_device_groups(
    catalog_name: Optional[_builtins.str] = ...,
    device_group_name: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    maxpagesize: Optional[_builtins.int] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip: Optional[_builtins.int] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListCatalogDeviceGroupsResult: ...
def list_catalog_device_groups_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    device_group_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    maxpagesize: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListCatalogDeviceGroupsResult]: ...
