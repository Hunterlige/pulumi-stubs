

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServiceNetworkServiceAssociationArgs', 'ServiceNetworkServiceAssociation']
@pulumi.input_type
class ServiceNetworkServiceAssociationArgs:
    def __init__(__self__, *, service_identifier: pulumi.Input[_builtins.str], service_network_identifier: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_identifier.setter
    def service_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_network_identifier.setter
    def service_network_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceNetworkServiceAssociationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_entries: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceNetworkServiceAssociationDnsEntryArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_identifier: Optional[pulumi.Input[_builtins.str]] = ..., service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceNetworkServiceAssociationDnsEntryArgs]]]]:
        
        ...
    
    @dns_entries.setter
    def dns_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceNetworkServiceAssociationDnsEntryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_identifier.setter
    def service_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_network_identifier.setter
    def service_network_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ServiceNetworkServiceAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_identifier: Optional[pulumi.Input[_builtins.str]] = ..., service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceNetworkServiceAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceNetworkServiceAssociationDnsEntryArgs, ServiceNetworkServiceAssociationDnsEntryArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_identifier: Optional[pulumi.Input[_builtins.str]] = ..., service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> ServiceNetworkServiceAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> pulumi.Output[Sequence[outputs.ServiceNetworkServiceAssociationDnsEntry]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIdentifier")
    def service_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


