import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineInstanceArgs", "VirtualMachineInstance"]

@pulumi.input_type
class VirtualMachineInstanceArgs:
    def __init__(
        __self__,
        *,
        resource_uri: pulumi.Input[_builtins.str],
        create_from_local: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        hardware_profile: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesHardwareProfileArgs]
        ] = ...,
        http_proxy_config: Optional[pulumi.Input[HttpProxyConfigurationArgs]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        network_profile: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesNetworkProfileArgs]
        ] = ...,
        os_profile: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesOsProfileArgs]
        ] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesSecurityProfileArgs]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesStorageProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_from_local.setter
    def create_from_local(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineInstancePropertiesHardwareProfileArgs]
    ]: ...
    @hardware_profile.setter
    def hardware_profile(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesHardwareProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(
        self,
    ) -> Optional[pulumi.Input[HttpProxyConfigurationArgs]]: ...
    @http_proxy_config.setter
    def http_proxy_config(
        self, value: Optional[pulumi.Input[HttpProxyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineInstancePropertiesNetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesNetworkProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineInstancePropertiesOsProfileArgs]]: ...
    @os_profile.setter
    def os_profile(
        self,
        value: Optional[pulumi.Input[VirtualMachineInstancePropertiesOsProfileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_uid.setter
    def resource_uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineInstancePropertiesSecurityProfileArgs]
    ]: ...
    @security_profile.setter
    def security_profile(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesSecurityProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineInstancePropertiesStorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineInstancePropertiesStorageProfileArgs]
        ],
    ): ...

@pulumi.type_token("azure-native:azurestackhci:VirtualMachineInstance")
class VirtualMachineInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_from_local: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        hardware_profile: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineInstancePropertiesHardwareProfileArgs,
                    VirtualMachineInstancePropertiesHardwareProfileArgsDict,
                ]
            ]
        ] = ...,
        http_proxy_config: Optional[
            pulumi.Input[
                Union[HttpProxyConfigurationArgs, HttpProxyConfigurationArgsDict]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        network_profile: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineInstancePropertiesNetworkProfileArgs,
                    VirtualMachineInstancePropertiesNetworkProfileArgsDict,
                ]
            ]
        ] = ...,
        os_profile: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineInstancePropertiesOsProfileArgs,
                    VirtualMachineInstancePropertiesOsProfileArgsDict,
                ]
            ]
        ] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineInstancePropertiesSecurityProfileArgs,
                    VirtualMachineInstancePropertiesSecurityProfileArgsDict,
                ]
            ]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineInstancePropertiesStorageProfileArgs,
                    VirtualMachineInstancePropertiesStorageProfileArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineInstance: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="guestAgentInstallStatus")
    def guest_agent_install_status(
        self,
    ) -> pulumi.Output[Optional[outputs.GuestAgentInstallStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineInstancePropertiesHardwareProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.HttpProxyConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(
        self,
    ) -> pulumi.Output[outputs.VirtualMachineInstanceViewResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineInstancePropertiesNetworkProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineInstancePropertiesOsProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineInstancePropertiesSecurityProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.VirtualMachineInstanceStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineInstancePropertiesStorageProfileResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[_builtins.str]: ...
