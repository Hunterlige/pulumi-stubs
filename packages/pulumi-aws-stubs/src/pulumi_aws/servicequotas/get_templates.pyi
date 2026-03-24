import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTemplatesResult",
    "AwaitableGetTemplatesResult",
    "get_templates",
    "get_templates_output",
]

@pulumi.output_type
class GetTemplatesResult:
    def __init__(
        __self__, aws_region=..., id=..., region=..., templates=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use get_region instead.""")
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetTemplatesTemplateResult]: ...

class AwaitableGetTemplatesResult(GetTemplatesResult):
    def __await__(self): ...

def get_templates(
    aws_region: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTemplatesResult: ...
def get_templates_output(
    aws_region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTemplatesResult]: ...
