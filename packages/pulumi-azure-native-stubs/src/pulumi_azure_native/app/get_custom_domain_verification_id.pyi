import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomDomainVerificationIdResult",
    "AwaitableGetCustomDomainVerificationIdResult",
    "get_custom_domain_verification_id",
    "get_custom_domain_verification_id_output",
]

@pulumi.output_type
class GetCustomDomainVerificationIdResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

class AwaitableGetCustomDomainVerificationIdResult(GetCustomDomainVerificationIdResult):
    def __await__(self): ...

def get_custom_domain_verification_id(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCustomDomainVerificationIdResult: ...
def get_custom_domain_verification_id_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomDomainVerificationIdResult]: ...
