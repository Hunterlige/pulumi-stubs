

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
__all__ = ['MySQLServerArgs', 'MySQLServer']
@pulumi.input_type
class MySQLServerArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], port_number: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], site_name: pulumi.Input[_builtins.str], edition: Optional[pulumi.Input[Union[_builtins.str, Edition]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[ErrorArgs]]]] = ..., host_ip: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_id: Optional[pulumi.Input[_builtins.str]] = ..., mysql_version: Optional[pulumi.Input[_builtins.str]] = ..., number_of_database: Optional[pulumi.Input[_builtins.float]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., support_end_in: Optional[pulumi.Input[_builtins.str]] = ..., support_status: Optional[pulumi.Input[Union[_builtins.str, SupportStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @port_number.setter
    def port_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[Union[_builtins.str, Edition]]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[Union[_builtins.str, Edition]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ErrorArgs]]]]:
        
        ...
    
    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ErrorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIp")
    def host_ip(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @host_ip.setter
    def host_ip(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_id.setter
    def machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mysqlVersion")
    def mysql_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mysql_version.setter
    def mysql_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfDatabase")
    def number_of_database(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @number_of_database.setter
    def number_of_database(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportEndIn")
    def support_end_in(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @support_end_in.setter
    def support_end_in(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportStatus")
    def support_status(self) -> Optional[pulumi.Input[Union[_builtins.str, SupportStatus]]]:
        
        ...
    
    @support_status.setter
    def support_status(self, value: Optional[pulumi.Input[Union[_builtins.str, SupportStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:mysqldiscovery:MySQLServer")
class MySQLServer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., edition: Optional[pulumi.Input[Union[_builtins.str, Edition]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ErrorArgs, ErrorArgsDict]]]]] = ..., host_ip: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., host_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_id: Optional[pulumi.Input[_builtins.str]] = ..., mysql_version: Optional[pulumi.Input[_builtins.str]] = ..., number_of_database: Optional[pulumi.Input[_builtins.float]] = ..., port_number: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., site_name: Optional[pulumi.Input[_builtins.str]] = ..., support_end_in: Optional[pulumi.Input[_builtins.str]] = ..., support_status: Optional[pulumi.Input[Union[_builtins.str, SupportStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MySQLServerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MySQLServer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Optional[Sequence[outputs.ErrorResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIp")
    def host_ip(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mysqlVersion")
    def mysql_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfDatabase")
    def number_of_database(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportEndIn")
    def support_end_in(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportStatus")
    def support_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


