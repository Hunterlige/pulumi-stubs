import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PublicCloudConnectorArgs", "PublicCloudConnector"]

@pulumi.input_type
class PublicCloudConnectorArgs:
    def __init__(
        __self__,
        *,
        aws_cloud_profile: pulumi.Input[AwsCloudProfileArgs],
        host_type: pulumi.Input[Union[_builtins.str, HostType]],
        resource_group_name: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_cloud_connector: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsCloudProfile")
    def aws_cloud_profile(self) -> pulumi.Input[AwsCloudProfileArgs]: ...
    @aws_cloud_profile.setter
    def aws_cloud_profile(self, value: pulumi.Input[AwsCloudProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Input[Union[_builtins.str, HostType]]: ...
    @host_type.setter
    def host_type(self, value: pulumi.Input[Union[_builtins.str, HostType]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicCloudConnector")
    def public_cloud_connector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_cloud_connector.setter
    def public_cloud_connector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class PublicCloudConnector(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_cloud_profile: Optional[
            pulumi.Input[Union[AwsCloudProfileArgs, AwsCloudProfileArgsDict]]
        ] = ...,
        host_type: Optional[pulumi.Input[Union[_builtins.str, HostType]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_cloud_connector: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PublicCloudConnectorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PublicCloudConnector: ...
    @_builtins.property
    @pulumi.getter(name="awsCloudProfile")
    def aws_cloud_profile(self) -> pulumi.Output[outputs.AwsCloudProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorPrimaryIdentifier")
    def connector_primary_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Output[_builtins.str]: ...
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
