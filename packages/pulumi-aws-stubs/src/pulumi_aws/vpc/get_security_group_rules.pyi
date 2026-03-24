import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityGroupRulesResult",
    "AwaitableGetSecurityGroupRulesResult",
    "get_security_group_rules",
    "get_security_group_rules_output",
]

@pulumi.output_type
class GetSecurityGroupRulesResult:
    def __init__(
        __self__, filters=..., id=..., ids=..., region=..., tags=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetSecurityGroupRulesFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

class AwaitableGetSecurityGroupRulesResult(GetSecurityGroupRulesResult):
    def __await__(self): ...

def get_security_group_rules(
    filters: Optional[
        Sequence[
            Union[GetSecurityGroupRulesFilterArgs, GetSecurityGroupRulesFilterArgsDict]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityGroupRulesResult: ...
def get_security_group_rules_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetSecurityGroupRulesFilterArgs,
                        GetSecurityGroupRulesFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityGroupRulesResult]: ...
