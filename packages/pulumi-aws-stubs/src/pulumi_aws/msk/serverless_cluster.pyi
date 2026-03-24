

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
__all__ = ['ServerlessClusterArgs', 'ServerlessCluster']
@pulumi.input_type
class ServerlessClusterArgs:
    def __init__(__self__, *, client_authentication: pulumi.Input[ServerlessClusterClientAuthenticationArgs], vpc_configs: pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]], cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Input[ServerlessClusterClientAuthenticationArgs]:
        
        ...
    
    @client_authentication.setter
    def client_authentication(self, value: pulumi.Input[ServerlessClusterClientAuthenticationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]]:
        
        ...
    
    @vpc_configs.setter
    def vpc_configs(self, value: pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _ServerlessClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., client_authentication: Optional[pulumi.Input[ServerlessClusterClientAuthenticationArgs]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_uuid: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_sasl_iam.setter
    def bootstrap_brokers_sasl_iam(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> Optional[pulumi.Input[ServerlessClusterClientAuthenticationArgs]]:
        
        ...
    
    @client_authentication.setter
    def client_authentication(self, value: Optional[pulumi.Input[ServerlessClusterClientAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_uuid.setter
    def cluster_uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]]]:
        
        ...
    
    @vpc_configs.setter
    def vpc_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServerlessClusterVpcConfigArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:msk/serverlessCluster:ServerlessCluster")
class ServerlessCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., client_authentication: Optional[pulumi.Input[Union[ServerlessClusterClientAuthenticationArgs, ServerlessClusterClientAuthenticationArgsDict]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServerlessClusterVpcConfigArgs, ServerlessClusterVpcConfigArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServerlessClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., client_authentication: Optional[pulumi.Input[Union[ServerlessClusterClientAuthenticationArgs, ServerlessClusterClientAuthenticationArgsDict]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_uuid: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServerlessClusterVpcConfigArgs, ServerlessClusterVpcConfigArgsDict]]]]] = ...) -> ServerlessCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Output[outputs.ServerlessClusterClientAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> pulumi.Output[Sequence[outputs.ServerlessClusterVpcConfig]]:
        
        ...
    


