

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBrokerResult', 'AwaitableGetBrokerResult', 'get_broker', 'get_broker_output']
@pulumi.output_type
class GetBrokerResult:
    
    def __init__(__self__, arn=..., authentication_strategy=..., auto_minor_version_upgrade=..., broker_id=..., broker_name=..., configuration=..., deployment_mode=..., encryption_options=..., engine_type=..., engine_version=..., host_instance_type=..., id=..., instances=..., ldap_server_metadatas=..., logs=..., maintenance_window_start_time=..., publicly_accessible=..., region=..., security_groups=..., storage_type=..., subnet_ids=..., tags=..., users=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerId")
    def broker_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.GetBrokerConfigurationResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> Sequence[outputs.GetBrokerEncryptionOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.GetBrokerInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapServerMetadatas")
    def ldap_server_metadatas(self) -> Sequence[outputs.GetBrokerLdapServerMetadataResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> outputs.GetBrokerLogsResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> outputs.GetBrokerMaintenanceWindowStartTimeResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Sequence[outputs.GetBrokerUserResult]:
        
        ...
    


class AwaitableGetBrokerResult(GetBrokerResult):
    def __await__(self): # -> Generator[Never, Any, GetBrokerResult]:
        ...
    


def get_broker(broker_id: Optional[_builtins.str] = ..., broker_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBrokerResult:
    
    ...

def get_broker_output(broker_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., broker_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBrokerResult]:
    
    ...

