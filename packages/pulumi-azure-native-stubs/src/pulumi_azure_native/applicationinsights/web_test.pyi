import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebTestArgs", "WebTest"]

@pulumi.input_type
class WebTestArgs:
    def __init__(
        __self__,
        *,
        locations: pulumi.Input[Sequence[pulumi.Input[WebTestGeolocationArgs]]],
        resource_group_name: pulumi.Input[_builtins.str],
        synthetic_monitor_id: pulumi.Input[_builtins.str],
        web_test_kind: Optional[pulumi.Input[WebTestKind]] = ...,
        configuration: Optional[pulumi.Input[WebTestPropertiesConfigurationArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        kind: Optional[pulumi.Input[WebTestKind]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        request: Optional[pulumi.Input[WebTestPropertiesRequestArgs]] = ...,
        retry_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_rules: Optional[
            pulumi.Input[WebTestPropertiesValidationRulesArgs]
        ] = ...,
        web_test_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[WebTestGeolocationArgs]]]: ...
    @locations.setter
    def locations(
        self, value: pulumi.Input[Sequence[pulumi.Input[WebTestGeolocationArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="syntheticMonitorId")
    def synthetic_monitor_id(self) -> pulumi.Input[_builtins.str]: ...
    @synthetic_monitor_id.setter
    def synthetic_monitor_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webTestKind")
    def web_test_kind(self) -> pulumi.Input[WebTestKind]: ...
    @web_test_kind.setter
    def web_test_kind(self, value: pulumi.Input[WebTestKind]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[WebTestPropertiesConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[WebTestPropertiesConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[WebTestKind]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[WebTestKind]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input[WebTestPropertiesRequestArgs]]: ...
    @request.setter
    def request(self, value: Optional[pulumi.Input[WebTestPropertiesRequestArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="retryEnabled")
    def retry_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retry_enabled.setter
    def retry_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationRules")
    def validation_rules(
        self,
    ) -> Optional[pulumi.Input[WebTestPropertiesValidationRulesArgs]]: ...
    @validation_rules.setter
    def validation_rules(
        self, value: Optional[pulumi.Input[WebTestPropertiesValidationRulesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webTestName")
    def web_test_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_test_name.setter
    def web_test_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:applicationinsights:WebTest")
class WebTest(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration: Optional[
            pulumi.Input[
                Union[
                    WebTestPropertiesConfigurationArgs,
                    WebTestPropertiesConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        kind: Optional[pulumi.Input[WebTestKind]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WebTestGeolocationArgs, WebTestGeolocationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        request: Optional[
            pulumi.Input[
                Union[WebTestPropertiesRequestArgs, WebTestPropertiesRequestArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        synthetic_monitor_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_rules: Optional[
            pulumi.Input[
                Union[
                    WebTestPropertiesValidationRulesArgs,
                    WebTestPropertiesValidationRulesArgsDict,
                ]
            ]
        ] = ...,
        web_test_kind: Optional[pulumi.Input[WebTestKind]] = ...,
        web_test_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebTestArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebTest: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WebTestPropertiesResponseConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> pulumi.Output[Sequence[outputs.WebTestGeolocationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def request(
        self,
    ) -> pulumi.Output[Optional[outputs.WebTestPropertiesResponseRequest]]: ...
    @_builtins.property
    @pulumi.getter(name="retryEnabled")
    def retry_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="syntheticMonitorId")
    def synthetic_monitor_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationRules")
    def validation_rules(
        self,
    ) -> pulumi.Output[Optional[outputs.WebTestPropertiesResponseValidationRules]]: ...
    @_builtins.property
    @pulumi.getter(name="webTestKind")
    def web_test_kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webTestName")
    def web_test_name(self) -> pulumi.Output[_builtins.str]: ...
