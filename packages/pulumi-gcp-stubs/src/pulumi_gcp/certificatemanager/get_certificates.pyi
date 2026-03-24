import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCertificatesResult",
    "AwaitableGetCertificatesResult",
    "get_certificates",
    "get_certificates_output",
]

@pulumi.output_type
class GetCertificatesResult:
    def __init__(
        __self__, certificates=..., filter=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Sequence[outputs.GetCertificatesCertificateResult]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

class AwaitableGetCertificatesResult(GetCertificatesResult):
    def __await__(self): ...

def get_certificates(
    filter: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCertificatesResult: ...
def get_certificates_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCertificatesResult]: ...
