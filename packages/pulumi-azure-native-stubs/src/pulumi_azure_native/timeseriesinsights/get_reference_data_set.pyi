import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReferenceDataSetResult",
    "AwaitableGetReferenceDataSetResult",
    "get_reference_data_set",
    "get_reference_data_set_output",
]

@pulumi.output_type
class GetReferenceDataSetResult:
    def __init__(
        __self__,
        azure_api_version=...,
        creation_time=...,
        data_string_comparison_behavior=...,
        id=...,
        key_properties=...,
        location=...,
        name=...,
        provisioning_state=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyProperties")
    def key_properties(
        self,
    ) -> Sequence[outputs.ReferenceDataSetKeyPropertyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetReferenceDataSetResult(GetReferenceDataSetResult):
    def __await__(self): ...

def get_reference_data_set(
    environment_name: Optional[_builtins.str] = ...,
    reference_data_set_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReferenceDataSetResult: ...
def get_reference_data_set_output(
    environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    reference_data_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReferenceDataSetResult]: ...
