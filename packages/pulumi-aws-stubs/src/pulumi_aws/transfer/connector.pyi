

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, access_role: pulumi.Input[_builtins.str], as2_config: Optional[pulumi.Input[ConnectorAs2ConfigArgs]] = ..., egress_config: Optional[pulumi.Input[ConnectorEgressConfigArgs]] = ..., logging_role: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., sftp_config: Optional[pulumi.Input[ConnectorSftpConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_role.setter
    def access_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="as2Config")
    def as2_config(self) -> Optional[pulumi.Input[ConnectorAs2ConfigArgs]]:
        
        ...
    
    @as2_config.setter
    def as2_config(self, value: Optional[pulumi.Input[ConnectorAs2ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressConfig")
    def egress_config(self) -> Optional[pulumi.Input[ConnectorEgressConfigArgs]]:
        
        ...
    
    @egress_config.setter
    def egress_config(self, value: Optional[pulumi.Input[ConnectorEgressConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sftpConfig")
    def sftp_config(self) -> Optional[pulumi.Input[ConnectorSftpConfigArgs]]:
        
        ...
    
    @sftp_config.setter
    def sftp_config(self, value: Optional[pulumi.Input[ConnectorSftpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectorState:
    def __init__(__self__, *, access_role: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., as2_config: Optional[pulumi.Input[ConnectorAs2ConfigArgs]] = ..., connector_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_config: Optional[pulumi.Input[ConnectorEgressConfigArgs]] = ..., logging_role: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., sftp_config: Optional[pulumi.Input[ConnectorSftpConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_role.setter
    def access_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="as2Config")
    def as2_config(self) -> Optional[pulumi.Input[ConnectorAs2ConfigArgs]]:
        
        ...
    
    @as2_config.setter
    def as2_config(self, value: Optional[pulumi.Input[ConnectorAs2ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_id.setter
    def connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressConfig")
    def egress_config(self) -> Optional[pulumi.Input[ConnectorEgressConfigArgs]]:
        
        ...
    
    @egress_config.setter
    def egress_config(self, value: Optional[pulumi.Input[ConnectorEgressConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sftpConfig")
    def sftp_config(self) -> Optional[pulumi.Input[ConnectorSftpConfigArgs]]:
        
        ...
    
    @sftp_config.setter
    def sftp_config(self, value: Optional[pulumi.Input[ConnectorSftpConfigArgs]]): # -> None:
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
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:transfer/connector:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_role: Optional[pulumi.Input[_builtins.str]] = ..., as2_config: Optional[pulumi.Input[Union[ConnectorAs2ConfigArgs, ConnectorAs2ConfigArgsDict]]] = ..., egress_config: Optional[pulumi.Input[Union[ConnectorEgressConfigArgs, ConnectorEgressConfigArgsDict]]] = ..., logging_role: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., sftp_config: Optional[pulumi.Input[Union[ConnectorSftpConfigArgs, ConnectorSftpConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_role: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., as2_config: Optional[pulumi.Input[Union[ConnectorAs2ConfigArgs, ConnectorAs2ConfigArgsDict]]] = ..., connector_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_config: Optional[pulumi.Input[Union[ConnectorEgressConfigArgs, ConnectorEgressConfigArgsDict]]] = ..., logging_role: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., sftp_config: Optional[pulumi.Input[Union[ConnectorSftpConfigArgs, ConnectorSftpConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> Connector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="as2Config")
    def as2_config(self) -> pulumi.Output[Optional[outputs.ConnectorAs2Config]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressConfig")
    def egress_config(self) -> pulumi.Output[Optional[outputs.ConnectorEgressConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sftpConfig")
    def sftp_config(self) -> pulumi.Output[Optional[outputs.ConnectorSftpConfig]]:
        
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
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


