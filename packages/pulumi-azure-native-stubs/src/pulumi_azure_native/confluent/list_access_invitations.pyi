import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAccessInvitationsResult",
    "AwaitableListAccessInvitationsResult",
    "list_access_invitations",
    "list_access_invitations_output",
]

@pulumi.output_type
class ListAccessInvitationsResult:
    def __init__(__self__, data=..., kind=..., metadata=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Sequence[outputs.InvitationRecordResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ConfluentListMetadataResponse]: ...

class AwaitableListAccessInvitationsResult(ListAccessInvitationsResult):
    def __await__(self): ...

def list_access_invitations(
    organization_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    search_filters: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAccessInvitationsResult: ...
def list_access_invitations_output(
    organization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    search_filters: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAccessInvitationsResult]: ...
