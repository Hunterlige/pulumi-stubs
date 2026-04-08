import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListConnectionAllModelsResult",
    "AwaitableListConnectionAllModelsResult",
    "list_connection_all_models",
    "list_connection_all_models_output",
]

@pulumi.output_type
class ListConnectionAllModelsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.EndpointModelPropertiesResponse]]: ...

class AwaitableListConnectionAllModelsResult(ListConnectionAllModelsResult):
    def __await__(self): ...

def list_connection_all_models(
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListConnectionAllModelsResult: ...
def list_connection_all_models_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListConnectionAllModelsResult]: ...
