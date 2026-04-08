import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListCustomApiWsdlInterfacesResult",
    "AwaitableListCustomApiWsdlInterfacesResult",
    "list_custom_api_wsdl_interfaces",
    "list_custom_api_wsdl_interfaces_output",
]

@pulumi.output_type
class ListCustomApiWsdlInterfacesResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.WsdlServiceResponse]]: ...

class AwaitableListCustomApiWsdlInterfacesResult(ListCustomApiWsdlInterfacesResult):
    def __await__(self): ...

def list_custom_api_wsdl_interfaces(
    content: Optional[_builtins.str] = ...,
    import_method: Optional[Union[_builtins.str, WsdlImportMethod]] = ...,
    location: Optional[_builtins.str] = ...,
    service: Optional[Union[WsdlService, WsdlServiceDict]] = ...,
    subscription_id: Optional[_builtins.str] = ...,
    url: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListCustomApiWsdlInterfacesResult: ...
def list_custom_api_wsdl_interfaces_output(
    content: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    import_method: Optional[
        pulumi.Input[Optional[Union[_builtins.str, WsdlImportMethod]]]
    ] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    service: Optional[
        pulumi.Input[Optional[Union[WsdlService, WsdlServiceDict]]]
    ] = ...,
    subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    url: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListCustomApiWsdlInterfacesResult]: ...
