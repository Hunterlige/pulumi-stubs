

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectorResult', 'AwaitableGetConnectorResult', 'get_connector', 'get_connector_output']
@pulumi.output_type
class GetConnectorResult:
    
    def __init__(__self__, access_role=..., arn=..., as2_configs=..., egress_configs=..., id=..., logging_role=..., region=..., security_policy_name=..., service_managed_egress_ip_addresses=..., sftp_configs=..., tags=..., url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="as2Configs")
    def as2_configs(self) -> Sequence[outputs.GetConnectorAs2ConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressConfigs")
    def egress_configs(self) -> Sequence[outputs.GetConnectorEgressConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceManagedEgressIpAddresses")
    def service_managed_egress_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sftpConfigs")
    def sftp_configs(self) -> Sequence[outputs.GetConnectorSftpConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectorResult(GetConnectorResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectorResult]:
        ...
    


def get_connector(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectorResult:
    
    ...

def get_connector_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectorResult]:
    
    ...

