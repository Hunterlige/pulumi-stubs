

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoShutdownProfileResponse', 'ConnectionProfileResponse', 'CredentialsResponse', 'IdentityResponse', 'ImageReferenceResponse', 'LabNetworkProfileResponse', 'LabPlanNetworkProfileResponse', 'RecurrencePatternResponse', 'ResourceOperationErrorResponse', 'RosterProfileResponse', 'SecurityProfileResponse', 'SkuResponse', 'SupportInfoResponse', 'SystemDataResponse', 'VirtualMachineAdditionalCapabilitiesResponse', 'VirtualMachineProfileResponse']
@pulumi.output_type
class AutoShutdownProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disconnect_delay: Optional[_builtins.str] = ..., idle_delay: Optional[_builtins.str] = ..., no_connect_delay: Optional[_builtins.str] = ..., shutdown_on_disconnect: Optional[_builtins.str] = ..., shutdown_on_idle: Optional[_builtins.str] = ..., shutdown_when_not_connected: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectDelay")
    def disconnect_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDelay")
    def idle_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noConnectDelay")
    def no_connect_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownOnDisconnect")
    def shutdown_on_disconnect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownOnIdle")
    def shutdown_on_idle(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shutdownWhenNotConnected")
    def shutdown_when_not_connected(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_rdp_access: Optional[_builtins.str] = ..., client_ssh_access: Optional[_builtins.str] = ..., web_rdp_access: Optional[_builtins.str] = ..., web_ssh_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientRdpAccess")
    def client_rdp_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSshAccess")
    def client_ssh_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webRdpAccess")
    def web_rdp_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSshAccess")
    def web_ssh_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CredentialsResponse(dict):
    
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ImageReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exact_version: _builtins.str, id: Optional[_builtins.str] = ..., offer: Optional[_builtins.str] = ..., publisher: Optional[_builtins.str] = ..., sku: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LabNetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, load_balancer_id: Optional[_builtins.str] = ..., public_ip_id: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LabPlanNetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecurrencePatternResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expiration_date: _builtins.str, frequency: _builtins.str, interval: Optional[_builtins.int] = ..., week_days: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ResourceOperationErrorResponse(dict):
    
    def __init__(__self__, *, action: Optional[_builtins.str] = ..., code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RosterProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_directory_group_id: Optional[_builtins.str] = ..., lms_instance: Optional[_builtins.str] = ..., lti_client_id: Optional[_builtins.str] = ..., lti_context_id: Optional[_builtins.str] = ..., lti_roster_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryGroupId")
    def active_directory_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lmsInstance")
    def lms_instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiClientId")
    def lti_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiContextId")
    def lti_context_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ltiRosterEndpoint")
    def lti_roster_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registration_code: _builtins.str, open_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAccess")
    def open_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SupportInfoResponse(dict):
    
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., instructions: Optional[_builtins.str] = ..., phone: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineAdditionalCapabilitiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, install_gpu_drivers: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installGpuDrivers")
    def install_gpu_drivers(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_user: outputs.CredentialsResponse, create_option: _builtins.str, image_reference: outputs.ImageReferenceResponse, os_type: _builtins.str, sku: outputs.SkuResponse, usage_quota: _builtins.str, additional_capabilities: Optional[outputs.VirtualMachineAdditionalCapabilitiesResponse] = ..., non_admin_user: Optional[outputs.CredentialsResponse] = ..., use_shared_password: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> outputs.CredentialsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> outputs.ImageReferenceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageQuota")
    def usage_quota(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[outputs.VirtualMachineAdditionalCapabilitiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonAdminUser")
    def non_admin_user(self) -> Optional[outputs.CredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSharedPassword")
    def use_shared_password(self) -> Optional[_builtins.str]:
        
        ...
    


