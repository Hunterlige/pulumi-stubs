import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterClusterEndpointArgs",
    "ClusterClusterEndpointArgsDict",
    "SafetyRuleRuleConfigArgs",
    "SafetyRuleRuleConfigArgsDict",
]

class ClusterClusterEndpointArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterClusterEndpointArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SafetyRuleRuleConfigArgsDict(TypedDict):
    inverted: pulumi.Input[_builtins.bool]
    threshold: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SafetyRuleRuleConfigArgs:
    def __init__(
        __self__,
        *,
        inverted: pulumi.Input[_builtins.bool],
        threshold: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inverted(self) -> pulumi.Input[_builtins.bool]: ...
    @inverted.setter
    def inverted(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.int]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
