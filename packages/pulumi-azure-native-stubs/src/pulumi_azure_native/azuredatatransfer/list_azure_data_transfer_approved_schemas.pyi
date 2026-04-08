import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAzureDataTransferApprovedSchemasResult",
    ...,
    "list_azure_data_transfer_approved_schemas",
    "list_azure_data_transfer_approved_schemas_output",
]

@pulumi.output_type
class ListAzureDataTransferApprovedSchemasResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SchemaResponse]]: ...

class AwaitableListAzureDataTransferApprovedSchemasResult(
    ListAzureDataTransferApprovedSchemasResult
):
    def __await__(self): ...

def list_azure_data_transfer_approved_schemas(
    direction: Optional[Union[_builtins.str, ListApprovedSchemasDirection]] = ...,
    pipeline: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAzureDataTransferApprovedSchemasResult: ...
def list_azure_data_transfer_approved_schemas_output(
    direction: Optional[
        pulumi.Input[Optional[Union[_builtins.str, ListApprovedSchemasDirection]]]
    ] = ...,
    pipeline: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAzureDataTransferApprovedSchemasResult]: ...
