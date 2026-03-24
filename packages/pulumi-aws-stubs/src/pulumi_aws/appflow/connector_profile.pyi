

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectorProfileArgs', 'ConnectorProfile']
@pulumi.input_type
class ConnectorProfileArgs:
    def __init__(__self__, *, connection_mode: pulumi.Input[_builtins.str], connector_profile_config: pulumi.Input[ConnectorProfileConnectorProfileConfigArgs], connector_type: pulumi.Input[_builtins.str], connector_label: Optional[pulumi.Input[_builtins.str]] = ..., kms_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_mode.setter
    def connection_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> pulumi.Input[ConnectorProfileConnectorProfileConfigArgs]:
        
        ...
    
    @connector_profile_config.setter
    def connector_profile_config(self, value: pulumi.Input[ConnectorProfileConnectorProfileConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_label.setter
    def connector_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectorProfileState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_mode: Optional[pulumi.Input[_builtins.str]] = ..., connector_label: Optional[pulumi.Input[_builtins.str]] = ..., connector_profile_config: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigArgs]] = ..., connector_type: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_mode.setter
    def connection_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_label.setter
    def connector_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigArgs]]:
        
        ...
    
    @connector_profile_config.setter
    def connector_profile_config(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:appflow/connectorProfile:ConnectorProfile")
class ConnectorProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_mode: Optional[pulumi.Input[_builtins.str]] = ..., connector_label: Optional[pulumi.Input[_builtins.str]] = ..., connector_profile_config: Optional[pulumi.Input[Union[ConnectorProfileConnectorProfileConfigArgs, ConnectorProfileConnectorProfileConfigArgsDict]]] = ..., connector_type: Optional[pulumi.Input[_builtins.str]] = ..., kms_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectorProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., connection_mode: Optional[pulumi.Input[_builtins.str]] = ..., connector_label: Optional[pulumi.Input[_builtins.str]] = ..., connector_profile_config: Optional[pulumi.Input[Union[ConnectorProfileConnectorProfileConfigArgs, ConnectorProfileConnectorProfileConfigArgsDict]]] = ..., connector_type: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ConnectorProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> pulumi.Output[outputs.ConnectorProfileConnectorProfileConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


