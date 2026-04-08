import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListIntegrationAccountMapContentCallbackUrlResult",
    ...,
    "list_integration_account_map_content_callback_url",
    ...,
]

@pulumi.output_type
class ListIntegrationAccountMapContentCallbackUrlResult:
    def __init__(
        __self__,
        base_path=...,
        method=...,
        queries=...,
        relative_path=...,
        relative_path_parameters=...,
        value=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basePath")
    def base_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def queries(
        self,
    ) -> Optional[outputs.WorkflowTriggerListCallbackUrlQueriesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relativePathParameters")
    def relative_path_parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

class AwaitableListIntegrationAccountMapContentCallbackUrlResult(
    ListIntegrationAccountMapContentCallbackUrlResult
):
    def __await__(self): ...

def list_integration_account_map_content_callback_url(
    integration_account_name: Optional[_builtins.str] = ...,
    key_type: Optional[Union[_builtins.str, KeyType]] = ...,
    map_name: Optional[_builtins.str] = ...,
    not_after: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListIntegrationAccountMapContentCallbackUrlResult: ...
def list_integration_account_map_content_callback_url_output(
    integration_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    key_type: Optional[pulumi.Input[Optional[Union[_builtins.str, KeyType]]]] = ...,
    map_name: Optional[pulumi.Input[_builtins.str]] = ...,
    not_after: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListIntegrationAccountMapContentCallbackUrlResult]: ...
