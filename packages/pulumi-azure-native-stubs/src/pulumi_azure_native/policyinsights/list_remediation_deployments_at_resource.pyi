import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListRemediationDeploymentsAtResourceResult",
    ...,
    "list_remediation_deployments_at_resource",
    "list_remediation_deployments_at_resource_output",
]

@pulumi.output_type
class ListRemediationDeploymentsAtResourceResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.RemediationDeploymentResponse]: ...

class AwaitableListRemediationDeploymentsAtResourceResult(
    ListRemediationDeploymentsAtResourceResult
):
    def __await__(self): ...

def list_remediation_deployments_at_resource(
    remediation_name: Optional[_builtins.str] = ...,
    resource_id: Optional[_builtins.str] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListRemediationDeploymentsAtResourceResult: ...
def list_remediation_deployments_at_resource_output(
    remediation_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListRemediationDeploymentsAtResourceResult]: ...
