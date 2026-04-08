import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AFDOriginGroupArgs", "AFDOriginGroup"]

@pulumi.input_type
class AFDOriginGroupArgs:
    def __init__(
        __self__,
        *,
        profile_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        authentication: Optional[
            pulumi.Input[OriginAuthenticationPropertiesArgs]
        ] = ...,
        health_probe_settings: Optional[pulumi.Input[HealthProbeParametersArgs]] = ...,
        load_balancing_settings: Optional[
            pulumi.Input[LoadBalancingSettingsParametersArgs]
        ] = ...,
        origin_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity_state: Optional[
            pulumi.Input[Union[_builtins.str, EnabledState]]
        ] = ...,
        traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[pulumi.Input[OriginAuthenticationPropertiesArgs]]: ...
    @authentication.setter
    def authentication(
        self, value: Optional[pulumi.Input[OriginAuthenticationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(
        self,
    ) -> Optional[pulumi.Input[HealthProbeParametersArgs]]: ...
    @health_probe_settings.setter
    def health_probe_settings(
        self, value: Optional[pulumi.Input[HealthProbeParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(
        self,
    ) -> Optional[pulumi.Input[LoadBalancingSettingsParametersArgs]]: ...
    @load_balancing_settings.setter
    def load_balancing_settings(
        self, value: Optional[pulumi.Input[LoadBalancingSettingsParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_group_name.setter
    def origin_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinityState")
    def session_affinity_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnabledState]]]: ...
    @session_affinity_state.setter
    def session_affinity_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnabledState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @traffic_restoration_time_to_healed_or_new_endpoints_in_minutes.setter
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.type_token("azure-native:cdn:AFDOriginGroup")
class AFDOriginGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication: Optional[
            pulumi.Input[
                Union[
                    OriginAuthenticationPropertiesArgs,
                    OriginAuthenticationPropertiesArgsDict,
                ]
            ]
        ] = ...,
        health_probe_settings: Optional[
            pulumi.Input[
                Union[HealthProbeParametersArgs, HealthProbeParametersArgsDict]
            ]
        ] = ...,
        load_balancing_settings: Optional[
            pulumi.Input[
                Union[
                    LoadBalancingSettingsParametersArgs,
                    LoadBalancingSettingsParametersArgsDict,
                ]
            ]
        ] = ...,
        origin_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity_state: Optional[
            pulumi.Input[Union[_builtins.str, EnabledState]]
        ] = ...,
        traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AFDOriginGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AFDOriginGroup: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> pulumi.Output[Optional[outputs.OriginAuthenticationPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.HealthProbeParametersResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.LoadBalancingSettingsParametersResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinityState")
    def session_affinity_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
