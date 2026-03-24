

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
__all__ = ['ServiceIntegrationArgs', 'ServiceIntegration']
@pulumi.input_type
class ServiceIntegrationArgs:
    def __init__(__self__, *, kms_server_side_encryption: pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs], logs_anomaly_detection: pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs], ops_center: pulumi.Input[ServiceIntegrationOpsCenterArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsServerSideEncryption")
    def kms_server_side_encryption(self) -> pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs]:
        
        ...
    
    @kms_server_side_encryption.setter
    def kms_server_side_encryption(self, value: pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsAnomalyDetection")
    def logs_anomaly_detection(self) -> pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs]:
        
        ...
    
    @logs_anomaly_detection.setter
    def logs_anomaly_detection(self, value: pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="opsCenter")
    def ops_center(self) -> pulumi.Input[ServiceIntegrationOpsCenterArgs]:
        
        ...
    
    @ops_center.setter
    def ops_center(self, value: pulumi.Input[ServiceIntegrationOpsCenterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceIntegrationState:
    def __init__(__self__, *, kms_server_side_encryption: Optional[pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs]] = ..., logs_anomaly_detection: Optional[pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs]] = ..., ops_center: Optional[pulumi.Input[ServiceIntegrationOpsCenterArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsServerSideEncryption")
    def kms_server_side_encryption(self) -> Optional[pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs]]:
        
        ...
    
    @kms_server_side_encryption.setter
    def kms_server_side_encryption(self, value: Optional[pulumi.Input[ServiceIntegrationKmsServerSideEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsAnomalyDetection")
    def logs_anomaly_detection(self) -> Optional[pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs]]:
        
        ...
    
    @logs_anomaly_detection.setter
    def logs_anomaly_detection(self, value: Optional[pulumi.Input[ServiceIntegrationLogsAnomalyDetectionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="opsCenter")
    def ops_center(self) -> Optional[pulumi.Input[ServiceIntegrationOpsCenterArgs]]:
        
        ...
    
    @ops_center.setter
    def ops_center(self, value: Optional[pulumi.Input[ServiceIntegrationOpsCenterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ServiceIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., kms_server_side_encryption: Optional[pulumi.Input[Union[ServiceIntegrationKmsServerSideEncryptionArgs, ServiceIntegrationKmsServerSideEncryptionArgsDict]]] = ..., logs_anomaly_detection: Optional[pulumi.Input[Union[ServiceIntegrationLogsAnomalyDetectionArgs, ServiceIntegrationLogsAnomalyDetectionArgsDict]]] = ..., ops_center: Optional[pulumi.Input[Union[ServiceIntegrationOpsCenterArgs, ServiceIntegrationOpsCenterArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceIntegrationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., kms_server_side_encryption: Optional[pulumi.Input[Union[ServiceIntegrationKmsServerSideEncryptionArgs, ServiceIntegrationKmsServerSideEncryptionArgsDict]]] = ..., logs_anomaly_detection: Optional[pulumi.Input[Union[ServiceIntegrationLogsAnomalyDetectionArgs, ServiceIntegrationLogsAnomalyDetectionArgsDict]]] = ..., ops_center: Optional[pulumi.Input[Union[ServiceIntegrationOpsCenterArgs, ServiceIntegrationOpsCenterArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ServiceIntegration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsServerSideEncryption")
    def kms_server_side_encryption(self) -> pulumi.Output[outputs.ServiceIntegrationKmsServerSideEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsAnomalyDetection")
    def logs_anomaly_detection(self) -> pulumi.Output[outputs.ServiceIntegrationLogsAnomalyDetection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="opsCenter")
    def ops_center(self) -> pulumi.Output[outputs.ServiceIntegrationOpsCenter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


