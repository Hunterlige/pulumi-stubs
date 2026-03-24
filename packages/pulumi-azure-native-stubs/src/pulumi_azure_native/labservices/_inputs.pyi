

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoShutdownProfileArgs', 'AutoShutdownProfileArgsDict', 'ConnectionProfileArgs', 'ConnectionProfileArgsDict', 'CredentialsArgs', 'CredentialsArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'ImageReferenceArgs', 'ImageReferenceArgsDict', 'LabNetworkProfileArgs', 'LabNetworkProfileArgsDict', 'LabPlanNetworkProfileArgs', 'LabPlanNetworkProfileArgsDict', 'RecurrencePatternArgs', 'RecurrencePatternArgsDict', 'RosterProfileArgs', 'RosterProfileArgsDict', 'SecurityProfileArgs', 'SecurityProfileArgsDict', 'SkuArgs', 'SkuArgsDict', 'SupportInfoArgs', 'SupportInfoArgsDict', 'VirtualMachineAdditionalCapabilitiesArgs', 'VirtualMachineAdditionalCapabilitiesArgsDict', 'VirtualMachineProfileArgs', 'VirtualMachineProfileArgsDict']
class AutoShutdownProfileArgsDict(TypedDict):
    
    disconnect_delay: NotRequired[pulumi.Input[_builtins.str]]
    idle_delay: NotRequired[pulumi.Input[_builtins.str]]
    no_connect_delay: NotRequired[pulumi.Input[_builtins.str]]
    shutdown_on_disconnect: NotRequired[pulumi.Input[EnableState]]
    shutdown_on_idle: NotRequired[pulumi.Input[ShutdownOnIdleMode]]
    shutdown_when_not_connected: NotRequired[pulumi.Input[EnableState]]


@pulumi.input_type
class AutoShutdownProfileArgs:
    def __init__(__self__, *, disconnect_delay: Optional[pulumi.Input[_builtins.str]] = ..., idle_delay: Optional[pulumi.Input[_builtins.str]] = ..., no_connect_delay: Optional[pulumi.Input[_builtins.str]] = ..., shutdown_on_disconnect: Optional[pulumi.Input[EnableState]] = ..., shutdown_on_idle: Optional[pulumi.Input[ShutdownOnIdleMode]] = ..., shutdown_when_not_connected: Optional[pulumi.Input[EnableState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectDelay")
    def disconnect_delay(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disconnect_delay.setter
    def disconnect_delay(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDelay")
    def idle_delay(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @idle_delay.setter
    def idle_delay(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noConnectDelay")
    def no_connect_delay(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_connect_delay.setter
    def no_connect_delay(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownOnDisconnect")
    def shutdown_on_disconnect(self) -> Optional[pulumi.Input[EnableState]]:
        
        ...
    
    @shutdown_on_disconnect.setter
    def shutdown_on_disconnect(self, value: Optional[pulumi.Input[EnableState]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownOnIdle")
    def shutdown_on_idle(self) -> Optional[pulumi.Input[ShutdownOnIdleMode]]:
        
        ...
    
    @shutdown_on_idle.setter
    def shutdown_on_idle(self, value: Optional[pulumi.Input[ShutdownOnIdleMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownWhenNotConnected")
    def shutdown_when_not_connected(self) -> Optional[pulumi.Input[EnableState]]:
        
        ...
    
    @shutdown_when_not_connected.setter
    def shutdown_when_not_connected(self, value: Optional[pulumi.Input[EnableState]]): # -> None:
        ...
    


class ConnectionProfileArgsDict(TypedDict):
    
    client_rdp_access: NotRequired[pulumi.Input[ConnectionType]]
    client_ssh_access: NotRequired[pulumi.Input[ConnectionType]]
    web_rdp_access: NotRequired[pulumi.Input[ConnectionType]]
    web_ssh_access: NotRequired[pulumi.Input[ConnectionType]]


@pulumi.input_type
class ConnectionProfileArgs:
    def __init__(__self__, *, client_rdp_access: Optional[pulumi.Input[ConnectionType]] = ..., client_ssh_access: Optional[pulumi.Input[ConnectionType]] = ..., web_rdp_access: Optional[pulumi.Input[ConnectionType]] = ..., web_ssh_access: Optional[pulumi.Input[ConnectionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientRdpAccess")
    def client_rdp_access(self) -> Optional[pulumi.Input[ConnectionType]]:
        
        ...
    
    @client_rdp_access.setter
    def client_rdp_access(self, value: Optional[pulumi.Input[ConnectionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSshAccess")
    def client_ssh_access(self) -> Optional[pulumi.Input[ConnectionType]]:
        
        ...
    
    @client_ssh_access.setter
    def client_ssh_access(self, value: Optional[pulumi.Input[ConnectionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webRdpAccess")
    def web_rdp_access(self) -> Optional[pulumi.Input[ConnectionType]]:
        
        ...
    
    @web_rdp_access.setter
    def web_rdp_access(self, value: Optional[pulumi.Input[ConnectionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSshAccess")
    def web_ssh_access(self) -> Optional[pulumi.Input[ConnectionType]]:
        
        ...
    
    @web_ssh_access.setter
    def web_ssh_access(self, value: Optional[pulumi.Input[ConnectionType]]): # -> None:
        ...
    


class CredentialsArgsDict(TypedDict):
    
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CredentialsArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    


class ImageReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    offer: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImageReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., offer: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LabNetworkProfileArgsDict(TypedDict):
    
    load_balancer_id: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_id: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LabNetworkProfileArgs:
    def __init__(__self__, *, load_balancer_id: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_id.setter
    def load_balancer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_id.setter
    def public_ip_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LabPlanNetworkProfileArgsDict(TypedDict):
    
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LabPlanNetworkProfileArgs:
    def __init__(__self__, *, subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RecurrencePatternArgsDict(TypedDict):
    
    expiration_date: pulumi.Input[_builtins.str]
    frequency: pulumi.Input[RecurrenceFrequency]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    week_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[WeekDay]]]]


@pulumi.input_type
class RecurrencePatternArgs:
    def __init__(__self__, *, expiration_date: pulumi.Input[_builtins.str], frequency: pulumi.Input[RecurrenceFrequency], interval: Optional[pulumi.Input[_builtins.int]] = ..., week_days: Optional[pulumi.Input[Sequence[pulumi.Input[WeekDay]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expiration_date.setter
    def expiration_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[RecurrenceFrequency]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: pulumi.Input[RecurrenceFrequency]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WeekDay]]]]:
        
        ...
    
    @week_days.setter
    def week_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WeekDay]]]]): # -> None:
        ...
    


class RosterProfileArgsDict(TypedDict):
    
    active_directory_group_id: NotRequired[pulumi.Input[_builtins.str]]
    lms_instance: NotRequired[pulumi.Input[_builtins.str]]
    lti_client_id: NotRequired[pulumi.Input[_builtins.str]]
    lti_context_id: NotRequired[pulumi.Input[_builtins.str]]
    lti_roster_endpoint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RosterProfileArgs:
    def __init__(__self__, *, active_directory_group_id: Optional[pulumi.Input[_builtins.str]] = ..., lms_instance: Optional[pulumi.Input[_builtins.str]] = ..., lti_client_id: Optional[pulumi.Input[_builtins.str]] = ..., lti_context_id: Optional[pulumi.Input[_builtins.str]] = ..., lti_roster_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryGroupId")
    def active_directory_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_group_id.setter
    def active_directory_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lmsInstance")
    def lms_instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lms_instance.setter
    def lms_instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiClientId")
    def lti_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lti_client_id.setter
    def lti_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiContextId")
    def lti_context_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lti_context_id.setter
    def lti_context_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiRosterEndpoint")
    def lti_roster_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lti_roster_endpoint.setter
    def lti_roster_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityProfileArgsDict(TypedDict):
    
    open_access: NotRequired[pulumi.Input[EnableState]]


@pulumi.input_type
class SecurityProfileArgs:
    def __init__(__self__, *, open_access: Optional[pulumi.Input[EnableState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAccess")
    def open_access(self) -> Optional[pulumi.Input[EnableState]]:
        
        ...
    
    @open_access.setter
    def open_access(self, value: Optional[pulumi.Input[EnableState]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    


class SupportInfoArgsDict(TypedDict):
    
    email: NotRequired[pulumi.Input[_builtins.str]]
    instructions: NotRequired[pulumi.Input[_builtins.str]]
    phone: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SupportInfoArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., instructions: Optional[pulumi.Input[_builtins.str]] = ..., phone: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instructions.setter
    def instructions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone.setter
    def phone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineAdditionalCapabilitiesArgsDict(TypedDict):
    
    install_gpu_drivers: NotRequired[pulumi.Input[EnableState]]


@pulumi.input_type
class VirtualMachineAdditionalCapabilitiesArgs:
    def __init__(__self__, *, install_gpu_drivers: Optional[pulumi.Input[EnableState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installGpuDrivers")
    def install_gpu_drivers(self) -> Optional[pulumi.Input[EnableState]]:
        
        ...
    
    @install_gpu_drivers.setter
    def install_gpu_drivers(self, value: Optional[pulumi.Input[EnableState]]): # -> None:
        ...
    


class VirtualMachineProfileArgsDict(TypedDict):
    
    admin_user: pulumi.Input[CredentialsArgsDict]
    create_option: pulumi.Input[CreateOption]
    image_reference: pulumi.Input[ImageReferenceArgsDict]
    sku: pulumi.Input[SkuArgsDict]
    usage_quota: pulumi.Input[_builtins.str]
    additional_capabilities: NotRequired[pulumi.Input[VirtualMachineAdditionalCapabilitiesArgsDict]]
    non_admin_user: NotRequired[pulumi.Input[CredentialsArgsDict]]
    use_shared_password: NotRequired[pulumi.Input[EnableState]]


@pulumi.input_type
class VirtualMachineProfileArgs:
    def __init__(__self__, *, admin_user: pulumi.Input[CredentialsArgs], create_option: pulumi.Input[CreateOption], image_reference: pulumi.Input[ImageReferenceArgs], sku: pulumi.Input[SkuArgs], usage_quota: pulumi.Input[_builtins.str], additional_capabilities: Optional[pulumi.Input[VirtualMachineAdditionalCapabilitiesArgs]] = ..., non_admin_user: Optional[pulumi.Input[CredentialsArgs]] = ..., use_shared_password: Optional[pulumi.Input[EnableState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> pulumi.Input[CredentialsArgs]:
        
        ...
    
    @admin_user.setter
    def admin_user(self, value: pulumi.Input[CredentialsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[CreateOption]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[CreateOption]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Input[ImageReferenceArgs]:
        
        ...
    
    @image_reference.setter
    def image_reference(self, value: pulumi.Input[ImageReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageQuota")
    def usage_quota(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @usage_quota.setter
    def usage_quota(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[pulumi.Input[VirtualMachineAdditionalCapabilitiesArgs]]:
        
        ...
    
    @additional_capabilities.setter
    def additional_capabilities(self, value: Optional[pulumi.Input[VirtualMachineAdditionalCapabilitiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAdminUser")
    def non_admin_user(self) -> Optional[pulumi.Input[CredentialsArgs]]:
        
        ...
    
    @non_admin_user.setter
    def non_admin_user(self, value: Optional[pulumi.Input[CredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSharedPassword")
    def use_shared_password(self) -> Optional[pulumi.Input[EnableState]]:
        
        ...
    
    @use_shared_password.setter
    def use_shared_password(self, value: Optional[pulumi.Input[EnableState]]): # -> None:
        ...
    


