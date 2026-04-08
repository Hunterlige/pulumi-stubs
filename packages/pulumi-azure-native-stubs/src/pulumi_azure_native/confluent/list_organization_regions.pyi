import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListOrganizationRegionsResult",
    "AwaitableListOrganizationRegionsResult",
    "list_organization_regions",
    "list_organization_regions_output",
]

@pulumi.output_type
class ListOrganizationRegionsResult:
    def __init__(__self__, data=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Sequence[outputs.RegionRecordResponse]]: ...

class AwaitableListOrganizationRegionsResult(ListOrganizationRegionsResult):
    def __await__(self): ...

def list_organization_regions(
    organization_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    search_filters: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListOrganizationRegionsResult: ...
def list_organization_regions_output(
    organization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    search_filters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListOrganizationRegionsResult]: ...
