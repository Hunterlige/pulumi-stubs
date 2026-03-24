import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceArgs", "Instance"]

@pulumi.input_type
class InstanceArgs:
    def __init__(
        __self__,
        *,
        oauth_config: pulumi.Input[InstanceOauthConfigArgs],
        admin_settings: Optional[pulumi.Input[InstanceAdminSettingsArgs]] = ...,
        consumer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        controlled_egress_config: Optional[
            pulumi.Input[InstanceControlledEgressConfigArgs]
        ] = ...,
        controlled_egress_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_domain: Optional[pulumi.Input[InstanceCustomDomainArgs]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_maintenance_period: Optional[
            pulumi.Input[InstanceDenyMaintenancePeriodArgs]
        ] = ...,
        encryption_config: Optional[pulumi.Input[InstanceEncryptionConfigArgs]] = ...,
        fips_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[pulumi.Input[InstanceMaintenanceWindowArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        periodic_export_config: Optional[
            pulumi.Input[InstancePeriodicExportConfigArgs]
        ] = ...,
        platform_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[pulumi.Input[InstancePscConfigArgs]] = ...,
        psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_range: Optional[pulumi.Input[_builtins.str]] = ...,
        user_metadata: Optional[pulumi.Input[InstanceUserMetadataArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> pulumi.Input[InstanceOauthConfigArgs]: ...
    @oauth_config.setter
    def oauth_config(self, value: pulumi.Input[InstanceOauthConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="adminSettings")
    def admin_settings(self) -> Optional[pulumi.Input[InstanceAdminSettingsArgs]]: ...
    @admin_settings.setter
    def admin_settings(
        self, value: Optional[pulumi.Input[InstanceAdminSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_network.setter
    def consumer_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressConfig")
    def controlled_egress_config(
        self,
    ) -> Optional[pulumi.Input[InstanceControlledEgressConfigArgs]]: ...
    @controlled_egress_config.setter
    def controlled_egress_config(
        self, value: Optional[pulumi.Input[InstanceControlledEgressConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressEnabled")
    def controlled_egress_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @controlled_egress_enabled.setter
    def controlled_egress_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input[InstanceCustomDomainArgs]]: ...
    @custom_domain.setter
    def custom_domain(
        self, value: Optional[pulumi.Input[InstanceCustomDomainArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriod")
    def deny_maintenance_period(
        self,
    ) -> Optional[pulumi.Input[InstanceDenyMaintenancePeriodArgs]]: ...
    @deny_maintenance_period.setter
    def deny_maintenance_period(
        self, value: Optional[pulumi.Input[InstanceDenyMaintenancePeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[InstanceEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[InstanceEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fipsEnabled")
    def fips_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fips_enabled.setter
    def fips_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="geminiEnabled")
    def gemini_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gemini_enabled.setter
    def gemini_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[InstanceMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[InstanceMaintenanceWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="periodicExportConfig")
    def periodic_export_config(
        self,
    ) -> Optional[pulumi.Input[InstancePeriodicExportConfigArgs]]: ...
    @periodic_export_config.setter
    def periodic_export_config(
        self, value: Optional[pulumi.Input[InstancePeriodicExportConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformEdition")
    def platform_edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_edition.setter
    def platform_edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpEnabled")
    def private_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_ip_enabled.setter
    def private_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[InstancePscConfigArgs]]: ...
    @psc_config.setter
    def psc_config(self, value: Optional[pulumi.Input[InstancePscConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @psc_enabled.setter
    def psc_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpEnabled")
    def public_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @public_ip_enabled.setter
    def public_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedRange")
    def reserved_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_range.setter
    def reserved_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[pulumi.Input[InstanceUserMetadataArgs]]: ...
    @user_metadata.setter
    def user_metadata(
        self, value: Optional[pulumi.Input[InstanceUserMetadataArgs]]
    ): ...

@pulumi.input_type
class _InstanceState:
    def __init__(
        __self__,
        *,
        admin_settings: Optional[pulumi.Input[InstanceAdminSettingsArgs]] = ...,
        consumer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        controlled_egress_config: Optional[
            pulumi.Input[InstanceControlledEgressConfigArgs]
        ] = ...,
        controlled_egress_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[pulumi.Input[InstanceCustomDomainArgs]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_maintenance_period: Optional[
            pulumi.Input[InstanceDenyMaintenancePeriodArgs]
        ] = ...,
        egress_public_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[pulumi.Input[InstanceEncryptionConfigArgs]] = ...,
        fips_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress_private_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_public_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        looker_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        looker_version: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[pulumi.Input[InstanceMaintenanceWindowArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_config: Optional[pulumi.Input[InstanceOauthConfigArgs]] = ...,
        periodic_export_config: Optional[
            pulumi.Input[InstancePeriodicExportConfigArgs]
        ] = ...,
        platform_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[pulumi.Input[InstancePscConfigArgs]] = ...,
        psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_range: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user_metadata: Optional[pulumi.Input[InstanceUserMetadataArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminSettings")
    def admin_settings(self) -> Optional[pulumi.Input[InstanceAdminSettingsArgs]]: ...
    @admin_settings.setter
    def admin_settings(
        self, value: Optional[pulumi.Input[InstanceAdminSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_network.setter
    def consumer_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressConfig")
    def controlled_egress_config(
        self,
    ) -> Optional[pulumi.Input[InstanceControlledEgressConfigArgs]]: ...
    @controlled_egress_config.setter
    def controlled_egress_config(
        self, value: Optional[pulumi.Input[InstanceControlledEgressConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressEnabled")
    def controlled_egress_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @controlled_egress_enabled.setter
    def controlled_egress_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input[InstanceCustomDomainArgs]]: ...
    @custom_domain.setter
    def custom_domain(
        self, value: Optional[pulumi.Input[InstanceCustomDomainArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriod")
    def deny_maintenance_period(
        self,
    ) -> Optional[pulumi.Input[InstanceDenyMaintenancePeriodArgs]]: ...
    @deny_maintenance_period.setter
    def deny_maintenance_period(
        self, value: Optional[pulumi.Input[InstanceDenyMaintenancePeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressPublicIp")
    def egress_public_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress_public_ip.setter
    def egress_public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[InstanceEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[InstanceEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fipsEnabled")
    def fips_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fips_enabled.setter
    def fips_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="geminiEnabled")
    def gemini_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gemini_enabled.setter
    def gemini_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressPrivateIp")
    def ingress_private_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_private_ip.setter
    def ingress_private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressPublicIp")
    def ingress_public_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_public_ip.setter
    def ingress_public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookerUri")
    def looker_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @looker_uri.setter
    def looker_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookerVersion")
    def looker_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @looker_version.setter
    def looker_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[InstanceMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[InstanceMaintenanceWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[pulumi.Input[InstanceOauthConfigArgs]]: ...
    @oauth_config.setter
    def oauth_config(self, value: Optional[pulumi.Input[InstanceOauthConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="periodicExportConfig")
    def periodic_export_config(
        self,
    ) -> Optional[pulumi.Input[InstancePeriodicExportConfigArgs]]: ...
    @periodic_export_config.setter
    def periodic_export_config(
        self, value: Optional[pulumi.Input[InstancePeriodicExportConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformEdition")
    def platform_edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_edition.setter
    def platform_edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpEnabled")
    def private_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_ip_enabled.setter
    def private_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[InstancePscConfigArgs]]: ...
    @psc_config.setter
    def psc_config(self, value: Optional[pulumi.Input[InstancePscConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @psc_enabled.setter
    def psc_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpEnabled")
    def public_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @public_ip_enabled.setter
    def public_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedRange")
    def reserved_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_range.setter
    def reserved_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[pulumi.Input[InstanceUserMetadataArgs]]: ...
    @user_metadata.setter
    def user_metadata(
        self, value: Optional[pulumi.Input[InstanceUserMetadataArgs]]
    ): ...

@pulumi.type_token("gcp:looker/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_settings: Optional[
            pulumi.Input[
                Union[InstanceAdminSettingsArgs, InstanceAdminSettingsArgsDict]
            ]
        ] = ...,
        consumer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        controlled_egress_config: Optional[
            pulumi.Input[
                Union[
                    InstanceControlledEgressConfigArgs,
                    InstanceControlledEgressConfigArgsDict,
                ]
            ]
        ] = ...,
        controlled_egress_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_domain: Optional[
            pulumi.Input[Union[InstanceCustomDomainArgs, InstanceCustomDomainArgsDict]]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_maintenance_period: Optional[
            pulumi.Input[
                Union[
                    InstanceDenyMaintenancePeriodArgs,
                    InstanceDenyMaintenancePeriodArgsDict,
                ]
            ]
        ] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[InstanceEncryptionConfigArgs, InstanceEncryptionConfigArgsDict]
            ]
        ] = ...,
        fips_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[
            pulumi.Input[
                Union[InstanceMaintenanceWindowArgs, InstanceMaintenanceWindowArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_config: Optional[
            pulumi.Input[Union[InstanceOauthConfigArgs, InstanceOauthConfigArgsDict]]
        ] = ...,
        periodic_export_config: Optional[
            pulumi.Input[
                Union[
                    InstancePeriodicExportConfigArgs,
                    InstancePeriodicExportConfigArgsDict,
                ]
            ]
        ] = ...,
        platform_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[
            pulumi.Input[Union[InstancePscConfigArgs, InstancePscConfigArgsDict]]
        ] = ...,
        psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_range: Optional[pulumi.Input[_builtins.str]] = ...,
        user_metadata: Optional[
            pulumi.Input[Union[InstanceUserMetadataArgs, InstanceUserMetadataArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_settings: Optional[
            pulumi.Input[
                Union[InstanceAdminSettingsArgs, InstanceAdminSettingsArgsDict]
            ]
        ] = ...,
        consumer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        controlled_egress_config: Optional[
            pulumi.Input[
                Union[
                    InstanceControlledEgressConfigArgs,
                    InstanceControlledEgressConfigArgsDict,
                ]
            ]
        ] = ...,
        controlled_egress_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain: Optional[
            pulumi.Input[Union[InstanceCustomDomainArgs, InstanceCustomDomainArgsDict]]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_maintenance_period: Optional[
            pulumi.Input[
                Union[
                    InstanceDenyMaintenancePeriodArgs,
                    InstanceDenyMaintenancePeriodArgsDict,
                ]
            ]
        ] = ...,
        egress_public_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[InstanceEncryptionConfigArgs, InstanceEncryptionConfigArgsDict]
            ]
        ] = ...,
        fips_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        gemini_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress_private_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_public_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        looker_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        looker_version: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[
                Union[InstanceMaintenanceWindowArgs, InstanceMaintenanceWindowArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_config: Optional[
            pulumi.Input[Union[InstanceOauthConfigArgs, InstanceOauthConfigArgsDict]]
        ] = ...,
        periodic_export_config: Optional[
            pulumi.Input[
                Union[
                    InstancePeriodicExportConfigArgs,
                    InstancePeriodicExportConfigArgsDict,
                ]
            ]
        ] = ...,
        platform_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[
            pulumi.Input[Union[InstancePscConfigArgs, InstancePscConfigArgsDict]]
        ] = ...,
        psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        public_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_range: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user_metadata: Optional[
            pulumi.Input[Union[InstanceUserMetadataArgs, InstanceUserMetadataArgsDict]]
        ] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter(name="adminSettings")
    def admin_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceAdminSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressConfig")
    def controlled_egress_config(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceControlledEgressConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="controlledEgressEnabled")
    def controlled_egress_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceCustomDomain]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriod")
    def deny_maintenance_period(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceDenyMaintenancePeriod]]: ...
    @_builtins.property
    @pulumi.getter(name="egressPublicIp")
    def egress_public_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[outputs.InstanceEncryptionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fipsEnabled")
    def fips_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="geminiEnabled")
    def gemini_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPrivateIp")
    def ingress_private_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressPublicIp")
    def ingress_public_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lookerUri")
    def looker_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lookerVersion")
    def looker_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceMaintenanceWindow]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> pulumi.Output[outputs.InstanceOauthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="periodicExportConfig")
    def periodic_export_config(
        self,
    ) -> pulumi.Output[Optional[outputs.InstancePeriodicExportConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="platformEdition")
    def platform_edition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpEnabled")
    def private_ip_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> pulumi.Output[outputs.InstancePscConfig]: ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpEnabled")
    def public_ip_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservedRange")
    def reserved_range(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceUserMetadata]]: ...
