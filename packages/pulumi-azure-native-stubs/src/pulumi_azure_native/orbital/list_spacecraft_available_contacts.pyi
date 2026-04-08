import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListSpacecraftAvailableContactsResult",
    "AwaitableListSpacecraftAvailableContactsResult",
    "list_spacecraft_available_contacts",
    "list_spacecraft_available_contacts_output",
]

@pulumi.output_type
class ListSpacecraftAvailableContactsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.AvailableContactsResponse]]: ...

class AwaitableListSpacecraftAvailableContactsResult(
    ListSpacecraftAvailableContactsResult
):
    def __await__(self): ...

def list_spacecraft_available_contacts(
    contact_profile: Optional[
        Union[ContactParametersContactProfile, ContactParametersContactProfileDict]
    ] = ...,
    end_time: Optional[_builtins.str] = ...,
    ground_station_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    spacecraft_name: Optional[_builtins.str] = ...,
    start_time: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListSpacecraftAvailableContactsResult: ...
def list_spacecraft_available_contacts_output(
    contact_profile: Optional[
        pulumi.Input[
            Union[ContactParametersContactProfile, ContactParametersContactProfileDict]
        ]
    ] = ...,
    end_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ground_station_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    spacecraft_name: Optional[pulumi.Input[_builtins.str]] = ...,
    start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListSpacecraftAvailableContactsResult]: ...
