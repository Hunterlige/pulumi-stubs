import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLaunchConfigurationResult",
    "AwaitableGetLaunchConfigurationResult",
    "get_launch_configuration",
    "get_launch_configuration_output",
]

@pulumi.output_type
class GetLaunchConfigurationResult:
    def __init__(
        __self__,
        arn=...,
        associate_public_ip_address=...,
        ebs_block_devices=...,
        ebs_optimized=...,
        enable_monitoring=...,
        ephemeral_block_devices=...,
        iam_instance_profile=...,
        id=...,
        image_id=...,
        instance_type=...,
        key_name=...,
        metadata_options=...,
        name=...,
        placement_tenancy=...,
        region=...,
        root_block_devices=...,
        security_groups=...,
        spot_price=...,
        user_data=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(
        self,
    ) -> Sequence[outputs.GetLaunchConfigurationEbsBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableMonitoring")
    def enable_monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(
        self,
    ) -> Sequence[outputs.GetLaunchConfigurationEphemeralBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(
        self,
    ) -> Sequence[outputs.GetLaunchConfigurationMetadataOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootBlockDevices")
    def root_block_devices(
        self,
    ) -> Sequence[outputs.GetLaunchConfigurationRootBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> _builtins.str: ...

class AwaitableGetLaunchConfigurationResult(GetLaunchConfigurationResult):
    def __await__(self): ...

def get_launch_configuration(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLaunchConfigurationResult: ...
def get_launch_configuration_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLaunchConfigurationResult]: ...
