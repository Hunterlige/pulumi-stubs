

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FailoverGroupArgs', 'FailoverGroup']
@pulumi.input_type
class FailoverGroupArgs:
    def __init__(__self__, *, partner_servers: pulumi.Input[Sequence[pulumi.Input[PartnerInfoArgs]]], read_write_endpoint: pulumi.Input[FailoverGroupReadWriteEndpointArgs], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], databases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., failover_group_name: Optional[pulumi.Input[_builtins.str]] = ..., read_only_endpoint: Optional[pulumi.Input[FailoverGroupReadOnlyEndpointArgs]] = ..., secondary_type: Optional[pulumi.Input[Union[_builtins.str, FailoverGroupDatabasesSecondaryType]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Input[Sequence[pulumi.Input[PartnerInfoArgs]]]:
        
        ...
    
    @partner_servers.setter
    def partner_servers(self, value: pulumi.Input[Sequence[pulumi.Input[PartnerInfoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readWriteEndpoint")
    def read_write_endpoint(self) -> pulumi.Input[FailoverGroupReadWriteEndpointArgs]:
        
        ...
    
    @read_write_endpoint.setter
    def read_write_endpoint(self, value: pulumi.Input[FailoverGroupReadWriteEndpointArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverGroupName")
    def failover_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @failover_group_name.setter
    def failover_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyEndpoint")
    def read_only_endpoint(self) -> Optional[pulumi.Input[FailoverGroupReadOnlyEndpointArgs]]:
        
        ...
    
    @read_only_endpoint.setter
    def read_only_endpoint(self, value: Optional[pulumi.Input[FailoverGroupReadOnlyEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryType")
    def secondary_type(self) -> Optional[pulumi.Input[Union[_builtins.str, FailoverGroupDatabasesSecondaryType]]]:
        
        ...
    
    @secondary_type.setter
    def secondary_type(self, value: Optional[pulumi.Input[Union[_builtins.str, FailoverGroupDatabasesSecondaryType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:FailoverGroup")
class FailoverGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., databases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., failover_group_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PartnerInfoArgs, PartnerInfoArgsDict]]]]] = ..., read_only_endpoint: Optional[pulumi.Input[Union[FailoverGroupReadOnlyEndpointArgs, FailoverGroupReadOnlyEndpointArgsDict]]] = ..., read_write_endpoint: Optional[pulumi.Input[Union[FailoverGroupReadWriteEndpointArgs, FailoverGroupReadWriteEndpointArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., secondary_type: Optional[pulumi.Input[Union[_builtins.str, FailoverGroupDatabasesSecondaryType]]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FailoverGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FailoverGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Output[Sequence[outputs.PartnerInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyEndpoint")
    def read_only_endpoint(self) -> pulumi.Output[Optional[outputs.FailoverGroupReadOnlyEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readWriteEndpoint")
    def read_write_endpoint(self) -> pulumi.Output[outputs.FailoverGroupReadWriteEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


