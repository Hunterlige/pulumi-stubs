import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConfigurationProfileHCIAssignmentArgs", "ConfigurationProfileHCIAssignment"]

@pulumi.input_type
class ConfigurationProfileHCIAssignmentArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        configuration_profile_assignment_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        properties: Optional[
            pulumi.Input[ConfigurationProfileAssignmentPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationProfileAssignmentName")
    def configuration_profile_assignment_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_profile_assignment_name.setter
    def configuration_profile_assignment_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ConfigurationProfileAssignmentPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[pulumi.Input[ConfigurationProfileAssignmentPropertiesArgs]],
    ): ...

@pulumi.type_token(...)
class ConfigurationProfileHCIAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_profile_assignment_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    ConfigurationProfileAssignmentPropertiesArgs,
                    ConfigurationProfileAssignmentPropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConfigurationProfileHCIAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConfigurationProfileHCIAssignment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.ConfigurationProfileAssignmentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
