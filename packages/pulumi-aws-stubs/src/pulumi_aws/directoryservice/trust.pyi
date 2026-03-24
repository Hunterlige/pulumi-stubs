

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TrustArgs', 'Trust']
@pulumi.input_type
class TrustArgs:
    def __init__(__self__, *, directory_id: pulumi.Input[_builtins.str], remote_domain_name: pulumi.Input[_builtins.str], trust_direction: pulumi.Input[_builtins.str], trust_password: pulumi.Input[_builtins.str], conditional_forwarder_ip_addrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delete_associated_conditional_forwarder: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., selective_auth: Optional[pulumi.Input[_builtins.str]] = ..., trust_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @remote_domain_name.setter
    def remote_domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trust_direction.setter
    def trust_direction(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustPassword")
    def trust_password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trust_password.setter
    def trust_password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalForwarderIpAddrs")
    def conditional_forwarder_ip_addrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @conditional_forwarder_ip_addrs.setter
    def conditional_forwarder_ip_addrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedConditionalForwarder")
    def delete_associated_conditional_forwarder(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_associated_conditional_forwarder.setter
    def delete_associated_conditional_forwarder(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectiveAuth")
    def selective_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selective_auth.setter
    def selective_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_type.setter
    def trust_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TrustState:
    def __init__(__self__, *, conditional_forwarder_ip_addrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., created_date_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_conditional_forwarder: Optional[pulumi.Input[_builtins.bool]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., selective_auth: Optional[pulumi.Input[_builtins.str]] = ..., state_last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ..., trust_direction: Optional[pulumi.Input[_builtins.str]] = ..., trust_password: Optional[pulumi.Input[_builtins.str]] = ..., trust_state: Optional[pulumi.Input[_builtins.str]] = ..., trust_state_reason: Optional[pulumi.Input[_builtins.str]] = ..., trust_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalForwarderIpAddrs")
    def conditional_forwarder_ip_addrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @conditional_forwarder_ip_addrs.setter
    def conditional_forwarder_ip_addrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_date_time.setter
    def created_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedConditionalForwarder")
    def delete_associated_conditional_forwarder(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_associated_conditional_forwarder.setter
    def delete_associated_conditional_forwarder(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDateTime")
    def last_updated_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_date_time.setter
    def last_updated_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_domain_name.setter
    def remote_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectiveAuth")
    def selective_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selective_auth.setter
    def selective_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateLastUpdatedDateTime")
    def state_last_updated_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_last_updated_date_time.setter
    def state_last_updated_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_direction.setter
    def trust_direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustPassword")
    def trust_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_password.setter
    def trust_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustState")
    def trust_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_state.setter
    def trust_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStateReason")
    def trust_state_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_state_reason.setter
    def trust_state_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_type.setter
    def trust_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:directoryservice/trust:Trust")
class Trust(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., conditional_forwarder_ip_addrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delete_associated_conditional_forwarder: Optional[pulumi.Input[_builtins.bool]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., selective_auth: Optional[pulumi.Input[_builtins.str]] = ..., trust_direction: Optional[pulumi.Input[_builtins.str]] = ..., trust_password: Optional[pulumi.Input[_builtins.str]] = ..., trust_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TrustArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., conditional_forwarder_ip_addrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., created_date_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_conditional_forwarder: Optional[pulumi.Input[_builtins.bool]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., selective_auth: Optional[pulumi.Input[_builtins.str]] = ..., state_last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ..., trust_direction: Optional[pulumi.Input[_builtins.str]] = ..., trust_password: Optional[pulumi.Input[_builtins.str]] = ..., trust_state: Optional[pulumi.Input[_builtins.str]] = ..., trust_state_reason: Optional[pulumi.Input[_builtins.str]] = ..., trust_type: Optional[pulumi.Input[_builtins.str]] = ...) -> Trust:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalForwarderIpAddrs")
    def conditional_forwarder_ip_addrs(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedConditionalForwarder")
    def delete_associated_conditional_forwarder(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDateTime")
    def last_updated_date_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDomainName")
    def remote_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectiveAuth")
    def selective_auth(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateLastUpdatedDateTime")
    def state_last_updated_date_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustPassword")
    def trust_password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustState")
    def trust_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStateReason")
    def trust_state_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


