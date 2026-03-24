import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetAmiResult", "AwaitableGetAmiResult", "get_ami", "get_ami_output"]

@pulumi.output_type
class GetAmiResult:
    def __init__(
        __self__,
        allow_unsafe_filter=...,
        architecture=...,
        arn=...,
        block_device_mappings=...,
        boot_mode=...,
        creation_date=...,
        deprecation_time=...,
        description=...,
        ena_support=...,
        executable_users=...,
        filters=...,
        hypervisor=...,
        id=...,
        image_id=...,
        image_location=...,
        image_owner_alias=...,
        image_type=...,
        imds_support=...,
        include_deprecated=...,
        kernel_id=...,
        last_launched_time=...,
        most_recent=...,
        name=...,
        name_regex=...,
        owner_id=...,
        owners=...,
        platform=...,
        platform_details=...,
        product_codes=...,
        public=...,
        ramdisk_id=...,
        region=...,
        root_device_name=...,
        root_device_type=...,
        root_snapshot_id=...,
        sriov_net_support=...,
        state=...,
        state_reason=...,
        tags=...,
        tpm_support=...,
        uefi_data=...,
        usage_operation=...,
        virtualization_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowUnsafeFilter")
    def allow_unsafe_filter(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> Sequence[outputs.GetAmiBlockDeviceMappingResult]: ...
    @_builtins.property
    @pulumi.getter(name="bootMode")
    def boot_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deprecationTime")
    def deprecation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="executableUsers")
    def executable_users(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAmiFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def hypervisor(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageOwnerAlias")
    def image_owner_alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imdsSupport")
    def imds_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeDeprecated")
    def include_deprecated(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastLaunchedTime")
    def last_launched_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="platformDetails")
    def platform_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productCodes")
    def product_codes(self) -> Sequence[outputs.GetAmiProductCodeResult]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootDeviceType")
    def root_device_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootSnapshotId")
    def root_snapshot_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tpmSupport")
    def tpm_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uefiData")
    def uefi_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usageOperation")
    def usage_operation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> _builtins.str: ...

class AwaitableGetAmiResult(GetAmiResult):
    def __await__(self): ...

def get_ami(
    allow_unsafe_filter: Optional[_builtins.bool] = ...,
    executable_users: Optional[Sequence[_builtins.str]] = ...,
    filters: Optional[Sequence[Union[GetAmiFilterArgs, GetAmiFilterArgsDict]]] = ...,
    include_deprecated: Optional[_builtins.bool] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    name_regex: Optional[_builtins.str] = ...,
    owners: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    uefi_data: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAmiResult: ...
def get_ami_output(
    allow_unsafe_filter: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    executable_users: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    filters: Optional[
        pulumi.Input[Optional[Sequence[Union[GetAmiFilterArgs, GetAmiFilterArgsDict]]]]
    ] = ...,
    include_deprecated: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    owners: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    uefi_data: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAmiResult]: ...
