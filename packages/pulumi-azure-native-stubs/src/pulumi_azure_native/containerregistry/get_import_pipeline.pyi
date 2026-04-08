import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetImportPipelineResult",
    "AwaitableGetImportPipelineResult",
    "get_import_pipeline",
    "get_import_pipeline_output",
]

@pulumi.output_type
class GetImportPipelineResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        options=...,
        provisioning_state=...,
        source=...,
        system_data=...,
        trigger=...,
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
    def identity(self) -> Optional[outputs.IdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.ImportPipelineSourcePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.PipelineTriggerPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetImportPipelineResult(GetImportPipelineResult):
    def __await__(self): ...

def get_import_pipeline(
    import_pipeline_name: Optional[_builtins.str] = ...,
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImportPipelineResult: ...
def get_import_pipeline_output(
    import_pipeline_name: Optional[pulumi.Input[_builtins.str]] = ...,
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImportPipelineResult]: ...
