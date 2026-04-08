import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBastionShareableLinkResult",
    "AwaitableGetBastionShareableLinkResult",
    "get_bastion_shareable_link",
    "get_bastion_shareable_link_output",
]

@pulumi.output_type
class GetBastionShareableLinkResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.BastionShareableLinkResponse]]: ...

class AwaitableGetBastionShareableLinkResult(GetBastionShareableLinkResult):
    def __await__(self): ...

def get_bastion_shareable_link(
    bastion_host_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vms: Optional[
        Sequence[Union[BastionShareableLink, BastionShareableLinkDict]]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBastionShareableLinkResult: ...
def get_bastion_shareable_link_output(
    bastion_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vms: Optional[
        pulumi.Input[
            Optional[Sequence[Union[BastionShareableLink, BastionShareableLinkDict]]]
        ]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBastionShareableLinkResult]: ...
