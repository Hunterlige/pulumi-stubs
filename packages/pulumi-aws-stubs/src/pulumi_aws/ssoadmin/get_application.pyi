import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationResult",
    "AwaitableGetApplicationResult",
    "get_application",
    "get_application_output",
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(
        __self__,
        application_account=...,
        application_arn=...,
        application_provider_arn=...,
        description=...,
        id=...,
        instance_arn=...,
        name=...,
        portal_options=...,
        region=...,
        status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationAccount")
    def application_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationProviderArn")
    def application_provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portalOptions")
    def portal_options(self) -> Sequence[outputs.GetApplicationPortalOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

class AwaitableGetApplicationResult(GetApplicationResult):
    def __await__(self): ...

def get_application(
    application_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationResult: ...
def get_application_output(
    application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationResult]: ...
