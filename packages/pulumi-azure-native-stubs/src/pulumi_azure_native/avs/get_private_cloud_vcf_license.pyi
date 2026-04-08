import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateCloudVcfLicenseResult",
    "AwaitableGetPrivateCloudVcfLicenseResult",
    "get_private_cloud_vcf_license",
    "get_private_cloud_vcf_license_output",
]

@pulumi.output_type
class GetPrivateCloudVcfLicenseResult:
    def __init__(__self__, kind=..., provisioning_state=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

class AwaitableGetPrivateCloudVcfLicenseResult(GetPrivateCloudVcfLicenseResult):
    def __await__(self): ...

def get_private_cloud_vcf_license(
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateCloudVcfLicenseResult: ...
def get_private_cloud_vcf_license_output(
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateCloudVcfLicenseResult]: ...
