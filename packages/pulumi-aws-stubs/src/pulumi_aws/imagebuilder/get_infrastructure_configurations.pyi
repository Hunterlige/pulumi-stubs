import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInfrastructureConfigurationsResult",
    "AwaitableGetInfrastructureConfigurationsResult",
    "get_infrastructure_configurations",
    "get_infrastructure_configurations_output",
]

@pulumi.output_type
class GetInfrastructureConfigurationsResult:
    def __init__(
        __self__, arns=..., filters=..., id=..., names=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetInfrastructureConfigurationsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetInfrastructureConfigurationsResult(
    GetInfrastructureConfigurationsResult
):
    def __await__(self): ...

def get_infrastructure_configurations(
    filters: Optional[
        Sequence[
            Union[
                GetInfrastructureConfigurationsFilterArgs,
                GetInfrastructureConfigurationsFilterArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInfrastructureConfigurationsResult: ...
def get_infrastructure_configurations_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetInfrastructureConfigurationsFilterArgs,
                        GetInfrastructureConfigurationsFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInfrastructureConfigurationsResult]: ...
