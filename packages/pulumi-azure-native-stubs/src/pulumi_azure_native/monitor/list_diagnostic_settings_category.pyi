import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListDiagnosticSettingsCategoryResult",
    "AwaitableListDiagnosticSettingsCategoryResult",
    "list_diagnostic_settings_category",
    "list_diagnostic_settings_category_output",
]

@pulumi.output_type
class ListDiagnosticSettingsCategoryResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[Sequence[outputs.DiagnosticSettingsCategoryResourceResponse]]: ...

class AwaitableListDiagnosticSettingsCategoryResult(
    ListDiagnosticSettingsCategoryResult
):
    def __await__(self): ...

def list_diagnostic_settings_category(
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListDiagnosticSettingsCategoryResult: ...
def list_diagnostic_settings_category_output(
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListDiagnosticSettingsCategoryResult]: ...
