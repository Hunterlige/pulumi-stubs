import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SQuotaPreferenceQuotaConfigArgs", "SQuotaPreferenceQuotaConfigArgsDict"]

class SQuotaPreferenceQuotaConfigArgsDict(TypedDict):
    preferred_value: pulumi.Input[_builtins.str]
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    granted_value: NotRequired[pulumi.Input[_builtins.str]]
    request_origin: NotRequired[pulumi.Input[_builtins.str]]
    state_detail: NotRequired[pulumi.Input[_builtins.str]]
    trace_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SQuotaPreferenceQuotaConfigArgs:
    def __init__(
        __self__,
        *,
        preferred_value: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        granted_value: Optional[pulumi.Input[_builtins.str]] = ...,
        request_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        state_detail: Optional[pulumi.Input[_builtins.str]] = ...,
        trace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredValue")
    def preferred_value(self) -> pulumi.Input[_builtins.str]: ...
    @preferred_value.setter
    def preferred_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grantedValue")
    def granted_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @granted_value.setter
    def granted_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestOrigin")
    def request_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_origin.setter
    def request_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateDetail")
    def state_detail(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_detail.setter
    def state_detail(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="traceId")
    def trace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trace_id.setter
    def trace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
