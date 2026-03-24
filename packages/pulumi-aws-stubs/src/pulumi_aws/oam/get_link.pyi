import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetLinkResult", "AwaitableGetLinkResult", "get_link", "get_link_output"]

@pulumi.output_type
class GetLinkResult:
    def __init__(
        __self__,
        arn=...,
        id=...,
        label=...,
        label_template=...,
        link_configurations=...,
        link_id=...,
        link_identifier=...,
        region=...,
        resource_types=...,
        sink_arn=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkConfigurations")
    def link_configurations(
        self,
    ) -> Sequence[outputs.GetLinkLinkConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sinkArn")
    def sink_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetLinkResult(GetLinkResult):
    def __await__(self): ...

def get_link(
    link_identifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLinkResult: ...
def get_link_output(
    link_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLinkResult]: ...
