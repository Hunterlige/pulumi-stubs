import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DirectoryConfigCertificateBasedAuthPropertiesArgs",
    ...,
    "DirectoryConfigServiceAccountCredentialsArgs",
    "DirectoryConfigServiceAccountCredentialsArgsDict",
    "FleetComputeCapacityArgs",
    "FleetComputeCapacityArgsDict",
    "FleetDomainJoinInfoArgs",
    "FleetDomainJoinInfoArgsDict",
    "FleetVpcConfigArgs",
    "FleetVpcConfigArgsDict",
    "ImageBuilderAccessEndpointArgs",
    "ImageBuilderAccessEndpointArgsDict",
    "ImageBuilderDomainJoinInfoArgs",
    "ImageBuilderDomainJoinInfoArgsDict",
    "ImageBuilderVpcConfigArgs",
    "ImageBuilderVpcConfigArgsDict",
    "StackAccessEndpointArgs",
    "StackAccessEndpointArgsDict",
    "StackApplicationSettingsArgs",
    "StackApplicationSettingsArgsDict",
    "StackStorageConnectorArgs",
    "StackStorageConnectorArgsDict",
    "StackStreamingExperienceSettingsArgs",
    "StackStreamingExperienceSettingsArgsDict",
    "StackUserSettingArgs",
    "StackUserSettingArgsDict",
]

class DirectoryConfigCertificateBasedAuthPropertiesArgsDict(TypedDict):
    certificate_authority_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DirectoryConfigCertificateBasedAuthPropertiesArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority_arn.setter
    def certificate_authority_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DirectoryConfigServiceAccountCredentialsArgsDict(TypedDict):
    account_name: pulumi.Input[_builtins.str]
    account_password: pulumi.Input[_builtins.str]

@pulumi.input_type
class DirectoryConfigServiceAccountCredentialsArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        account_password: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> pulumi.Input[_builtins.str]: ...
    @account_password.setter
    def account_password(self, value: pulumi.Input[_builtins.str]): ...

class FleetComputeCapacityArgsDict(TypedDict):
    available: NotRequired[pulumi.Input[_builtins.int]]
    desired_instances: NotRequired[pulumi.Input[_builtins.int]]
    desired_sessions: NotRequired[pulumi.Input[_builtins.int]]
    in_use: NotRequired[pulumi.Input[_builtins.int]]
    running: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FleetComputeCapacityArgs:
    def __init__(
        __self__,
        *,
        available: Optional[pulumi.Input[_builtins.int]] = ...,
        desired_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        desired_sessions: Optional[pulumi.Input[_builtins.int]] = ...,
        in_use: Optional[pulumi.Input[_builtins.int]] = ...,
        running: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def available(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @available.setter
    def available(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredInstances")
    def desired_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_instances.setter
    def desired_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredSessions")
    def desired_sessions(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_sessions.setter
    def desired_sessions(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inUse")
    def in_use(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @in_use.setter
    def in_use(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def running(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @running.setter
    def running(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FleetDomainJoinInfoArgsDict(TypedDict):
    directory_name: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FleetDomainJoinInfoArgs:
    def __init__(
        __self__,
        *,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_distinguished_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FleetVpcConfigArgsDict(TypedDict):
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FleetVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ImageBuilderAccessEndpointArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    vpce_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageBuilderAccessEndpointArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        vpce_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpce_id.setter
    def vpce_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageBuilderDomainJoinInfoArgsDict(TypedDict):
    directory_name: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageBuilderDomainJoinInfoArgs:
    def __init__(
        __self__,
        *,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_distinguished_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ImageBuilderVpcConfigArgsDict(TypedDict):
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ImageBuilderVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class StackAccessEndpointArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    vpce_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StackAccessEndpointArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        vpce_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpce_id.setter
    def vpce_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StackApplicationSettingsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    settings_group: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StackApplicationSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        settings_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="settingsGroup")
    def settings_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @settings_group.setter
    def settings_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StackStorageConnectorArgsDict(TypedDict):
    connector_type: pulumi.Input[_builtins.str]
    domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StackStorageConnectorArgs:
    def __init__(
        __self__,
        *,
        connector_type: pulumi.Input[_builtins.str],
        domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        resource_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[_builtins.str]: ...
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domains.setter
    def domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StackStreamingExperienceSettingsArgsDict(TypedDict):
    preferred_protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StackStreamingExperienceSettingsArgs:
    def __init__(
        __self__, *, preferred_protocol: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredProtocol")
    def preferred_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_protocol.setter
    def preferred_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StackUserSettingArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    permission: pulumi.Input[_builtins.str]

@pulumi.input_type
class StackUserSettingArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        permission: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]: ...
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): ...
