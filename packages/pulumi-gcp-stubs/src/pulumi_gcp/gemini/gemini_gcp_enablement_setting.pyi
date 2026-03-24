import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GeminiGcpEnablementSettingArgs", "GeminiGcpEnablementSetting"]

@pulumi.input_type
class GeminiGcpEnablementSettingArgs:
    def __init__(
        __self__,
        *,
        gemini_gcp_enablement_setting_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        disable_web_grounding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_customer_data_sharing: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geminiGcpEnablementSettingId")
    def gemini_gcp_enablement_setting_id(self) -> pulumi.Input[_builtins.str]: ...
    @gemini_gcp_enablement_setting_id.setter
    def gemini_gcp_enablement_setting_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disableWebGrounding")
    @_utilities.deprecated(...)
    def disable_web_grounding(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_web_grounding.setter
    def disable_web_grounding(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCustomerDataSharing")
    def enable_customer_data_sharing(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_customer_data_sharing.setter
    def enable_customer_data_sharing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_grounding_type.setter
    def web_grounding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GeminiGcpEnablementSettingState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_web_grounding: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_customer_data_sharing: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_gcp_enablement_setting_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableWebGrounding")
    @_utilities.deprecated(...)
    def disable_web_grounding(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_web_grounding.setter
    def disable_web_grounding(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCustomerDataSharing")
    def enable_customer_data_sharing(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_customer_data_sharing.setter
    def enable_customer_data_sharing(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="geminiGcpEnablementSettingId")
    def gemini_gcp_enablement_setting_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gemini_gcp_enablement_setting_id.setter
    def gemini_gcp_enablement_setting_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_grounding_type.setter
    def web_grounding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class GeminiGcpEnablementSetting(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disable_web_grounding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_customer_data_sharing: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_gcp_enablement_setting_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GeminiGcpEnablementSettingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_web_grounding: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_customer_data_sharing: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_gcp_enablement_setting_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        web_grounding_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GeminiGcpEnablementSetting: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableWebGrounding")
    @_utilities.deprecated(...)
    def disable_web_grounding(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCustomerDataSharing")
    def enable_customer_data_sharing(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="geminiGcpEnablementSettingId")
    def gemini_gcp_enablement_setting_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webGroundingType")
    def web_grounding_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
