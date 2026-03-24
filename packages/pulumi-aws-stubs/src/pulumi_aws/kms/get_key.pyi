import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetKeyResult", "AwaitableGetKeyResult", "get_key", "get_key_output"]

@pulumi.output_type
class GetKeyResult:
    def __init__(
        __self__,
        arn=...,
        aws_account_id=...,
        cloud_hsm_cluster_id=...,
        creation_date=...,
        custom_key_store_id=...,
        customer_master_key_spec=...,
        deletion_date=...,
        description=...,
        enabled=...,
        expiration_model=...,
        grant_tokens=...,
        id=...,
        key_id=...,
        key_manager=...,
        key_spec=...,
        key_state=...,
        key_usage=...,
        multi_region=...,
        multi_region_configurations=...,
        origin=...,
        pending_deletion_window_in_days=...,
        region=...,
        valid_to=...,
        xks_key_configurations=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudHsmClusterId")
    def cloud_hsm_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customKeyStoreId")
    def custom_key_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="expirationModel")
    def expiration_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyManager")
    def key_manager(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionConfigurations")
    def multi_region_configurations(
        self,
    ) -> Sequence[outputs.GetKeyMultiRegionConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pendingDeletionWindowInDays")
    def pending_deletion_window_in_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="xksKeyConfigurations")
    def xks_key_configurations(
        self,
    ) -> Sequence[outputs.GetKeyXksKeyConfigurationResult]: ...

class AwaitableGetKeyResult(GetKeyResult):
    def __await__(self): ...

def get_key(
    grant_tokens: Optional[Sequence[_builtins.str]] = ...,
    key_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKeyResult: ...
def get_key_output(
    grant_tokens: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKeyResult]: ...
