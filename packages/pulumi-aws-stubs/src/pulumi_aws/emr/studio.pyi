import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StudioArgs", "Studio"]

@pulumi.input_type
class StudioArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[_builtins.str],
        default_s3_location: pulumi.Input[_builtins.str],
        engine_security_group_id: pulumi.Input[_builtins.str],
        service_role: pulumi.Input[_builtins.str],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
        workspace_security_group_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_auth_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_relay_state_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input[_builtins.str]: ...
    @auth_mode.setter
    def auth_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultS3Location")
    def default_s3_location(self) -> pulumi.Input[_builtins.str]: ...
    @default_s3_location.setter
    def default_s3_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="engineSecurityGroupId")
    def engine_security_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @engine_security_group_id.setter
    def engine_security_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Input[_builtins.str]: ...
    @service_role.setter
    def service_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_security_group_id.setter
    def workspace_security_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpAuthUrl")
    def idp_auth_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_auth_url.setter
    def idp_auth_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_relay_state_parameter_name.setter
    def idp_relay_state_parameter_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="userRole")
    def user_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_role.setter
    def user_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _StudioState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_s3_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_auth_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_relay_state_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        user_role: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_mode.setter
    def auth_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultS3Location")
    def default_s3_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_s3_location.setter
    def default_s3_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineSecurityGroupId")
    def engine_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_security_group_id.setter
    def engine_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idpAuthUrl")
    def idp_auth_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_auth_url.setter
    def idp_auth_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_relay_state_parameter_name.setter
    def idp_relay_state_parameter_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userRole")
    def user_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_role.setter
    def user_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_security_group_id.setter
    def workspace_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:emr/studio:Studio")
class Studio(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_s3_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_auth_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_relay_state_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_role: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StudioArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_s3_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_auth_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_relay_state_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        user_role: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Studio: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultS3Location")
    def default_s3_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="engineSecurityGroupId")
    def engine_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="idpAuthUrl")
    def idp_auth_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userRole")
    def user_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
