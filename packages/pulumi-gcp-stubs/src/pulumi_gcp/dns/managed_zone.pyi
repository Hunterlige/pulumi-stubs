import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedZoneArgs", "ManagedZone"]

@pulumi.input_type
class ManagedZoneArgs:
    def __init__(
        __self__,
        *,
        dns_name: pulumi.Input[_builtins.str],
        cloud_logging_config: Optional[
            pulumi.Input[ManagedZoneCloudLoggingConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dnssec_config: Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        forwarding_config: Optional[
            pulumi.Input[ManagedZoneForwardingConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_config: Optional[pulumi.Input[ManagedZonePeeringConfigArgs]] = ...,
        private_visibility_config: Optional[
            pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reverse_lookup: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Input[_builtins.str]: ...
    @dns_name.setter
    def dns_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudLoggingConfig")
    def cloud_logging_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneCloudLoggingConfigArgs]]: ...
    @cloud_logging_config.setter
    def cloud_logging_config(
        self, value: Optional[pulumi.Input[ManagedZoneCloudLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnssecConfig")
    def dnssec_config(self) -> Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]]: ...
    @dnssec_config.setter
    def dnssec_config(
        self, value: Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingConfig")
    def forwarding_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneForwardingConfigArgs]]: ...
    @forwarding_config.setter
    def forwarding_config(
        self, value: Optional[pulumi.Input[ManagedZoneForwardingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZonePeeringConfigArgs]]: ...
    @peering_config.setter
    def peering_config(
        self, value: Optional[pulumi.Input[ManagedZonePeeringConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateVisibilityConfig")
    def private_visibility_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]]: ...
    @private_visibility_config.setter
    def private_visibility_config(
        self, value: Optional[pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reverseLookup")
    def reverse_lookup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reverse_lookup.setter
    def reverse_lookup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self, value: Optional[pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ManagedZoneState:
    def __init__(
        __self__,
        *,
        cloud_logging_config: Optional[
            pulumi.Input[ManagedZoneCloudLoggingConfigArgs]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dnssec_config: Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        forwarding_config: Optional[
            pulumi.Input[ManagedZoneForwardingConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        managed_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peering_config: Optional[pulumi.Input[ManagedZonePeeringConfigArgs]] = ...,
        private_visibility_config: Optional[
            pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reverse_lookup: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudLoggingConfig")
    def cloud_logging_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneCloudLoggingConfigArgs]]: ...
    @cloud_logging_config.setter
    def cloud_logging_config(
        self, value: Optional[pulumi.Input[ManagedZoneCloudLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnssecConfig")
    def dnssec_config(self) -> Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]]: ...
    @dnssec_config.setter
    def dnssec_config(
        self, value: Optional[pulumi.Input[ManagedZoneDnssecConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingConfig")
    def forwarding_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneForwardingConfigArgs]]: ...
    @forwarding_config.setter
    def forwarding_config(
        self, value: Optional[pulumi.Input[ManagedZoneForwardingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedZoneId")
    def managed_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_zone_id.setter
    def managed_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @name_servers.setter
    def name_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZonePeeringConfigArgs]]: ...
    @peering_config.setter
    def peering_config(
        self, value: Optional[pulumi.Input[ManagedZonePeeringConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateVisibilityConfig")
    def private_visibility_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]]: ...
    @private_visibility_config.setter
    def private_visibility_config(
        self, value: Optional[pulumi.Input[ManagedZonePrivateVisibilityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reverseLookup")
    def reverse_lookup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reverse_lookup.setter
    def reverse_lookup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self, value: Optional[pulumi.Input[ManagedZoneServiceDirectoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:dns/managedZone:ManagedZone")
class ManagedZone(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cloud_logging_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneCloudLoggingConfigArgs,
                    ManagedZoneCloudLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dnssec_config: Optional[
            pulumi.Input[
                Union[ManagedZoneDnssecConfigArgs, ManagedZoneDnssecConfigArgsDict]
            ]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        forwarding_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneForwardingConfigArgs, ManagedZoneForwardingConfigArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_config: Optional[
            pulumi.Input[
                Union[ManagedZonePeeringConfigArgs, ManagedZonePeeringConfigArgsDict]
            ]
        ] = ...,
        private_visibility_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZonePrivateVisibilityConfigArgs,
                    ManagedZonePrivateVisibilityConfigArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reverse_lookup: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_directory_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneServiceDirectoryConfigArgs,
                    ManagedZoneServiceDirectoryConfigArgsDict,
                ]
            ]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedZoneArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cloud_logging_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneCloudLoggingConfigArgs,
                    ManagedZoneCloudLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dnssec_config: Optional[
            pulumi.Input[
                Union[ManagedZoneDnssecConfigArgs, ManagedZoneDnssecConfigArgsDict]
            ]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        forwarding_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneForwardingConfigArgs, ManagedZoneForwardingConfigArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        managed_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peering_config: Optional[
            pulumi.Input[
                Union[ManagedZonePeeringConfigArgs, ManagedZonePeeringConfigArgsDict]
            ]
        ] = ...,
        private_visibility_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZonePrivateVisibilityConfigArgs,
                    ManagedZonePrivateVisibilityConfigArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reverse_lookup: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_directory_config: Optional[
            pulumi.Input[
                Union[
                    ManagedZoneServiceDirectoryConfigArgs,
                    ManagedZoneServiceDirectoryConfigArgsDict,
                ]
            ]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ManagedZone: ...
    @_builtins.property
    @pulumi.getter(name="cloudLoggingConfig")
    def cloud_logging_config(
        self,
    ) -> pulumi.Output[outputs.ManagedZoneCloudLoggingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnssecConfig")
    def dnssec_config(self) -> pulumi.Output[outputs.ManagedZoneDnssecConfig]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingConfig")
    def forwarding_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedZoneForwardingConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="managedZoneId")
    def managed_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="peeringConfig")
    def peering_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedZonePeeringConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="privateVisibilityConfig")
    def private_visibility_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedZonePrivateVisibilityConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reverseLookup")
    def reverse_lookup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedZoneServiceDirectoryConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional[_builtins.str]]: ...
