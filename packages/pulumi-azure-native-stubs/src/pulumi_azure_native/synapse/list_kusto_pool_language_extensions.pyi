import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListKustoPoolLanguageExtensionsResult",
    "AwaitableListKustoPoolLanguageExtensionsResult",
    "list_kusto_pool_language_extensions",
    "list_kusto_pool_language_extensions_output",
]

@pulumi.output_type
class ListKustoPoolLanguageExtensionsResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.LanguageExtensionResponse]]: ...

class AwaitableListKustoPoolLanguageExtensionsResult(
    ListKustoPoolLanguageExtensionsResult
):
    def __await__(self): ...

def list_kusto_pool_language_extensions(
    kusto_pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListKustoPoolLanguageExtensionsResult: ...
def list_kusto_pool_language_extensions_output(
    kusto_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListKustoPoolLanguageExtensionsResult]: ...
