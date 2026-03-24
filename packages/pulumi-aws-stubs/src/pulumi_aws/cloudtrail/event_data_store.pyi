import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EventDataStoreArgs", "EventDataStore"]

@pulumi.input_type
class EventDataStoreArgs:
    def __init__(
        __self__,
        *,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]
            ]
        ] = ...,
        billing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        suspend: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]]
    ]: ...
    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionEnabled")
    def multi_region_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_region_enabled.setter
    def multi_region_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationEnabled")
    def organization_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @organization_enabled.setter
    def organization_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def suspend(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suspend.setter
    def suspend(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @termination_protection_enabled.setter
    def termination_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _EventDataStoreState:
    def __init__(
        __self__,
        *,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        suspend: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]]
    ]: ...
    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionEnabled")
    def multi_region_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_region_enabled.setter
    def multi_region_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationEnabled")
    def organization_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @organization_enabled.setter
    def organization_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def suspend(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suspend.setter
    def suspend(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @termination_protection_enabled.setter
    def termination_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token("aws:cloudtrail/eventDataStore:EventDataStore")
class EventDataStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventDataStoreAdvancedEventSelectorArgs,
                            EventDataStoreAdvancedEventSelectorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        billing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        suspend: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[EventDataStoreArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_event_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventDataStoreAdvancedEventSelectorArgs,
                            EventDataStoreAdvancedEventSelectorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        suspend: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> EventDataStore: ...
    @_builtins.property
    @pulumi.getter(name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> pulumi.Output[Sequence[outputs.EventDataStoreAdvancedEventSelector]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionEnabled")
    def multi_region_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationEnabled")
    def organization_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def suspend(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
