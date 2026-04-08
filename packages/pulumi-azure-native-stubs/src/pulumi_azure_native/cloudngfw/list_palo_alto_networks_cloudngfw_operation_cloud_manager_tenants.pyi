import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class ListPaloAltoNetworksCloudngfwOperationCloudManagerTenantsResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[_builtins.str]: ...

class AwaitableListPaloAltoNetworksCloudngfwOperationCloudManagerTenantsResult(
    ListPaloAltoNetworksCloudngfwOperationCloudManagerTenantsResult
):
    def __await__(self): ...

def list_palo_alto_networks_cloudngfw_operation_cloud_manager_tenants(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPaloAltoNetworksCloudngfwOperationCloudManagerTenantsResult: ...
def list_palo_alto_networks_cloudngfw_operation_cloud_manager_tenants_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListPaloAltoNetworksCloudngfwOperationCloudManagerTenantsResult]: ...
