import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTemplateArtifactResult",
    "AwaitableGetTemplateArtifactResult",
    "get_template_artifact",
    "get_template_artifact_output",
]

@pulumi.output_type
class GetTemplateArtifactResult:
    def __init__(
        __self__,
        azure_api_version=...,
        depends_on=...,
        description=...,
        display_name=...,
        id=...,
        kind=...,
        name=...,
        parameters=...,
        resource_group=...,
        template=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, outputs.ParameterValueResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTemplateArtifactResult(GetTemplateArtifactResult):
    def __await__(self): ...

def get_template_artifact(
    artifact_name: Optional[_builtins.str] = ...,
    blueprint_name: Optional[_builtins.str] = ...,
    resource_scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTemplateArtifactResult: ...
def get_template_artifact_output(
    artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
    blueprint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTemplateArtifactResult]: ...
