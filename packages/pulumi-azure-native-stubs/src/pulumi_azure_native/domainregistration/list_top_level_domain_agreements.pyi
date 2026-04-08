import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListTopLevelDomainAgreementsResult",
    "AwaitableListTopLevelDomainAgreementsResult",
    "list_top_level_domain_agreements",
    "list_top_level_domain_agreements_output",
]

@pulumi.output_type
class ListTopLevelDomainAgreementsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.TldLegalAgreementResponse]: ...

class AwaitableListTopLevelDomainAgreementsResult(ListTopLevelDomainAgreementsResult):
    def __await__(self): ...

def list_top_level_domain_agreements(
    for_transfer: Optional[_builtins.bool] = ...,
    include_privacy: Optional[_builtins.bool] = ...,
    name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListTopLevelDomainAgreementsResult: ...
def list_top_level_domain_agreements_output(
    for_transfer: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    include_privacy: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListTopLevelDomainAgreementsResult]: ...
