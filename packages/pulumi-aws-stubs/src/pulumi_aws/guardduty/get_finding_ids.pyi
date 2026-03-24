import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFindingIdsResult",
    "AwaitableGetFindingIdsResult",
    "get_finding_ids",
    "get_finding_ids_output",
]

@pulumi.output_type
class GetFindingIdsResult:
    def __init__(
        __self__, detector_id=..., finding_ids=..., has_findings=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="findingIds")
    def finding_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasFindings")
    def has_findings(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetFindingIdsResult(GetFindingIdsResult):
    def __await__(self): ...

def get_finding_ids(
    detector_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFindingIdsResult: ...
def get_finding_ids_output(
    detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFindingIdsResult]: ...
