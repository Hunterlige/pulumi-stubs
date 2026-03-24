import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentBlueprintConfigurationArgs", "EnvironmentBlueprintConfiguration"]

@pulumi.input_type
class EnvironmentBlueprintConfigurationArgs:
    def __init__(
        __self__,
        *,
        domain_id: pulumi.Input[_builtins.str],
        enabled_regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        environment_blueprint_id: pulumi.Input[_builtins.str],
        manage_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_parameters: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[_builtins.str]: ...
    @domain_id.setter
    def domain_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enabledRegions")
    def enabled_regions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @enabled_regions.setter
    def enabled_regions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentBlueprintId")
    def environment_blueprint_id(self) -> pulumi.Input[_builtins.str]: ...
    @environment_blueprint_id.setter
    def environment_blueprint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="manageAccessRoleArn")
    def manage_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manage_access_role_arn.setter
    def manage_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningRoleArn")
    def provisioning_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalParameters")
    def regional_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
        ]
    ]: ...
    @regional_parameters.setter
    def regional_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...

@pulumi.input_type
class _EnvironmentBlueprintConfigurationState:
    def __init__(
        __self__,
        *,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_parameters: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enabledRegions")
    def enabled_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_regions.setter
    def enabled_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentBlueprintId")
    def environment_blueprint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_blueprint_id.setter
    def environment_blueprint_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="manageAccessRoleArn")
    def manage_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manage_access_role_arn.setter
    def manage_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningRoleArn")
    def provisioning_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalParameters")
    def regional_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
        ]
    ]: ...
    @regional_parameters.setter
    def regional_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...

@pulumi.type_token(...)
class EnvironmentBlueprintConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_parameters: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentBlueprintConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_parameters: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> EnvironmentBlueprintConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledRegions")
    def enabled_regions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentBlueprintId")
    def environment_blueprint_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manageAccessRoleArn")
    def manage_access_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningRoleArn")
    def provisioning_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionalParameters")
    def regional_parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, Mapping[str, _builtins.str]]]]: ...
