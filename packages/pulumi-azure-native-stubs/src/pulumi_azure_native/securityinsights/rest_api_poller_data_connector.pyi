

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RestApiPollerDataConnectorArgs', 'RestApiPollerDataConnector']
@pulumi.input_type
class RestApiPollerDataConnectorArgs:
    def __init__(__self__, *, auth: pulumi.Input[Union[AWSAuthModelArgs, ApiKeyAuthModelArgs, BasicAuthModelArgs, GCPAuthModelArgs, GenericBlobSbsAuthModelArgs, GitHubAuthModelArgs, JwtAuthModelArgs, NoneAuthModelArgs, OAuthModelArgs, OracleAuthModelArgs, SessionAuthModelArgs]], connector_definition_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], request: pulumi.Input[RestApiPollerRequestConfigArgs], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], add_on_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., data_type: Optional[pulumi.Input[_builtins.str]] = ..., dcr_config: Optional[pulumi.Input[DCRConfigurationArgs]] = ..., is_active: Optional[pulumi.Input[_builtins.bool]] = ..., paging: Optional[pulumi.Input[RestApiPollerRequestPagingConfigArgs]] = ..., response: Optional[pulumi.Input[CcpResponseConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> pulumi.Input[Union[AWSAuthModelArgs, ApiKeyAuthModelArgs, BasicAuthModelArgs, GCPAuthModelArgs, GenericBlobSbsAuthModelArgs, GitHubAuthModelArgs, JwtAuthModelArgs, NoneAuthModelArgs, OAuthModelArgs, OracleAuthModelArgs, SessionAuthModelArgs]]:
        
        ...
    
    @auth.setter
    def auth(self, value: pulumi.Input[Union[AWSAuthModelArgs, ApiKeyAuthModelArgs, BasicAuthModelArgs, GCPAuthModelArgs, GenericBlobSbsAuthModelArgs, GitHubAuthModelArgs, JwtAuthModelArgs, NoneAuthModelArgs, OAuthModelArgs, OracleAuthModelArgs, SessionAuthModelArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connector_definition_name.setter
    def connector_definition_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> pulumi.Input[RestApiPollerRequestConfigArgs]:
        
        ...
    
    @request.setter
    def request(self, value: pulumi.Input[RestApiPollerRequestConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addOnAttributes")
    def add_on_attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @add_on_attributes.setter
    def add_on_attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectorId")
    def data_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_connector_id.setter
    def data_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> Optional[pulumi.Input[DCRConfigurationArgs]]:
        
        ...
    
    @dcr_config.setter
    def dcr_config(self, value: Optional[pulumi.Input[DCRConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paging(self) -> Optional[pulumi.Input[RestApiPollerRequestPagingConfigArgs]]:
        
        ...
    
    @paging.setter
    def paging(self, value: Optional[pulumi.Input[RestApiPollerRequestPagingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[pulumi.Input[CcpResponseConfigArgs]]:
        
        ...
    
    @response.setter
    def response(self, value: Optional[pulumi.Input[CcpResponseConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RestApiPollerDataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., add_on_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., auth: Optional[pulumi.Input[Union[Union[AWSAuthModelArgs, AWSAuthModelArgsDict], Union[ApiKeyAuthModelArgs, ApiKeyAuthModelArgsDict], Union[BasicAuthModelArgs, BasicAuthModelArgsDict], Union[GCPAuthModelArgs, GCPAuthModelArgsDict], Union[GenericBlobSbsAuthModelArgs, GenericBlobSbsAuthModelArgsDict], Union[GitHubAuthModelArgs, GitHubAuthModelArgsDict], Union[JwtAuthModelArgs, JwtAuthModelArgsDict], Union[NoneAuthModelArgs, NoneAuthModelArgsDict], Union[OAuthModelArgs, OAuthModelArgsDict], Union[OracleAuthModelArgs, OracleAuthModelArgsDict], Union[SessionAuthModelArgs, SessionAuthModelArgsDict]]]] = ..., connector_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., data_type: Optional[pulumi.Input[_builtins.str]] = ..., dcr_config: Optional[pulumi.Input[Union[DCRConfigurationArgs, DCRConfigurationArgsDict]]] = ..., is_active: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., paging: Optional[pulumi.Input[Union[RestApiPollerRequestPagingConfigArgs, RestApiPollerRequestPagingConfigArgsDict]]] = ..., request: Optional[pulumi.Input[Union[RestApiPollerRequestConfigArgs, RestApiPollerRequestConfigArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., response: Optional[pulumi.Input[Union[CcpResponseConfigArgs, CcpResponseConfigArgsDict]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RestApiPollerDataConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RestApiPollerDataConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addOnAttributes")
    def add_on_attributes(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> pulumi.Output[Optional[outputs.DCRConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paging(self) -> pulumi.Output[Optional[outputs.RestApiPollerRequestPagingConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> pulumi.Output[outputs.RestApiPollerRequestConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> pulumi.Output[Optional[outputs.CcpResponseConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


