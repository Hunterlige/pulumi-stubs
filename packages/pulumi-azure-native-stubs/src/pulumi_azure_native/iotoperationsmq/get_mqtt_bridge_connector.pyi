

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMqttBridgeConnectorResult', 'AwaitableGetMqttBridgeConnectorResult', 'get_mqtt_bridge_connector', 'get_mqtt_bridge_connector_output']
@pulumi.output_type
class GetMqttBridgeConnectorResult:
    
    def __init__(__self__, azure_api_version=..., bridge_instances=..., client_id_prefix=..., extended_location=..., id=..., image=..., local_broker_connection=..., location=..., log_level=..., name=..., node_tolerations=..., protocol=..., provisioning_state=..., remote_broker_connection=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bridgeInstances")
    def bridge_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIdPrefix")
    def client_id_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> outputs.ContainerImageResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(self) -> Optional[outputs.LocalBrokerConnectionSpecResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(self) -> Optional[outputs.NodeTolerationsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteBrokerConnection")
    def remote_broker_connection(self) -> outputs.MqttBridgeRemoteBrokerConnectionSpecResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMqttBridgeConnectorResult(GetMqttBridgeConnectorResult):
    def __await__(self): # -> Generator[Never, Any, GetMqttBridgeConnectorResult]:
        ...
    


def get_mqtt_bridge_connector(mq_name: Optional[_builtins.str] = ..., mqtt_bridge_connector_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMqttBridgeConnectorResult:
    
    ...

def get_mqtt_bridge_connector_output(mq_name: Optional[pulumi.Input[_builtins.str]] = ..., mqtt_bridge_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMqttBridgeConnectorResult]:
    
    ...

