import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class ListPaloAltoNetworksCloudngfwOperationProductSerialNumberStatusResult:
    def __init__(__self__, serial_number=..., status=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

class AwaitableListPaloAltoNetworksCloudngfwOperationProductSerialNumberStatusResult(
    ListPaloAltoNetworksCloudngfwOperationProductSerialNumberStatusResult
):
    def __await__(self): ...

def list_palo_alto_networks_cloudngfw_operation_product_serial_number_status(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPaloAltoNetworksCloudngfwOperationProductSerialNumberStatusResult: ...
def list_palo_alto_networks_cloudngfw_operation_product_serial_number_status_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[
    ListPaloAltoNetworksCloudngfwOperationProductSerialNumberStatusResult
]: ...
