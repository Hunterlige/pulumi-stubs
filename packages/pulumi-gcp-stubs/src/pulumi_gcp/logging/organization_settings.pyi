import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationSettingsArgs", "OrganizationSettings"]

@pulumi.input_type
class OrganizationSettingsArgs:
    def __init__(
        __self__,
        *,
        organization: pulumi.Input[_builtins.str],
        disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OrganizationSettingsState:
    def __init__(
        __self__,
        *,
        disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_default_sink.setter
    def disable_default_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_service_account_id.setter
    def kms_service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_service_account_id.setter
    def logging_service_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class OrganizationSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        disable_default_sink: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OrganizationSettings: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultSink")
    def disable_default_sink(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsServiceAccountId")
    def kms_service_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingServiceAccountId")
    def logging_service_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output[_builtins.str]: ...
