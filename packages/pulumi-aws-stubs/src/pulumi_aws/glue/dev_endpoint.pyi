

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DevEndpointArgs', 'DevEndpoint']
@pulumi.input_type
class DevEndpointArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., extra_jars_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., extra_python_libs_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., glue_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ..., number_of_workers: Optional[pulumi.Input[_builtins.int]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., worker_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraJarsS3Path")
    def extra_jars_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extra_jars_s3_path.setter
    def extra_jars_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraPythonLibsS3Path")
    def extra_python_libs_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extra_python_libs_s3_path.setter
    def extra_python_libs_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @public_keys.setter
    def public_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DevEndpointState:
    def __init__(__self__, *, arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., extra_jars_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., extra_python_libs_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., glue_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ..., number_of_workers: Optional[pulumi.Input[_builtins.int]] = ..., private_address: Optional[pulumi.Input[_builtins.str]] = ..., public_address: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., worker_type: Optional[pulumi.Input[_builtins.str]] = ..., yarn_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ..., zeppelin_remote_spark_interpreter_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraJarsS3Path")
    def extra_jars_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extra_jars_s3_path.setter
    def extra_jars_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraPythonLibsS3Path")
    def extra_python_libs_s3_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extra_python_libs_s3_path.setter
    def extra_python_libs_s3_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateAddress")
    def private_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_address.setter
    def private_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAddress")
    def public_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_address.setter
    def public_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @public_keys.setter
    def public_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="yarnEndpointAddress")
    def yarn_endpoint_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @yarn_endpoint_address.setter
    def yarn_endpoint_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeppelinRemoteSparkInterpreterPort")
    def zeppelin_remote_spark_interpreter_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @zeppelin_remote_spark_interpreter_port.setter
    def zeppelin_remote_spark_interpreter_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/devEndpoint:DevEndpoint")
class DevEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., extra_jars_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., extra_python_libs_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., glue_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ..., number_of_workers: Optional[pulumi.Input[_builtins.int]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., worker_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DevEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., extra_jars_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., extra_python_libs_s3_path: Optional[pulumi.Input[_builtins.str]] = ..., failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., glue_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ..., number_of_workers: Optional[pulumi.Input[_builtins.int]] = ..., private_address: Optional[pulumi.Input[_builtins.str]] = ..., public_address: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., worker_type: Optional[pulumi.Input[_builtins.str]] = ..., yarn_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ..., zeppelin_remote_spark_interpreter_port: Optional[pulumi.Input[_builtins.int]] = ...) -> DevEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraJarsS3Path")
    def extra_jars_s3_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraPythonLibsS3Path")
    def extra_python_libs_s3_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateAddress")
    def private_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAddress")
    def public_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yarnEndpointAddress")
    def yarn_endpoint_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeppelinRemoteSparkInterpreterPort")
    def zeppelin_remote_spark_interpreter_port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


