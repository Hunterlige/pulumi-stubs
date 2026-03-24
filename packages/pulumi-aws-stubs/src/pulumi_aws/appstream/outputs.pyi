import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DirectoryConfigCertificateBasedAuthProperties",
    "DirectoryConfigServiceAccountCredentials",
    "FleetComputeCapacity",
    "FleetDomainJoinInfo",
    "FleetVpcConfig",
    "ImageBuilderAccessEndpoint",
    "ImageBuilderDomainJoinInfo",
    "ImageBuilderVpcConfig",
    "StackAccessEndpoint",
    "StackApplicationSettings",
    "StackStorageConnector",
    "StackStreamingExperienceSettings",
    "StackUserSetting",
    "GetImageApplicationResult",
    "GetImageApplicationIconS3LocationResult",
    "GetImageImagePermissionResult",
    "GetImageStateChangeReasonResult",
]

@pulumi.output_type
class DirectoryConfigCertificateBasedAuthProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectoryConfigServiceAccountCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, account_name: _builtins.str, account_password: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> _builtins.str: ...

@pulumi.output_type
class FleetComputeCapacity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        available: Optional[_builtins.int] = ...,
        desired_instances: Optional[_builtins.int] = ...,
        desired_sessions: Optional[_builtins.int] = ...,
        in_use: Optional[_builtins.int] = ...,
        running: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def available(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="desiredInstances")
    def desired_instances(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="desiredSessions")
    def desired_sessions(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inUse")
    def in_use(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def running(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FleetDomainJoinInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        directory_name: Optional[_builtins.str] = ...,
        organizational_unit_distinguished_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ImageBuilderAccessEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_type: _builtins.str,
        vpce_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageBuilderDomainJoinInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        directory_name: Optional[_builtins.str] = ...,
        organizational_unit_distinguished_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageBuilderVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackAccessEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_type: _builtins.str,
        vpce_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackApplicationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        settings_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="settingsGroup")
    def settings_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackStorageConnector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_type: _builtins.str,
        domains: Optional[Sequence[_builtins.str]] = ...,
        resource_identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackStreamingExperienceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, preferred_protocol: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredProtocol")
    def preferred_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StackUserSetting(dict):
    def __init__(
        __self__, *, action: _builtins.str, permission: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageApplicationResult(dict):
    def __init__(
        __self__,
        *,
        app_block_arn: _builtins.str,
        arn: _builtins.str,
        created_time: _builtins.str,
        description: _builtins.str,
        display_name: _builtins.str,
        enabled: _builtins.bool,
        icon_s3_locations: Sequence[outputs.GetImageApplicationIconS3LocationResult],
        icon_url: _builtins.str,
        instance_families: Sequence[_builtins.str],
        launch_parameters: _builtins.str,
        launch_path: _builtins.str,
        metadata: Mapping[str, _builtins.str],
        name: _builtins.str,
        platforms: Sequence[_builtins.str],
        working_directory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBlockArn")
    def app_block_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="iconS3Locations")
    def icon_s3_locations(
        self,
    ) -> Sequence[outputs.GetImageApplicationIconS3LocationResult]: ...
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceFamilies")
    def instance_families(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchParameters")
    def launch_parameters(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def platforms(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageApplicationIconS3LocationResult(dict):
    def __init__(
        __self__, *, s3_bucket: _builtins.str, s3_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageImagePermissionResult(dict):
    def __init__(
        __self__, *, allow_fleet: _builtins.bool, allow_image_builder: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowFleet")
    def allow_fleet(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowImageBuilder")
    def allow_image_builder(self) -> _builtins.bool: ...

@pulumi.output_type
class GetImageStateChangeReasonResult(dict):
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
