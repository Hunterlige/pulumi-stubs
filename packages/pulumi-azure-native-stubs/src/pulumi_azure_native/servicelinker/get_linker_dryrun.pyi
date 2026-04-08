import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLinkerDryrunResult",
    "AwaitableGetLinkerDryrunResult",
    "get_linker_dryrun",
    "get_linker_dryrun_output",
]

@pulumi.output_type
class GetLinkerDryrunResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        operation_previews=...,
        parameters=...,
        prerequisite_results=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationPreviews")
    def operation_previews(
        self,
    ) -> Sequence[outputs.DryrunOperationPreviewResponse]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[outputs.CreateOrUpdateDryrunParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="prerequisiteResults")
    def prerequisite_results(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLinkerDryrunResult(GetLinkerDryrunResult):
    def __await__(self): ...

def get_linker_dryrun(
    dryrun_name: Optional[_builtins.str] = ...,
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLinkerDryrunResult: ...
def get_linker_dryrun_output(
    dryrun_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLinkerDryrunResult]: ...
