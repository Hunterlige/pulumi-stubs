

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAttachmentArgs', 'EndpointAttachment']
@pulumi.input_type
class EndpointAttachmentArgs:
    def __init__(__self__, *, endpoint_attachment_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], service_attachment: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAttachmentId")
    def endpoint_attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_attachment_id.setter
    def endpoint_attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_attachment.setter
    def service_attachment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointAttachmentState:
    def __init__(__self__, *, connection_state: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_state.setter
    def connection_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAttachmentId")
    def endpoint_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_attachment_id.setter
    def endpoint_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/endpointAttachment:EndpointAttachment")
class EndpointAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., endpoint_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connection_state: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ...) -> EndpointAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAttachmentId")
    def endpoint_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


