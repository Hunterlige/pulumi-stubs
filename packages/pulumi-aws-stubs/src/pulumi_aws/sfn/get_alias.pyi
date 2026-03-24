import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetAliasResult", "AwaitableGetAliasResult", "get_alias", "get_alias_output"]

@pulumi.output_type
class GetAliasResult:
    def __init__(
        __self__,
        arn=...,
        creation_date=...,
        description=...,
        id=...,
        name=...,
        region=...,
        routing_configurations=...,
        statemachine_arn=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingConfigurations")
    def routing_configurations(
        self,
    ) -> Sequence[outputs.GetAliasRoutingConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="statemachineArn")
    def statemachine_arn(self) -> _builtins.str: ...

class AwaitableGetAliasResult(GetAliasResult):
    def __await__(self): ...

def get_alias(
    description: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    statemachine_arn: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAliasResult: ...
def get_alias_output(
    description: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    statemachine_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAliasResult]: ...
