import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CollectorPolicyArgs", "CollectorPolicy"]

@pulumi.input_type
class CollectorPolicyArgs:
    def __init__(
        __self__,
        *,
        azure_traffic_collector_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        collector_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        emission_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[EmissionPoliciesPropertiesFormatArgs]]]
        ] = ...,
        ingestion_policy: Optional[
            pulumi.Input[IngestionPolicyPropertiesFormatArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureTrafficCollectorName")
    def azure_traffic_collector_name(self) -> pulumi.Input[_builtins.str]: ...
    @azure_traffic_collector_name.setter
    def azure_traffic_collector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="collectorPolicyName")
    def collector_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collector_policy_name.setter
    def collector_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emissionPolicies")
    def emission_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EmissionPoliciesPropertiesFormatArgs]]]
    ]: ...
    @emission_policies.setter
    def emission_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EmissionPoliciesPropertiesFormatArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingestionPolicy")
    def ingestion_policy(
        self,
    ) -> Optional[pulumi.Input[IngestionPolicyPropertiesFormatArgs]]: ...
    @ingestion_policy.setter
    def ingestion_policy(
        self, value: Optional[pulumi.Input[IngestionPolicyPropertiesFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:networkfunction:CollectorPolicy")
class CollectorPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        azure_traffic_collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        collector_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        emission_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EmissionPoliciesPropertiesFormatArgs,
                            EmissionPoliciesPropertiesFormatArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        ingestion_policy: Optional[
            pulumi.Input[
                Union[
                    IngestionPolicyPropertiesFormatArgs,
                    IngestionPolicyPropertiesFormatArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CollectorPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CollectorPolicy: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emissionPolicies")
    def emission_policies(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.EmissionPoliciesPropertiesFormatResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionPolicy")
    def ingestion_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.IngestionPolicyPropertiesFormatResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
