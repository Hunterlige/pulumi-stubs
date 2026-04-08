import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAzureDevOpsOrgAvailableResult",
    "AwaitableListAzureDevOpsOrgAvailableResult",
    "list_azure_dev_ops_org_available",
    "list_azure_dev_ops_org_available_output",
]

@pulumi.output_type
class ListAzureDevOpsOrgAvailableResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.AzureDevOpsOrgResponse]]: ...

class AwaitableListAzureDevOpsOrgAvailableResult(ListAzureDevOpsOrgAvailableResult):
    def __await__(self): ...

def list_azure_dev_ops_org_available(
    resource_group_name: Optional[_builtins.str] = ...,
    security_connector_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAzureDevOpsOrgAvailableResult: ...
def list_azure_dev_ops_org_available_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    security_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAzureDevOpsOrgAvailableResult]: ...
