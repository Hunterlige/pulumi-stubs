import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SmsPreferencesArgs", "SmsPreferences"]

@pulumi.input_type
class SmsPreferencesArgs:
    def __init__(
        __self__,
        *,
        default_sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_sms_type: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_success_sampling_rate: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        monthly_spend_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_report_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSenderId")
    def default_sender_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_sender_id.setter
    def default_sender_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSmsType")
    def default_sms_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_sms_type.setter
    def default_sms_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusIamRoleArn")
    def delivery_status_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_status_iam_role_arn.setter
    def delivery_status_iam_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusSuccessSamplingRate")
    def delivery_status_success_sampling_rate(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_status_success_sampling_rate.setter
    def delivery_status_success_sampling_rate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monthlySpendLimit")
    def monthly_spend_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monthly_spend_limit.setter
    def monthly_spend_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usageReportS3Bucket")
    def usage_report_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @usage_report_s3_bucket.setter
    def usage_report_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SmsPreferencesState:
    def __init__(
        __self__,
        *,
        default_sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_sms_type: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_success_sampling_rate: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        monthly_spend_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_report_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSenderId")
    def default_sender_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_sender_id.setter
    def default_sender_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSmsType")
    def default_sms_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_sms_type.setter
    def default_sms_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusIamRoleArn")
    def delivery_status_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_status_iam_role_arn.setter
    def delivery_status_iam_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusSuccessSamplingRate")
    def delivery_status_success_sampling_rate(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_status_success_sampling_rate.setter
    def delivery_status_success_sampling_rate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monthlySpendLimit")
    def monthly_spend_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monthly_spend_limit.setter
    def monthly_spend_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usageReportS3Bucket")
    def usage_report_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @usage_report_s3_bucket.setter
    def usage_report_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sns/smsPreferences:SmsPreferences")
class SmsPreferences(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_sms_type: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_success_sampling_rate: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        monthly_spend_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_report_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[SmsPreferencesArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_sms_type: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_status_success_sampling_rate: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        monthly_spend_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_report_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SmsPreferences: ...
    @_builtins.property
    @pulumi.getter(name="defaultSenderId")
    def default_sender_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSmsType")
    def default_sms_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusIamRoleArn")
    def delivery_status_iam_role_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStatusSuccessSamplingRate")
    def delivery_status_success_sampling_rate(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="monthlySpendLimit")
    def monthly_spend_limit(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usageReportS3Bucket")
    def usage_report_s3_bucket(self) -> pulumi.Output[Optional[_builtins.str]]: ...
