

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBootstrapBrokersResult', 'AwaitableGetBootstrapBrokersResult', 'get_bootstrap_brokers', 'get_bootstrap_brokers_output']
@pulumi.output_type
class GetBootstrapBrokersResult:
    
    def __init__(__self__, bootstrap_brokers=..., bootstrap_brokers_public_sasl_iam=..., bootstrap_brokers_public_sasl_scram=..., bootstrap_brokers_public_tls=..., bootstrap_brokers_sasl_iam=..., bootstrap_brokers_sasl_scram=..., bootstrap_brokers_tls=..., bootstrap_brokers_vpc_connectivity_sasl_iam=..., bootstrap_brokers_vpc_connectivity_sasl_scram=..., bootstrap_brokers_vpc_connectivity_tls=..., cluster_arn=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokers")
    def bootstrap_brokers(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslIam")
    def bootstrap_brokers_public_sasl_iam(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslScram")
    def bootstrap_brokers_public_sasl_scram(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicTls")
    def bootstrap_brokers_public_tls(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslIam")
    def bootstrap_brokers_vpc_connectivity_sasl_iam(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslScram")
    def bootstrap_brokers_vpc_connectivity_sasl_scram(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivityTls")
    def bootstrap_brokers_vpc_connectivity_tls(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetBootstrapBrokersResult(GetBootstrapBrokersResult):
    def __await__(self): # -> Generator[Never, Any, GetBootstrapBrokersResult]:
        ...
    


def get_bootstrap_brokers(cluster_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBootstrapBrokersResult:
    
    ...

def get_bootstrap_brokers_output(cluster_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBootstrapBrokersResult]:
    
    ...

