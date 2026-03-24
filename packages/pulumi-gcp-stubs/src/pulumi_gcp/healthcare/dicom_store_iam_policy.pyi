import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DicomStoreIamPolicyArgs", "DicomStoreIamPolicy"]

@pulumi.input_type
class DicomStoreIamPolicyArgs:
    def __init__(
        __self__,
        *,
        dicom_store_id: pulumi.Input[_builtins.str],
        policy_data: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @dicom_store_id.setter
    def dicom_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]: ...
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _DicomStoreIamPolicyState:
    def __init__(
        __self__,
        *,
        dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dicom_store_id.setter
    def dicom_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DicomStoreIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DicomStoreIamPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DicomStoreIamPolicy: ...
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]: ...
