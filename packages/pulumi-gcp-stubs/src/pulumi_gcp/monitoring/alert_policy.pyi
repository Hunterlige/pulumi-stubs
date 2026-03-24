import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AlertPolicyArgs", "AlertPolicy"]

@pulumi.input_type
class AlertPolicyArgs:
    def __init__(
        __self__,
        *,
        combiner: pulumi.Input[_builtins.str],
        conditions: pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]],
        display_name: pulumi.Input[_builtins.str],
        alert_strategy: Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]] = ...,
        documentation: Optional[pulumi.Input[AlertPolicyDocumentationArgs]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_channels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def combiner(self) -> pulumi.Input[_builtins.str]: ...
    @combiner.setter
    def combiner(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]]: ...
    @conditions.setter
    def conditions(
        self, value: pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alertStrategy")
    def alert_strategy(
        self,
    ) -> Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]]: ...
    @alert_strategy.setter
    def alert_strategy(
        self, value: Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[AlertPolicyDocumentationArgs]]: ...
    @documentation.setter
    def documentation(
        self, value: Optional[pulumi.Input[AlertPolicyDocumentationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationChannels")
    def notification_channels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_channels.setter
    def notification_channels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _AlertPolicyState:
    def __init__(
        __self__,
        *,
        alert_strategy: Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]] = ...,
        combiner: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]]
        ] = ...,
        creation_records: Optional[
            pulumi.Input[Sequence[pulumi.Input[AlertPolicyCreationRecordArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[pulumi.Input[AlertPolicyDocumentationArgs]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertStrategy")
    def alert_strategy(
        self,
    ) -> Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]]: ...
    @alert_strategy.setter
    def alert_strategy(
        self, value: Optional[pulumi.Input[AlertPolicyAlertStrategyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def combiner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @combiner.setter
    def combiner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationRecords")
    def creation_records(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AlertPolicyCreationRecordArgs]]]
    ]: ...
    @creation_records.setter
    def creation_records(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AlertPolicyCreationRecordArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[AlertPolicyDocumentationArgs]]: ...
    @documentation.setter
    def documentation(
        self, value: Optional[pulumi.Input[AlertPolicyDocumentationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationChannels")
    def notification_channels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_channels.setter
    def notification_channels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:monitoring/alertPolicy:AlertPolicy")
class AlertPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alert_strategy: Optional[
            pulumi.Input[
                Union[AlertPolicyAlertStrategyArgs, AlertPolicyAlertStrategyArgsDict]
            ]
        ] = ...,
        combiner: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AlertPolicyConditionArgs, AlertPolicyConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[
            pulumi.Input[
                Union[AlertPolicyDocumentationArgs, AlertPolicyDocumentationArgsDict]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_channels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AlertPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alert_strategy: Optional[
            pulumi.Input[
                Union[AlertPolicyAlertStrategyArgs, AlertPolicyAlertStrategyArgsDict]
            ]
        ] = ...,
        combiner: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AlertPolicyConditionArgs, AlertPolicyConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        creation_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AlertPolicyCreationRecordArgs,
                            AlertPolicyCreationRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[
            pulumi.Input[
                Union[AlertPolicyDocumentationArgs, AlertPolicyDocumentationArgsDict]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AlertPolicy: ...
    @_builtins.property
    @pulumi.getter(name="alertStrategy")
    def alert_strategy(
        self,
    ) -> pulumi.Output[Optional[outputs.AlertPolicyAlertStrategy]]: ...
    @_builtins.property
    @pulumi.getter
    def combiner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.AlertPolicyCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="creationRecords")
    def creation_records(
        self,
    ) -> pulumi.Output[Sequence[outputs.AlertPolicyCreationRecord]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def documentation(
        self,
    ) -> pulumi.Output[Optional[outputs.AlertPolicyDocumentation]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationChannels")
    def notification_channels(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
