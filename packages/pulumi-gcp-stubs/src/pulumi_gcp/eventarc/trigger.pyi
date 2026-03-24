import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TriggerArgs", "Trigger"]

@pulumi.input_type
class TriggerArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[TriggerDestinationArgs],
        location: pulumi.Input[_builtins.str],
        matching_criterias: pulumi.Input[
            Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]
        ],
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        event_data_content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[pulumi.Input[TriggerRetryPolicyArgs]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        transport: Optional[pulumi.Input[TriggerTransportArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[TriggerDestinationArgs]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[TriggerDestinationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="matchingCriterias")
    def matching_criterias(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]]: ...
    @matching_criterias.setter
    def matching_criterias(
        self, value: pulumi.Input[Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventDataContentType")
    def event_data_content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_data_content_type.setter
    def event_data_content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[TriggerRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[TriggerRetryPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transport(self) -> Optional[pulumi.Input[TriggerTransportArgs]]: ...
    @transport.setter
    def transport(self, value: Optional[pulumi.Input[TriggerTransportArgs]]): ...

@pulumi.input_type
class _TriggerState:
    def __init__(
        __self__,
        *,
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[TriggerDestinationArgs]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        event_data_content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        matching_criterias: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_policy: Optional[pulumi.Input[TriggerRetryPolicyArgs]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        transport: Optional[pulumi.Input[TriggerTransportArgs]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @conditions.setter
    def conditions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[TriggerDestinationArgs]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[TriggerDestinationArgs]]): ...
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
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventDataContentType")
    def event_data_content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_data_content_type.setter
    def event_data_content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="matchingCriterias")
    def matching_criterias(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]]
    ]: ...
    @matching_criterias.setter
    def matching_criterias(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerMatchingCriteriaArgs]]]
        ],
    ): ...
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
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[TriggerRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[TriggerRetryPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transport(self) -> Optional[pulumi.Input[TriggerTransportArgs]]: ...
    @transport.setter
    def transport(self, value: Optional[pulumi.Input[TriggerTransportArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:eventarc/trigger:Trigger")
class Trigger(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[Union[TriggerDestinationArgs, TriggerDestinationArgsDict]]
        ] = ...,
        event_data_content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        matching_criterias: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TriggerMatchingCriteriaArgs, TriggerMatchingCriteriaArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[
            pulumi.Input[Union[TriggerRetryPolicyArgs, TriggerRetryPolicyArgsDict]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        transport: Optional[
            pulumi.Input[Union[TriggerTransportArgs, TriggerTransportArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TriggerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[Union[TriggerDestinationArgs, TriggerDestinationArgsDict]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        event_data_content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        matching_criterias: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TriggerMatchingCriteriaArgs, TriggerMatchingCriteriaArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_policy: Optional[
            pulumi.Input[Union[TriggerRetryPolicyArgs, TriggerRetryPolicyArgsDict]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        transport: Optional[
            pulumi.Input[Union[TriggerTransportArgs, TriggerTransportArgsDict]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Trigger: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[outputs.TriggerDestination]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventDataContentType")
    def event_data_content_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchingCriterias")
    def matching_criterias(
        self,
    ) -> pulumi.Output[Sequence[outputs.TriggerMatchingCriteria]]: ...
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
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> pulumi.Output[Optional[outputs.TriggerRetryPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def transport(self) -> pulumi.Output[outputs.TriggerTransport]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
